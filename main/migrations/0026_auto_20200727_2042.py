# Generated by Django 2.0.13 on 2020-07-27 17:42

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20200720_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalogmodel',
            options={'verbose_name': 'Квартиру', 'verbose_name_plural': 'Добавление квартиры'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Галерея', 'verbose_name_plural': 'Галереи'},
        ),
        migrations.RemoveField(
            model_name='catalogmodel',
            name='mortgage',
        ),
        migrations.RemoveField(
            model_name='catalogmodel',
            name='photo_arr',
        ),
        migrations.RemoveField(
            model_name='catalogmodel',
            name='type_of_transaction',
        ),
        migrations.AddField(
            model_name='catalogmodel',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='catalogmodel',
            name='number_of_rooms',
            field=models.CharField(choices=[('1', 'Одна'), ('2', 'Две'), ('3', 'Три'), ('4', 'Четыре'), ('5', 'Пять+'), ('6', 'Студия'), ('7', 'Общежите')], default='1', max_length=2, verbose_name='Количество комнат'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Галерея'),
        ),
        migrations.AlterModelTable(
            name='image',
            table='photos',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
