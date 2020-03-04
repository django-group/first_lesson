from django.urls import path
from lesson7_Alex import views

urlpatterns = [
    path('', views.my_auth),
    path('my_login/', views.my_login)
]