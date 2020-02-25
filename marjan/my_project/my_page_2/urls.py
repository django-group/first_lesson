from django.urls import path, include
from my_page_2 import views

urlpatterns = [
    path('my_page_2/', views.first_page),
]
