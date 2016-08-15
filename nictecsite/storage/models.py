from __future__ import unicode_literals

from django.db import models

# Create your models here.
class equipment(models.Model): 
    name = models.CharField(max_length=30) 
    fabricator = models.CharField(max_length=30, default='-') 
    storeplace = models.IntegerField() 
    labor_choices = (  
        ('L', 'Licht'), 
        ('T', 'Ton'), 
        ('R', 'rigging'),
    ) 
    labor = models.CharField(max_length=1, choices=labor_choices)  
   
    def __str__(self): 
        return self.name
    
    
class client(models.Model): 
    firstname = models.CharField(max_length=30) 
    secondname = models.CharField(max_length=30) 
    email = models.EmailField() 
    post_code = models.IntegerField()
    city = models.CharField(max_length=30) 
    street= models.CharField(max_length=30)   
        
        
    def __str__(self):              
        return "%s %s" % (self.firstname, self.secondname)
        