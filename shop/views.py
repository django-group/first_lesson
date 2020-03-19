from django.shortcuts import render, HttpResponse
from shop import models


def foo(requests):
    context = {"admin": "http://127.0.0.1:8000/admin"}
    prod = models.Product.getall()
    print(type(prod))
    return render(requests, 'shop/index.html', context, prod)
