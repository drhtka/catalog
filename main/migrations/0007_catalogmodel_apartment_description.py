# Generated by Django 2.0.13 on 2020-06-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200624_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogmodel',
            name='apartment_description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
