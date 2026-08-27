from django.db import models, transaction
from django.utils import timezone
from accounts.models import ServiceRecord


class Invoice(models.Model):
    DISCOUNT_CHOICES = [
        ('none', 'No discount'),
        ('percentage', 'Percentage off'),
        ('fixed', 'Fixed amount off'),
    ]

    invoice_number = models.CharField(max_length=20, unique=True, editable=False)
    service_record = models.OneToOneField(ServiceRecord, on_delete=models.CASCADE, related_name='invoice')
    issue_date = models.DateField(default=timezone.localdate)
    due_date = models.DateField(null=True, blank=True)
    bill_to_name = models.CharField(max_length=150)
    bill_to_email = models.EmailField(blank=True)
    bill_to_phone = models.CharField(max_length=30, blank=True)

    discount_type = models.CharField(max_length=10, choices=DISCOUNT_CHOICES, default='none')
    discount_value = models.PositiveIntegerField(
        default=0,
        help_text="If percentage: whole number 0-100. If fixed: amount in cents."
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = self.issue_date + timezone.timedelta(days=2)
        if not self.invoice_number:
            self.invoice_number = self._generate_invoice_number()
        super().save(*args, **kwargs)

    def _generate_invoice_number(self):
        date_str = self.issue_date.strftime('%d%m%Y')
        with transaction.atomic():
            count_today = Invoice.objects.select_for_update().filter(
                invoice_number__startswith=date_str
            ).count()
        return f"{date_str}{count_today + 1}"

    @property
    def subtotal_cents(self):
        return sum(item.line_total_cents for item in self.items.all())

    @property
    def discount_cents(self):
        if self.discount_type == 'percentage':
            return round(self.subtotal_cents * self.discount_value / 100)
        elif self.discount_type == 'fixed':
            return min(self.discount_value, self.subtotal_cents)
        return 0

    @property
    def net_total_cents(self):
        return self.subtotal_cents - self.discount_cents

    @property
    def tax_cents(self):
        return round(self.net_total_cents * 0.1)

    @property
    def total_cents(self):
        return self.net_total_cents + self.tax_cents

    # Dollar-formatted display properties
    @property
    def subtotal_display(self):
        return f"{self.subtotal_cents / 100:.2f}"

    @property
    def discount_display(self):
        return f"{self.discount_cents / 100:.2f}"

    @property
    def net_total_display(self):
        return f"{self.net_total_cents / 100:.2f}"

    @property
    def tax_display(self):
        return f"{self.tax_cents / 100:.2f}"

    @property
    def total_display(self):
        return f"{self.total_cents / 100:.2f}"

    def __str__(self):
        return f"Invoice {self.invoice_number}"


class InvoiceLineItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price_cents = models.PositiveIntegerField()

    @property
    def line_total_cents(self):
        return self.quantity * self.unit_price_cents

    @property
    def unit_price_display(self):
        return f"{self.unit_price_cents / 100:.2f}"

    @property
    def line_total_display(self):
        return f"{self.line_total_cents / 100:.2f}"