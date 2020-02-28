from django.shortcuts import render, HttpResponse
from . import forms
from . import models
from django.views import generic

# Create your views here.


def form(request):
    form_for_human = forms.HumanOneForm(request.POST)
    if request.method == "POST":
        if form_for_human.is_valid():
            data = form_for_human.cleaned_data
            form_for_human.save()
            return HttpResponse("Seccess!")

    context = {
        'form_for_human': form_for_human
    }
    return render(request, 'form.html', context)