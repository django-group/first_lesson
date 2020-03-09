from django.urls import path, include, re_path
from lesson6_pract import views

urlpatterns = [
    path("", views.main),
    path("main/", views.main),
    path("<int:id>/", views.some, name='one_page'),
    path("add_comment/", views.add_comment, name="add_comment"),
]