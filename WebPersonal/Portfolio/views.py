from django.shortcuts import render
from .models import Project

#Inyectamos los proyectos
def portfolio(request):
    projects = Project.objects.all()
    return render (request, 'Portfolio/portfolio.html',{'projects':projects})