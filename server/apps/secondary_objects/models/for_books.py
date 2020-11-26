from django.db import models


class Genre(models.Model):
    name = models.CharField('Название', max_length=120)
    description = models.TextField('Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.name}'


class BookSeries(models.Model):
    name = models.CharField('Название')
    description = models.TextField('Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

    def __str__(self):
        return f'{self.name}'


class Publisher(models.Model):
    name = models.CharField('Название', max_length=70)
    description = models.TextField('Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    middle_name = models.CharField('Отчество', max_length=30, null=True, blank=True)
    last_name = models.CharField('Фамилия', max_length=40)
    description = models.TextField('Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
