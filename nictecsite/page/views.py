from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import news


# Create your views here. 
def index(request):  
    news1 = news.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if news1:
        return render(request, 'page/index.html', {'news':news1}) 
    else:
        print('error')
        return render(request, 'page/licht.html')

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

def logout_view(request): 
    auth.logout(request) 
    return HttpResponseRedirect("intern/loggedout/")

@login_required
def loggedin(request): 
    return render(request, 'page/loggedin.html')  

def loggedout(request): 
    return render(request, 'page/loggedout.html')
       
    
        
   
        
    