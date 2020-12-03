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


class Street(models.Model):
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=190)

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.ForeignKey(Street, verbose_name='Улица', on_delete=models.CASCADE)
    house = models.CharField('Дом', max_length=6)
    apartment = models.PositiveSmallIntegerField('Номер кв.')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.street}, {self.house}'
