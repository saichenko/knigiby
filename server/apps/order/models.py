from django.db import models

from apps.cart.models import Cart
from apps.users.models import Profile


class Order(models.Model):
    RECEIVING_METHOD_CHOICES = [
        (1, 'Самовывоз'),
        (2, 'Доставка')
    ]

    STATUS_CHOICES = [
        (1, 'Заказ принят. Идет обработка заказа.'),
        (2, 'Заказ ожидает в пункте выдачи.'),
        (3, 'Посылка принята.'),
        (4, 'В пути.'),
        (5, 'Заказ доставлен.'),
        (6, 'Заказ выполнен.'),
    ]

    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.PROTECT)
    profile = models.ForeignKey(Profile, verbose_name='Профиль', on_delete=models.PROTECT, related_name='order')
    receiving_method = models.PositiveSmallIntegerField(verbose_name='Способ получения', choices=RECEIVING_METHOD_CHOICES)
    status = models.PositiveSmallIntegerField(verbose_name='Статус заказа', choices=STATUS_CHOICES)
    byn_price = models.PositiveSmallIntegerField('Цена, бел. рубли')
    created = models.DateTimeField('Создан', auto_now_add=True)
    last_modified = models.DateTimeField('Последнее изменение', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.id} для {self.profile.user.username} от {self.created}'


class OrderComment(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE, related_name='order_comment')
    profile = models.ForeignKey(Profile, verbose_name='Профлиль', on_delete=models.CASCADE, related_name='order_comment')
    text = models.TextField('Текст')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Комментарий к заказу'
        verbose_name_plural = 'Коментарии к заказам'

    def __str__(self):
        return f'Комментарий к {self.order} от {self.created}'
