from django.urls import path, re_path, include
from djstore import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    path('main/', views.ProductList.as_view(), name='main'),
    path('product/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail_url'),
    path('search/', views.SearchList.as_view(), name='search_url'),
    path('bucket/', views.bucket_view, name='bucket_url'),
    path('bucket/<slug:slug>/', views.add_to_bucket, name='add_to_bucket_url'),
]