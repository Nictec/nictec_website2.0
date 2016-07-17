from django.conf.urls import url, include
from django.contrib import admin 
from page import views  
from django.contrib.auth.views import login, logout



urlpatterns = [
   url(r'^$', views.index, name= 'home'),
   url(r'^lichtpakete/', views.light, name= 'licht'), 
   url(r'^beschallungspakete/', views.audio, name= 'ton'), 
   url(r'^Kontakt/', views.contact, name= 'kontakt'), 
   url(r'^technik/', views.tec, name= 'technik'),
   url(r'^ueber uns/', views.ueber,  name= 'ueber'), 
   url(r'^intern/login/$',login, name='login'),
   url(r'^loggedin/', views.loggedin, name= 'loggedin'), 
   url(r'^intern/loggedout', views.loggedout),
   url(r'intern/logout', views.logout_view, name='logout'),
]
