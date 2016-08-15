from django.conf.urls import url, include 
from django.contrib import admin 
from . import views 
from backend.views import newsedit, newsupdate, newsdelete

urlpatterns = [ 
    url(r'^$', views.index, name='index'), 
    url(r'^users/$', views.useredit, name='users'), 
    url(r'^news/$', newsedit.as_view(), name='news'), 
    url(r'^update_news(?P<pk>\d+)/$', newsupdate.as_view(), name='newsupdate'), 
    url(r'^delete/(?P<pk>\d+)/$', newsdelete.as_view(), name='newsdelete'),
    url(r'^user_add/$', views.useradd, name="user_add"), 
    url(r'^news_add/$', views.newsadd, name="news_add"),

] 

