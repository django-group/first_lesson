from django.urls import path, include
from shop import views

urlpatterns = [
    path('', views.foo),
    path('<slug:slug>/', views.Adress.as_view(), name='adress')
]