# Generated by Django 2.0.13 on 2020-08-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20200801_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogmodel',
            name='float_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Квартиры'),
        ),
        migrations.AlterField(
            model_name='catalogmodel',
            name='goods',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Товары'),
        ),
        migrations.AlterField(
            model_name='catalogmodel',
            name='object_type',
            field=models.CharField(blank=True, max_length=255, verbose_name='Тип объекта'),
        ),
        migrations.AlterField(
            model_name='catalogmodel',
            name='pages',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Страницы'),
        ),
        migrations.AlterField(
            model_name='catalogmodel',
            name='photos',
            field=models.CharField(blank=True, max_length=255, verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='catalogmodel',
            name='quadrature',
            field=models.CharField(blank=True, max_length=255, verbose_name='Квадратура'),
        ),
    ]
