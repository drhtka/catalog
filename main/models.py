# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class CatalogModel(models.Model):
    #Каталог товаров
    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    categories = models.TextField('Категории', max_length=30, blank=True, null=True)
    goods = models.TextField('Товары', blank=True, null=True)
    pages = models.TextField('Страницы', blank=True, null=True)
    float_name = models.TextField('Квартиры', blank=True)
    photos = models.TextField('Фотография', blank=True)
    photo_arr = models.TextField('Фотографии', blank=True)

    class Meta:
        verbose_name = 'Каталог '
        verbose_name_plural = 'Каталоги'
        db_table = 'catalogmodel'

class Users(models.Model):
    # пользователи
    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    username = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=30, blank=True, null=True)
    user_pass = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        #managed = True
        db_table = 'users'

class Categories(models.Model):
    #Категории
    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    cat_name = models.TextField('Категории', max_length=30, blank=True, null=True)
    cat_url = models.TextField('Категории', max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'categor'
