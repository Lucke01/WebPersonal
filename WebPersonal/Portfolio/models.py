from django.db import models

# Create your models here.

class Project(models.Model):
    titulo = models.CharField(max_length = 100)
    descripcion = models.TextField()
    creado = models.DateTimeField(auto_now_add = True) 
    actualizado = models.DateTimeField(auto_now=True)
    
    #creando subclase para dar mas info
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        #como ordenar
        ordering = ["-creado"]
        #nos devuelve una cadena para poder ver 
    def __str__(self):
        return self.titulo 
        