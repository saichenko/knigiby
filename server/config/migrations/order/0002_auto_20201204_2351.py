# Generated by Django 3.0.8 on 2020-12-04 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercomment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='order.Order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='ordercomment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile', verbose_name='Профлиль'),
        ),
    ]