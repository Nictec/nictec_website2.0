from django.contrib import admin 
from .models import Equipment, client, Assignment 

# Register your models here.
admin.site.register(Equipment) 
admin.site.register(client) 
admin.site.register(Assignment)