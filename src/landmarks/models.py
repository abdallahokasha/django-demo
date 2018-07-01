from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Landmark(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    country = CountryField()
    latitude = models.FloatField(default="30.044281")
    longitude = models.FloatField(default="31.340002") 
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

def __unicode__(self):
    return self.title 

def __str__(self):
    return self.title  


