# Generated by Django 3.0.8 on 2020-12-04 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secondary_objects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.CharField(max_length=12, verbose_name='Номер тел.')),
                ('address', models.ManyToManyField(related_name='profile', to='secondary_objects.Address', verbose_name='Адрес')),
                ('phone_num_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondary_objects.Country', verbose_name='Код номера тел.')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
