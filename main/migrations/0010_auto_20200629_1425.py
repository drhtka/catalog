# Generated by Django 2.0.13 on 2020-06-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.TextField(blank=True, verbose_name='Почта'),
        ),
        migrations.AddField(
            model_name='orders',
            name='tel',
            field=models.TextField(blank=True, verbose_name='Телефон'),
        ),
    ]