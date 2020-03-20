from django.shortcuts import render, HttpResponse, Http404, redirect
from djstore import models
from djstore import forms
from django.views import generic
from django.urls import reverse
from djstore import filters
import json
import random

# Create your views here.


class ProductList(generic.ListView):
    model = models.Product
    filter = filters.ProductFilter
    template_name = 'djstore/home.html'
    form = forms.SearchForm
    #model_cat = models.Categorie

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = self.filter(self.request.GET, queryset=self.model.objects.all())
        context['object_list'] = object_list.qs
        context['filter'] = self.filter
        context['form'] = self.form
        #context['model_cat'] = self.model_cat
        return context


def add_to_bucket(request, slug):
    session_key = request.session.get('bucket', [])
    if not session_key:
        session_key = str(random.randint(1, 10000))
        request.session['bucket'] = session_key

    product = models.Product.objects.get(slug=slug)
    bucket, _ = models.Bucket.objects.get_or_create(session_key=session_key)
    bucket.save()
    bucket.product.add(product)
    response = redirect(reverse('product_detail_url', args=[slug]))
    return response


def bucket_view(request):
    session_key = request.session.get('bucket', '')
    bucket = models.Bucket.objects.filter(session_key=session_key)
    if bucket:
        products = bucket[0].product.all()
    else:
        products = None
    context = {
        'bucket': products
    }
    return render(request, 'djstore/bucket.html', context)


class SearchList(generic.ListView):
    form = forms.SearchForm
    model = models.Product
    template_name = 'djstore/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        search_data = self.request.GET.get('search_field')
        search_data = models.Product.objects.filter(name__contains=search_data)
        if not search_data:
            raise Http404
        context['object_list'] = search_data
        return context


class ProductDetail(generic.DetailView):
    models = models.Product
    template_name = 'djstore/product_detail.html'
    context_object_name = 'product'
    comment_form = forms.CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = self.comment_form
        return context

    def get_queryset(self):
        product = models.Product.objects.filter(slug=self.kwargs.get('slug'))
        return product

    def post(self, request, *args, **kwargs):
        form = self.comment_form(request.POST)
        if form.is_valid():
            obj = self.get_object()
            form.instance.product = obj
            form.save()
            return redirect(reverse('product_detail_url', args=[obj.slug]))