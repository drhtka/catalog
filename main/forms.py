# -*- coding: utf-8 -*-
from django import forms



class AddOrderForm(forms.Form):
    tel = forms.CharField(max_length=10, min_length=10)
    email = forms.EmailField(max_length=20)



