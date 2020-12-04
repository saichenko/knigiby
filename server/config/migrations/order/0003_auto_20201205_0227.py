# Generated by Django 3.0.8 on 2020-12-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20201204_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Заказ принят. Идет обработка заказа.'), (2, 'Заказ ожидает в пункте выдачи.'), (3, 'Посылка принята.'), (4, 'В пути.'), (5, 'Заказ доставлен.'), (6, 'Заказ выполнен.')], default=1, verbose_name='Статус заказа'),
        ),
    ]
