# Generated by Django 2.0.13 on 2020-08-15 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-date',), 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
