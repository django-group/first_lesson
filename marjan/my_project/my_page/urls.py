from django.urls import path, include
from my_page import views

urlpatterns = [
    path('my_page/', views.page1),
]
