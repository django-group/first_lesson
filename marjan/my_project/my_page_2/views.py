from django.shortcuts import render, HttpResponse
from django.template import loader


# Create your views here.


def first_page(requests):
    return render(requests, 'my_page_2/index.html')


def content_art(requests):
    template = loader.get_template('my_page_2/index.html')
    context = {
        "logo": "https://codexe.pro/static/img/technologies/django-python.png",
        "h1": "Lorem Ipsum",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    }
    return HttpResponse(template.render(context, requests))

