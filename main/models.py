# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField
# Create your models here.
from photologue.models import Gallery


class CatalogModel(models.Model):
    # Каталог товаров

    class Meta:
        verbose_name = 'Квартиру'
        verbose_name_plural = 'Объекты и добавление'
        db_table = 'catalogmodel'

    novostroj = '1'
    flat = '2'
    homes = '3'
    rent = '4'
    second = '5'
    land = '6'
    property = '7'
    vip = '8'
    sale = '9'
    YEAR_IN_SCHOOL_CHOICES = (
        (novostroj, 'Новостройки'),
        (flat, 'Квартиры'),
        (homes, 'Дома'),
        (rent, 'Аренда'),
        (second, 'Вторичное'),
        (land, 'Земельные участки'),
        (property, 'Застройщики '),
        (vip, 'vip'),
        (sale, 'sale'),
    )

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    categories = models.CharField(max_length=15, verbose_name='Категории', choices=YEAR_IN_SCHOOL_CHOICES,
                                  default=novostroj)
    # categories = models.TextField(help_text='Новостои 1, Квартиры 2, Дома 3, Аренда 4, Вторичное 5, Зем участки 6, Застройщики 7', verbose_name= 'Категории', max_length=30, blank=True, null=True, )
    goods = models.CharField('Название', max_length=20, blank=True, null=True)
    pages = models.CharField('Район', max_length=20, blank=True, null=True, help_text='Вписать район')
    float_name = models.CharField('Адрес', max_length=20, blank=True, help_text='Адрес')
    city = models.CharField('Город', max_length=15, blank=True)
    # photo_arr = models.TextField('Фотографии', blank=True)
    price = models.CharField(max_length=30, verbose_name='Цена', blank=True)
    specifications = models.TextField('Характеристики', blank=True)
    about_the_apartment = models.CharField('Этажность в доме и этаж квартиры', max_length=255, blank=True)
    apartment_description = models.CharField('Новострой или вторичка', max_length=30, blank=True)
    quadrature = models.CharField('Квадратура', max_length=10, blank=True)
    one = '1'
    two = '2'
    three = '3'
    four = '4'

    object_type = models.CharField('Тип объекта', max_length=255, blank=True, help_text= 'вписать любое: значение Жилая Нежилая VIP Sale')
    # type_of_transaction = models.TextField('Тип сделки', blank=True)
    # mortgage = models.TextField('Ипотека', blank=True)
    plot_hundred = models.CharField(max_length=10, verbose_name='Участок соток', blank=True)
    owner_phone_number = models.CharField(max_length=15, verbose_name='Телефон собственника', blank=True)
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    studiya = '6'
    obsh = '7'
    YEAR_IN_SCHOOL_CHOICES = (
        (one, 'Одна'),
        (two, 'Две'),
        (three, 'Три'),
        (four, 'Четыре'),
        (five, 'Пять+'),
        (studiya, 'Студия'),
        (obsh, 'Общежите'),
    )
    number_of_rooms = models.CharField(max_length=2, verbose_name='Количество комнат', choices=YEAR_IN_SCHOOL_CHOICES,
                                       default=one)
    video = EmbedVideoField(blank=True, verbose_name='Видео', help_text='Обязательно должно быть какое то видео')
    image = models.ImageField(upload_to='img', verbose_name='Основное изображение', blank=True, null=True)
    gallery = models.ForeignKey(Gallery, verbose_name='Фотографии', on_delete=models.SET_NULL, null=True, blank=True)

    def publich(self):
        self.order_date = timezone.now()
        self.save()

    def __str__(self):
        return self.goods


class Users(models.Model):
    # пользователи

    class Meta:
        # managed = True
        db_table = 'users'

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    username = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=30, blank=True, null=True)
    user_pass = models.CharField(max_length=30, blank=True, null=True)


class Categories(models.Model):
    # Категории

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'categor'

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    cat_name = models.TextField('Категории', max_length=30, blank=True, null=True)
    cat_url = models.TextField('Категории', max_length=30, blank=True, null=True)


class Orders(models.Model):
    # Заказы
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        db_table = 'orders'

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    title = models.CharField('Примечание', max_length=200, blank=True)
    id_flat = models.TextField('Код Объекта', blank=True, null=True)
    order_date = models.DateTimeField('Дата заказа', auto_now_add=True)
    tel = models.TextField('Телефон', blank=True, null=True)
    email = models.TextField('Почта', blank=True, null=True)
    price = models.TextField('Цена', blank=True, null=True)
    name_flate = models.TextField('Название кв', blank=True, null=True)

    def publich(self):
        self.order_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


from django.contrib.contenttypes.fields import GenericForeignKey


class Image(models.Model):
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        db_table = 'photos'

    image = models.ImageField(upload_to="img")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    #print('mayak')
    #print(object_id, image.)


class Product(models.Model):
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
        db_table = 'product'

    name = models.CharField('Галерея', max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        db_table = 'blog'
        ordering = ('-date',)

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст новости', blank=True, null=True)
    date = models.DateTimeField('Дата заказа', auto_now_add=True)
    image = models.ImageField(upload_to='blog_img', verbose_name='Изображение', blank=True, null=True)

    def __str__(self):
        return self.title
