# Generated by Django 2.0.13 on 2020-07-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_image_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
