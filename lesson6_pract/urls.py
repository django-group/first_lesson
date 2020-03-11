from django.urls import path, include, re_path
from lesson6_pract import views

urlpatterns = [
    path("", views.BooksList.as_view(), name="home"),
    path("main/", views.BooksList.as_view(), name="main"),
    path("<int:id>/", views.BooksDetail.as_view(), name='one_page'),
]