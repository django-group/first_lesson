from django.shortcuts import render, HttpResponse
from blog import models


def art_text(request):
    return render(request, "index.html", {"Art": models.Article.objects.all()})


def asd(request, pk):
    context = {"text": models.Article.objects.get(pk=pk)}
    return render(request, "comments.html", context)