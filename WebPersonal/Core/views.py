from django.shortcuts import render, HttpResponse

#definiendo HOME
def home(request):
    return HttpResponse('<h1> Mi web personal </h1>')
