"""
URL configuration for WebPersonal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Core import views
from Portfolio import views as portfolio_views
from django.conf import settings

urlpatterns = [
    path('',views.home , name ='Home'),
    path('about/',views.about, name = "About"),
    path('contact/',views.contact, name = "Contact"),
    path('portfolio/',portfolio_views.portfolio, name ="Portfolio"),
    path('admin/', admin.site.urls),
    
    
]
#separamos la app
if settings.DEBUG:
    from django.conf.urls.static import static #hola
    urlpatterns += static(settings.MEDIA_URL, 
                        document_root = settings.MEDIA_ROOT)