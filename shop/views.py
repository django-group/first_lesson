from django.shortcuts import render, HttpResponse


def foo(requests):
    return render(requests, 'shop/index.html')
