# -*- coding: utf-8 -*-
from django import forms 
from .models import Equipment, Assignment  
from storage.choices import *


 
class neweqForm(forms.ModelForm): 
   
    
    name = forms.CharField(label="Name") 
    fabricator = forms.CharField(label="Hersteller") 
    storeplace = forms.IntegerField(label="Regal") 
    labour = forms.ChoiceField(label = "Gewerk", choices=labor_choices)
    
     
    
    class Meta: 
        model = Equipment 
        fields =['name', 'fabricator', 'storeplace', 'labour'] 
 
 


class neweventForm(forms.ModelForm): 
    
    name = forms.CharField(label="Name") 
    Type = forms.ChoiceField(label="Art", choices=TYPE_CHOICES ) 
    city = forms.CharField(label="Ort") 
    street = forms.CharField(label="Straße") 
    date = forms.DateField(label="Datum") 
    GuestNumber = forms.IntegerField(label="Gästeanzahl")
    description = forms.CharField(label="Beschreibung", widget=forms.Textarea)
    
    class Meta: 
        model = Assignment 
        fields =['name', 'Type', 'city', 'street', 'date', 'GuestNumber', 'description'] 

    
class FilterForm(forms.Form): 
    
    filter = forms.ChoiceField(choices=labor_choices)
    

    