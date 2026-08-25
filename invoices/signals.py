from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import ServiceRecord
from .models import Invoice, InvoiceLineItem


@receiver(post_save, sender=ServiceRecord)
def create_invoice_for_service_record(sender, instance, created, **kwargs):
    if not created or instance.cost_cents is None:
        return
    if hasattr(instance, 'invoice'):
        return

    vehicle = instance.vehicle
    owner = vehicle.owner
    booking = instance.booking

    if owner:
        bill_to_name = owner.get_full_name() or owner.username
        bill_to_email = owner.email
    elif booking:
        bill_to_name = booking.customer_name
        bill_to_email = booking.email
    else:
        bill_to_name = str(vehicle)
        bill_to_email = ''

    invoice = Invoice.objects.create(
        service_record=instance,
        bill_to_name=bill_to_name,
        bill_to_email=bill_to_email,
        bill_to_phone=booking.phone if booking else '',
    )
    InvoiceLineItem.objects.create(
        invoice=invoice,
        description=instance.description,
        quantity=1,
        unit_price_cents=instance.cost_cents,
    )
    