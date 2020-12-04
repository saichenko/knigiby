from django.db import models
from django.core.exceptions import ValidationError


class DollarValue(models.Model):
    value = models.DecimalField('Цена USD к BYN', max_digits=6, decimal_places=2)
    last_modified = models.DateTimeField('Последнее изменение', auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk and DollarValue.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one DollarValue instance')
        return super(DollarValue, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Курс доллара'
        verbose_name_plural = 'Курсы'
