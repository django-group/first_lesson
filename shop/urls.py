from django.urls import path, include
from shop import views

urlpatterns = [
    path('', views.products_list),
    path('<slug:slug>/', views.Adress.as_view(), name='adress'),
]
