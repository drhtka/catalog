# Generated by Django 2.0.13 on 2020-07-01 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200629_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='name_flate',
            field=models.TextField(blank=True, verbose_name='Название кв'),
        ),
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.TextField(blank=True, verbose_name='Цена'),
        ),
    ]