from django import forms 
from .models import equipment 


 
class neweqForm(forms.ModelForm): 
   
    
    name = forms.CharField(label="Name") 
    fabricator = forms.CharField(label="Hersteller") 
    storeplace = forms.IntegerField(label="Regal") 
     
    
    class Meta: 
        model = equipment 
        fields = "__all__" 
 

    
    
    

       