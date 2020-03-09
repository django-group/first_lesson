"""First_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson1/', include('lets_go.urls')),
    path('lesson2/', include('lesson2_Alex.urls')),
    path('lesson3/', include('lesson3_Alex.urls')),
    path('lesson4/', include('lesson4_Alex.urls')),
    path('lesson5/', include('lesson5_Alex.urls')),
    path('lesson6/', include('lesson6_pract.urls')),
    path('lesson7/', include('lesson7_Alex.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]