# -*- coding: utf-8 -*-
import hashlib

from django.http import HttpResponse

from main.models import CatalogModel, Users
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View


class IndexViews(View):
    #Главная
    def get(self, request):

        print('index')
        print('index')
        return render(request, 'main/index.html')


class UsersSiteView(View):
    # registration users with site

    def post(self, request):
        # hash

        # mystring = input('Enter String to hash: ')
        # hash_object = hashlib.md5(mystring.encode())
        # print(hash_object.hexdigest())

        role_id = request.POST.get('role')
        print(role_id)
        site_users = request.POST.get('username')
        print(site_users)
        site_email = request.POST.get('user_email')

        hashed_password = hashlib.md5(request.POST.get('user_pass').encode())
        final_ph = hashed_password.hexdigest()
        seve_site = Users(username=site_users, user_email=site_email, user_pass=final_ph,
                          role=role_id)  # заносим в базу

        seve_site.save()
        return render(request, 'main/user.html')


class LogginView(View):
    # authorization loggin
    # template_name = 'main/outh.html'
    def post(self, request):
        hashed_password = hashlib.md5(request.POST.get('pass').encode())
        final_ph = hashed_password.hexdigest()
        find_user = Users.objects.filter(user_email=request.POST.get('loggin'),
                                         user_pass=final_ph).values('user_email')
        # request.session['my_list'] = []
        if len(find_user) > 0:
            # request.session.get('find_us')
            request.session['my_list'] = request.POST.get('loggin')  # записали емаил пользователя в сессию
            return redirect('/lk/')
        else:
            return HttpResponse('Данные не верны <a href="http://127.0.0.1:8000/loggin/">Вернуться назад</a>')

        # return render(request, 'main/outh.html')
        return render(request, 'main/outh.html')
class RealtyViews(View):
    #Квартиры
    def get(self, request):
        return render(request, 'main/realty.html')

class HomesViews(View):
    #Дома
    def get(self, request):
        return render(request, 'main/homes.html')

class LandViews(View):
    #Земельные участки
    def get(self, request):
        return render(request, 'main/land.html')

class NovostrojViews(View):
    # Новостройки
    def get(self, request):
        return render(request, 'main/novostroi.html')

class PropertyViews(View):
    #Застройщики
    def get(self, request):
        return render(request, 'main/property_develop.html')

class RentViews(View):
    #Аренда
    def get(self, request):
        return render(request, 'main/rent.html')

class FlatViews(View):
    # Квартира детальнее
    def get(self, request):
        return render(request, 'main/flat.html')

class SecondViews(View):
    #Вторичное
    def get(self, request):
        all_kvartirs = CatalogModel.objects.filter(categories=1).values_list('id',
                                                                             'goods',
                                                                             'pages',
                                                                             'float_name',
                                                                             'photos',
                                                                             'photo_arr',)

        return render(request, 'main/secondary.html', {'all_kvartirs': all_kvartirs})

