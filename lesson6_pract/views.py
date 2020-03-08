from django.shortcuts import render, HttpResponse, Http404
from . import models

# Create your views here.


def main(request):
    try:
        data = models.Article.objects.all()
    except models.Article.DoesNotExist:
        raise Http404("Article does not exist")
    print(data)
    return render(request, "home.html", {"data": data})


def some(request,id):
    try:
        data = models.Article.objects.get(id=id)
        comments = models.Comments.objects.filter(article=id)

    except models.Article.DoesNotExist:
        raise Http404( "Article does not exist")

    context = {
        "data": data,
        "comments": comments,
    }
    return render(request, "article.html", context)
