# Generated by Django 2.0.13 on 2020-08-17 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20200817_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogmodel',
            name='categories',
            field=models.CharField(choices=[('Новостройки', 'Новостройки'), ('2', 'Квартиры'), ('3', 'Дома'), ('4', 'Аренда'), ('5', 'Вторичное'), ('6', 'Земельные участки'), ('7', 'Застройщики '), ('vip', 'vip ')], default='Новостройки', max_length=15, verbose_name='Категории'),
        ),
    ]
