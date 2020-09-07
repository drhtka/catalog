# -*- coding: utf-8 -*-
"""catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
#from django.contrib import admin
#from django.conf.urls.static import static
#from catalog import settings
from django.urls import path
#from main.views import UsersSiteView, LogginView
from main.views import HomesViews, LandViews, NovostrojViews, PropertyViews, RentViews, SecondViews, IndexViews, RealtyViews, FlatViews, Flat3Views, OrderClientView, OrdersView, ChekFormFiltrView, ErrorOutView, \
    ChekErrorFiltrView, UsersSiteView, LogginView, BlogViews, BlogDetailViews, VipViews, SaleViews, cheajax #CallFromTheSiteView,
#from main import views
from django.conf import settings
#from django.conf.urls.static import static
#chek_form_filtr
from django.views.static import serve

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', IndexViews.as_view(), name='index'),
    path('users', UsersSiteView.as_view(), name='users'),
    path('loggin/', LogginView.as_view(), name='loggin'),
    path('realty/', RealtyViews.as_view(), name='realty'),
    path('homes/', HomesViews.as_view(), name='homes'),
    path('land/', LandViews.as_view(), name='land'),
    path('novostroj/', NovostrojViews.as_view(), name='novostroj'),
    path('property/', PropertyViews.as_view(), name='property'),
    path('rent/', RentViews.as_view(), name='rent'),
    path('second/', SecondViews.as_view(), name='second'),
    path('vip/', VipViews.as_view(), name='vip'),
    path('sale/', SaleViews.as_view(), name='sale'),
    path('flat/', FlatViews.as_view(), name='flat'),
    path('flat3/', Flat3Views.as_view(), name='flat3'),
    path('orders', OrdersView.as_view(), name='orders'),
    #path('call', CallFromTheSiteView.as_view(), name='call'),
    path('order_client', OrderClientView.as_view(), name='order_client'),
    path('chek_form_filtr/', ChekFormFiltrView.as_view(), name='chek_form_filtr'),
    path('call/', cheajax),
    path('error_out/', ErrorOutView.as_view(), name='error_out'),
    path('error_filter/', ChekErrorFiltrView.as_view(), name='error_filter/'),
    path('blog/', BlogViews.as_view(), name='blog'),
    path('detail/', BlogDetailViews.as_view(), name='detail'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
