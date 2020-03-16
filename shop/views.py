from django.shortcuts import render, HttpResponse


def foo(requests):
    return HttpResponse('<br><br><p><a href="http://127.0.0.1:8000/admin">Админка</a></p>')
