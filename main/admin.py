# -*- coding: utf-8 -*-
from django.contrib import admin
from main.models import Orders, CatalogModel, Blog
from embed_video.admin import AdminVideoMixin
# Register your models here.
from django.contrib.contenttypes.admin import GenericTabularInline


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'title', 'id', 'name_flate', 'price', 'tel', 'email')
    list_filter = ('order_date', 'title')


@admin.register(CatalogModel)
class CatalogModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    print('Hellocatalog')
    # raw_id_fields = ('categories',)
    list_display = ('goods', 'id', 'categories', 'price', 'quadrature', 'number_of_rooms', 'city', 'about_the_apartment',)
    list_filter = ('goods', 'categories', 'price', 'quadrature', 'number_of_rooms', 'city')


# admin.site.register(CatalogModel, CatalogModelAdmin)

from main.models import Image, Product


class ImageInline(GenericTabularInline):
    model = Image
    list_filter = ('object_id')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    inlines = [
        ImageInline,
    ]


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'date')
    list_filter = ('id', 'title', 'date')


admin.site.register(Orders, OrdersAdmin, )
admin.site.register(Product, ProductAdmin)
admin.site.register(Blog, BlogAdmin, )
