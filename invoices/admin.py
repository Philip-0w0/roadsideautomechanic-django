from django.contrib import admin
from django.utils.html import format_html
from .models import Invoice, InvoiceLineItem


class InvoiceLineItemInline(admin.TabularInline):
    model = InvoiceLineItem
    extra = 0


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'bill_to_name', 'issue_date', 'discount_type', 'download_link')
    list_filter = ('discount_type',)
    fields = (
        'invoice_number', 'service_record', 'issue_date', 'due_date',
        'bill_to_name', 'bill_to_email', 'bill_to_phone',
        'discount_type', 'discount_value',
    )
    readonly_fields = ('invoice_number',)
    inlines = [InvoiceLineItemInline]

    def download_link(self, obj):
        return format_html('<a href="/invoices/{}/pdf/" target="_blank">Download PDF</a>', obj.id)
    download_link.short_description = 'PDF'