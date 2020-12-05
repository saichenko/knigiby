from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.order.models.models import Order


@receiver(post_save, sender=Order)
def notify_about_order(sender, instance, **kwargs):
    # TODO: Send mail notification to the customer and staff
    pass
