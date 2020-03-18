from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, Http404

from main_page import forms
from main_page import models


def all_products(request):
    products = models.Product.objects.all()
    return render(request, 'main_page/all_products.html', {'products': products})


def product(request, slug):
    single_product = models.Product.objects.get(slug=slug)
    recent_reviews = models.Review.objects.filter(product__slug=slug)
    if single_product.count_reviews() > 2:
        recent_reviews = recent_reviews[single_product.count_reviews()-2:single_product.count_reviews()]
    print(recent_reviews)
    return render(
        request,
        'main_page/product.html',
        {'single_product': single_product, 'recent_reviews': recent_reviews}
    )


def all_reviews(request, slug):
    single_product = models.Product.objects.get(slug=slug)
    reviews = models.Review.objects.filter(product__slug=slug)
    return render(
        request,
        'main_page/all_reviews.html',
        {'single_product': single_product, 'reviews': reviews}
    )

# def filter_for_all_products(request):
#     pass


class SearchView(generic.ListView):
    form = forms.SearchForm
    model = models.Product
    template_name = 'main_page/all_products.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        search_value = self.request.GET.get('search_field')
        search_value = models.Product.objects.filter(title__contains=search_value)
        if not search_value:
            raise Http404
        context['object_list'] = search_value
        return context
