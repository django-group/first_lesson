from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from blog import models


def art_text(request):
    return render(request, "index.html", {"Art": models.Article.objects.all()})


def comments(request, pk):
    context = models.Article.objects.get()
    return render(request, "comment.html", context)