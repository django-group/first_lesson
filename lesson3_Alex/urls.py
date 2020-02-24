from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'base/$', views.base),
    re_path(r'home/$', views.home),
    re_path(r'my_game/(<number>[\d]{0,4})?/$', views.my_game)
]