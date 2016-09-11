from django.contrib import admin 
from .models import equipment, client, Assignment 

# Register your models here.
admin.site.register(equipment) 
admin.site.register(client) 
admin.site.register(Assignment)