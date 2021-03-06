# Generated by Django 2.0.13 on 2020-07-18 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200718_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogmodel',
            name='categories',
            field=models.CharField(choices=[('1', 'Новостройки'), ('2', 'Квартиры'), ('3', 'Дома'), ('4', 'Аренда'), ('5', 'Вторичное'), ('6', 'Земельные участки'), ('7', 'Застройщики ')], default='1', max_length=2, verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='catalogmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='загрузить изображение'),
        ),
    ]
