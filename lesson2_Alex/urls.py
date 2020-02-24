from django.urls import path, re_path
from . import views


urlpatterns = [
    path('hello/', views.hello),
    re_path(r'^redirect/$', views.http_redirect),
    re_path(r'^target/$', views.target),
    re_path(r'^render-html/$', views.render_html),
    re_path(r'^render-template/$', views.render_template),
]