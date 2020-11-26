from django.db import models


class Country(models.Model):
    name = models.CharField('Название', max_length=50)
    code = models.PositiveSmallIntegerField('Код страны')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.CASCADE)
    name = models.CharField('Название города', max_length=60)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'


class Address(models.Model):
    city = models.ForeignKey(City, verbose_name='Город',  on_delete=models.CASCADE)
    street_and_house = models.CharField('Улица, дом, кв', max_length=200)

    # Filled in automatically.
    postcode = models.CharField(max_length=9)
    longitude = models.DecimalField(max_digits=18, decimal_places=6)
    latitude = models.DecimalField(max_digits=18, decimal_places=6)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.city}, {self.address}'
