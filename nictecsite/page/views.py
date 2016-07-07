from django.shortcuts import render

# Create your views here. 
def index(request): 
     return render(request, 'page/index.html') 

def light(request): 
    return render(request, 'page/licht.html') 

def audio(request): 
    return render(request, 'page/beschallung.html') 

def contact(request): 
    return render(request, 'page/buchung.html') 

def tec(request): 
    return render(request, 'page/technik.html') 

def ueber(request): 
    return render(request, 'page/ueber.html')