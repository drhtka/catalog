# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class CatalogModel(models.Model):
    #Каталог товаров
    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    categories = models.TextField('Категории', max_length=30, blank=True, null=True)
    goods = models.TextField('Товары', blank=True, null=True)
    pages = models.TextField('Страницы', blank=True, null=True)
    users = models.TextField('Пользователи', blank=True)

    class Meta:
        verbose_name = 'Каталог '
        verbose_name_plural = 'Каталоги'
        db_table = 'catalogmodel'