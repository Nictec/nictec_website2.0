# -*- coding: utf-8 -*
from django.shortcuts import render, redirect, HttpResponse
import datetime 
from .forms import neweqForm, neweventForm, FilterForm 
from storage.models import Equipment, Assignment, client
from django.contrib import messages 
from django.views.generic import ListView, DetailView 
from django.views.generic import UpdateView 
from django.views.generic import DeleteView  
from django.views.generic.edit import FormMixin 
from custom_responses import AjaxTemplateMixin
from django.core.urlresolvers import reverse 
from django.db.models import Count

# Create your views here. 
def index(request): 
    

    
    return render(request, 'main/login.html') 
    
def dashboard(request):  
    now = str(datetime.date.today().strftime("%A %d.%m.%Y")) 
    today = datetime.date.today() 
    events = Assignment.objects.filter(date=today).values('date')  
    num = events.aggregate(data=Count('date')) 
    return render(request,'main/index.html', {'date':now, 'number':num, 'filter':today})


class storage(ListView): 
    model = Equipment 
    template_name= 'main/storage.html' 
    
class storageupdate(UpdateView): 
    model = Equipment 
    template_name= 'main/storageupdate.html' 
    ajax_template_name = 'main/storageupdate_inner.html'
    fields = ['name', 'fabricator', 'storeplace'] 
     
    

    
class storagedelete(AjaxTemplateMixin, DeleteView): 
      model = Equipment
      template_name = 'main/storagedelete.html' 
      ajax_template_name= 'main/storagedelete_inner.html'
      def get_success_url(self): 
            return reverse('storage')
        
    
    
    
    
def clients(request): 
     return render(request, 'main/clients.html') 
    
    
class assignments(ListView): 
    model = Assignment 
    template_name = 'main/assignments.html' 
    

        
        
    
def new_assignment(request): 
             # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = neweventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            event = form.save(commit=False) 
            event.save() 
            messages.success(request, "Erfolgreich gespeichert") 
            request.session['event_name'] = event.id
            # redirect to a new URL:
            return redirect('/lager/chose') 
    # if a GET (or any other method) we'll create a blank form
    else:
        form = neweventForm()

    return render(request, 'main/newevent.html', {'form': form}) 

    
    
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
            return redirect('/lager/equipment')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = neweqForm()

    return render(request, 'main/neweq.html', {'form': form}) 




def eqadd(request): 
    eventname = request.session['event_name']  
    eqid = request.GET.get('eq', '') 
    equipment = Equipment.objects.get(pk=eqid) 
   
    
    if equipment.quantity > 0: 
        equipment.event.add(eventname) 
        Equipment.objects.filter(pk=eqid).update(quantity=-1)
        return redirect("/lager/dashboard")
    else: 
        return redirect("/lager/chose")
    
    
    


class eqlist(ListView): 
    model=Equipment 
    template_name='main/eqlist.html' 
    
    def get_queryset(self):
        queryset = Equipment.objects.all()

        if self.request.GET.get('filter'): 
            queryset = queryset.filter(labor=self.request.GET.get('filter')) 
        return queryset
        
        
  
   
        
        
       
    
    
    
class ass_detail(DetailView): 
    model = Assignment
    template_name='main/ass_detail.html' 
    queryset = Assignment.objects.select_related() 
    
    
    
def del_session(request): 
    del request.session['event_name'] 
    return redirect('/lager/chose')
    
     
        
        
        
class userlist(ListView): 
    model=client 
    template_name='main/clients.html' 
    
def picklist(request): 
    eqid = request.GET.get('eq', '') 
    
    equipment_py = Equipment.objects.filter(event = eqid)
    return render(request, 'main/picklist.html', {'equipment': equipment_py})
        

    


    

    
    
