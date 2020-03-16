from django.shortcuts import render, HttpResponse, Http404, redirect
from djstore import models
from djstore import forms
from django.views import generic
from django.urls import reverse

# Create your views here.


class ProductList(generic.ListView):
    model = models.Product
    template_name = 'djstore/home.html'


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