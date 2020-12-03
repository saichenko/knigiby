from django.db import models

from apps.products.models.products import Product
from apps.users.models.profiles import Profile


class Cart(models.Model):
    profile = models.ForeignKey(Profile, verbose_name='Профиль', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, verbose_name='Товары')
    created = models.DateTimeField('Создано', auto_now_add=True)
    last_modified = models.DateTimeField('Последнее изменение', auto_now=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.profile.user.username} корзина'
