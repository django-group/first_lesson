from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def my_auth(request):
    return render(request, 'if_auth.html')


@login_required
def my_login(request):
    return HttpResponse('You are login')