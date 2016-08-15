from django import forms 
from page.models import news  


class newseditForm(forms.ModelForm): 
    
    title = forms.CharField(label="Titel") 
    text = forms.TextInput(attrs={'class': "form-control"}),

    
    class Meta: 
        model = news 
        fields =['title', 'text']