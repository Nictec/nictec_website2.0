from django.shortcuts import render, redirect 
from page.models import news 
from .forms import newseditForm 
from django.contrib import messages 
from django.views.generic import ListView 
from django.views.generic import UpdateView 
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse

# Create your views here. 

def index(request):  
    return render(request, 'backend/index.html')
    
class newsedit(ListView):  
    model = news
    template_name = 'backend/newsedit.html' 
    
class newsupdate(UpdateView): 
    model = news 
    template_name = 'backend/newsupdate.html' 
    fields =['title', 'text'] 
    
    def get_success_url(self):
        return reverse('news')
   
class newsdelete(DeleteView): 
    model = news 
    template_name = 'backend/newsdelete.html' 
    def get_success_url(self):
        return reverse('news')

def useredit(request): 
    return render(request, 'backend/useredit.html') 

def useradd(request): 
    return render(request, 'backend/newuser.html') 

def newsadd(request):  
    if request.method == 'POST': 
        form = newseditForm(request.POST or None) 
        if form.is_valid(): 
            news = form.save(commit=False) 
            news.save() 
            messages.success(request, "Erfolgreich gespeichert") 
            
            return redirect('/admin/news_add') 
        
    else: 
        form = newseditForm() 
    return render(request, 'backend/newnews.html', {'form': form})