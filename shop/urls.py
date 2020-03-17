from django.urls import path, include
from shop import views

urlpatterns = [
    path('', views.foo),
]