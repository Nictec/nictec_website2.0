from django.conf.urls import url, include
from django.contrib import admin 
from page import views 



urlpatterns = [
   url(r'^$', views.index, name= 'home'),
   url(r'^lichtpakete/', views.light, name= 'licht'), 
   url(r'^beschallungspakete/', views.audio, name= 'ton'), 
   url(r'^Kontakt/', views.contact, name= 'kontakt'), 
   url(r'^technik/', views.tec, name= 'technik'),
   url(r'^ueber uns/', views.ueber,  name= 'ueber'),
]
