from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def base(request):
    return render(request, 'base.html', {})


def home(request):
    return redirect('/lesson3/base/')


def my_game(request, number):
    context = {"numbers": number}
    return render(request, 'my_game.html', context)
