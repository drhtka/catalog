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
from django.contrib import admin
from django.urls import path, include
from main.views import UsersSiteView, LogginView
#from main import views
from django.conf import settings
from django.conf.urls.static import static
from main.views import HomesViews, LandViews, NovostrojViews, \
    PropertyViews, RentViews, SecondViews, IndexViews, RealtyViews


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/', IndexViews.as_view(), name='index'),
    path('users', UsersSiteView.as_view(), name='users'),
    path('loggin/', LogginView.as_view(), name='loggin'),
    path('realty/', RealtyViews.as_view(), name='realty'),
    path('homee/', HomesViews.as_view(), name='homes'),
    path('land/', LandViews.as_view(), name='land'),
    path('novostroj/', NovostrojViews.as_view(), name='novostroj'),
    path('property/', PropertyViews.as_view(), name='property'),
    path('rent/', RentViews.as_view(), name='rent'),
    path('second/', SecondViews.as_view(), name='second'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
