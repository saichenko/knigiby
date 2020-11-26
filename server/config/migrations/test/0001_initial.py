# Generated by Django 3.0.8 on 2020-11-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('random_string', models.CharField(blank=True, max_length=255, null=True, verbose_name='Рандномная строка')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тест',
            },
        ),
    ]
