from django.shortcuts import render, redirect 
import datetime 
from .forms import neweqForm 
from .models import equipment 
from django.contrib import messages

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
    
def reservations(request): 
    return render(request, 'main/reservations.html') 

def neweq(request): 
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = neweqForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            equip = form.save(commit=False) 
            equip.save() 
            messages.success(request, "Erfolgreich gespeichert")
            
            # redirect to a new URL:
            return redirect('/lager/new')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = neweqForm()

    return render(request, 'main/neweq.html', {'form': form})
    

    
    
