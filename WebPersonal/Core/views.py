from django.shortcuts import render, HttpResponse


#definiendo HOME
def home(request):
    return render(request, 'Core/home.html')


#definiendo ABOUT
def about(request):
    return render(request ,'Core/about.html')


#definiendo CONTACT


def contact(request):
    return render(request , 'Core/contact.html')