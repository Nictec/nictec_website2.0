from django.conf.urls import url, include
from django.contrib import admin 
from . import views 
from storage.views import storage, storageupdate, storagedelete, assignments, eqlist

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^equipment/$', storage.as_view(), name='storage'), 
    url(r'^update_eq(?P<pk>\d+)/$', storageupdate.as_view(), name="storageupdate"), 
     url(r'^deleteeq/(?P<pk>\d+)/$', storagedelete.as_view(), name='storagedelete'),
    url(r'^clients/', views.clients, name='clients'), 
    url(r'events/', assignments.as_view(), name='assignments'), 
    url(r'^bills/', views.bills, name='bills'), 
    url(r'^reservations/', views.reservations, name='reservations'), 
    url(r'^neweq/', views.neweq, name='neweq'), 
    url(r'^newevent/$', views.new_assignment, name="newevent"), 
    url(r'^chose/$', eqlist.as_view(), name="eqlist"), 
    url(r'^eqadd/$', views.eqadd, name='eqadd')
    
]

