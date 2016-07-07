from __future__ import unicode_literals

from django.db import models

# Create your models here.
class equipment(models.Model): 
    name = models.CharField(max_length=30) 
    storeplace = models.IntegerField() 
    labor_choices = (  
        ('L', 'Licht'), 
        ('T', 'Ton'), 
        ('R', 'rigging'),
    ) 
    labor = models.CharField(max_length=1, choices=labor_choices)  
   
    