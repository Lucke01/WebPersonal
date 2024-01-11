from django.db import models

# Create your models here.

class Project(models.Model):
    titulo = models.CharField(max_length = 100)
    descripcion = models.TextField()
    creado = models.DateTimeField(auto_now_add = True) 
    actualizado = models.DateTimeField(auto_now=True)
    
    