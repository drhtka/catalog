# Generated by Django 2.0.13 on 2020-08-29 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20200827_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogmodel',
            name='pages',
            field=models.CharField(blank=True, help_text='Вписать район', max_length=255, null=True, verbose_name='Район'),
        ),
    ]