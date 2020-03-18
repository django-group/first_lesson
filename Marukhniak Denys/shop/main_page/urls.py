from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main_page import views


urlpatterns = [
    path('', views.all_products),
    path('product/<slug:slug>/', views.product),
    path('product/<slug:slug>/reviews/', views.all_reviews, name='all_reviews_for_product'),
    path('search/', views.SearchView.as_view(), name='search_url'),
    # path('filter/', views.filter_for_all_products),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
