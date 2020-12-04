from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.products.models.products import ProductComment, Product


@receiver(post_save, sender=ProductComment)
def count_product_avg_rate(sender, instance, **kwargs):
    product = Product.objects.get(id=instance.product.id)
    product.rating = product.product_comment.all().aggregate(Avg('rate'))['rate__avg']
    product.save()
