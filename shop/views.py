from django.shortcuts import render, HttpResponse
from shop import models, forms
from django.views import generic


def foo(requests):
    context = {'admin': 'http://127.0.0.1:8000/admin', 'div_block': '<div class="col-lg-4 col-md-6 mb-4">',
               'products': models.Product.objects.all()}
    return render(requests, 'shop/product_list.html', context)


class Adress(generic.DetailView):
    context_object_name = 'product'
    model = models.Product
    template_name = 'shop/product_detail.html'
    comment_form = forms.CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coment_f'] = self.comment_form
        return context