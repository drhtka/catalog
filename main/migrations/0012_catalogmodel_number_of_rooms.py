# Generated by Django 2.0.13 on 2020-07-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200701_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogmodel',
            name='number_of_rooms',
            field=models.TextField(blank=True, verbose_name='Количество комнат'),
        ),
    ]