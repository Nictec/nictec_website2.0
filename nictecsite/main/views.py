from django.shortcuts import render 
import datetime

# Create your views here. 
def index(request): 
     return render(request, 'main/login.html') 
    
def dashboard(request):  
    now = str(datetime.date.today().strftime("%A %d.%m.%Y"))
    return render(request,'main/index.html', {'date':now})


def storage(request): 
     return render(request, 'main/storage.html') 
    
    
    
def clients(request): 
     return render(request, 'main/clients.html') 
    
    
def assignments(request): 
     return render(request, 'main/assignments.html')  
    
    
def bills(request): 
     return render(request, 'main/bills.html') 
    
    
