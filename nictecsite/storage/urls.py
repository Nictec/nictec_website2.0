from django.conf.urls import url, include
from django.contrib import admin 
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^equipment/', views.storage, name='storage'),  
    url(r'^clients/', views.clients, name='clients'), 
    url(r'assignments/', views.assignments, name='assignments'), 
    url(r'^bills/', views.bills, name='bills'), 
    url(r'^reservations/', views.reservations, name='reservations'), 
    url(r'^new/', views.neweq, name='neweq'),
    
]

