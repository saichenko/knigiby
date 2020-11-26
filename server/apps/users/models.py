from django.contrib.auth.models import User
from django.db import models

from apps.secondary_objects.models.locational import Country, Address


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    phone_num_code = models.ForeignKey(Country, verbose_name='Код номера тел.',  on_delete=models.CASCADE)
    phone_num = models.CharField('Номер тел.', max_length=12)
    address = models.ForeignKey(Address, verbose_name='Адрес',  null=True, blank=True, on_delete=models.CASCADE, related_name='address')
    opt_address = models.ForeignKey(Address, verbose_name='Доп. адрес',  null=True, blank=True, on_delete=models.CASCADE, related_name='opt_adress')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user.username} профиль'
