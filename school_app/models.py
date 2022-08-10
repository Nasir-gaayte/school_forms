from re import I
from unicodedata import name
from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.name
    
    
class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    digry = models.PositiveSmallIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name    