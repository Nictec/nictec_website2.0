from django import forms 
from .models import Equipment, Assignment 


 
class neweqForm(forms.ModelForm): 
   
    
    name = forms.CharField(label="Name") 
    fabricator = forms.CharField(label="Hersteller") 
    storeplace = forms.IntegerField(label="Regal") 
     
    
    class Meta: 
        model = Equipment 
        fields = "__all__" 
 


class neweventForm(forms.ModelForm): 
    
    class Meta: 
        model = Assignment 
        fields =['name', 'city', 'street', 'date', 'GuestNumber', 'description'] 

    
    
    

       