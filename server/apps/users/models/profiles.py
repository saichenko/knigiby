from django.contrib.auth.models import User
from django.db import models

from apps.secondary_objects.models.locational import Country, Address


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_num_code = models.ForeignKey(Country, verbose_name='Код номера тел.',  on_delete=models.CASCADE)
    phone_num = models.CharField('Номер тел.', max_length=12)
    address = models.ManyToManyField(Address, verbose_name='Адрес', related_name='profile')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user.username} профиль'
