from django.db import models

# Create your models here.
class padre(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    parentesco = models.CharField(max_length=40)    

class madre(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    parentesco = models.CharField(max_length=40)    

class hermano(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    parentesco = models.CharField(max_length=40)    



