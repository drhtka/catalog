# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View



def index(request):
    return render(request, 'main/index.html')
