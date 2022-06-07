from email.policy import default
from django import forms

class Books_form(forms.Form):
    ISBN = forms.IntegerField()
    title = forms.CharField(max_length = 100)
    synopsis = forms.CharField(max_length=300, required = False)
    publication_date = forms.DateField(required=False)
    edition = forms.IntegerField(required = False)
    price = forms.FloatField(required=False)
    # cover = forms.ImageField(required = False)
    active = forms.BooleanField(required = False, initial = True)

class Authors_form(forms.Form):
    name = forms.CharField(max_length = 50)
    middle_name = forms.CharField(max_length = 10, required=False)
    surname = forms.CharField(max_length = 100)
    nickname = forms.CharField(max_length = 25, required=False)
    day_birth = forms.DateField(required=False)
    id = forms.IntegerField()
    active = forms.BooleanField(required = False, initial = True)

class Editorials_form(forms.Form):
    name = forms.CharField(max_length = 50)
    founder = forms.CharField(max_length = 50, required=False)
    foundation_date = forms.DateField(required=False)
    country = forms.CharField(max_length = 50, required=False)
    main_organization = forms.CharField(max_length = 50, required=False)
    id = forms.IntegerField()    
    active = forms.BooleanField(required = False, initial = True)
    
class Genres_Form(forms.Form):
    name = forms.CharField(max_length = 50)
    description = forms.CharField(max_length = 100, required = False)
    id = forms.IntegerField()   
    active = forms.BooleanField(required = False, initial = True)
