from django.shortcuts import render

# Create your views here. 
def menue(request):
    return render(request, 'backend/index.html')
