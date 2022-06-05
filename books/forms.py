from tkinter.tix import Form
from django import forms

class Book_form(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    country = forms.CharField(max_length=40)
    price = forms.FloatField()
    EAN = forms.CharField(max_length=13)
    active = forms.BooleanField()
