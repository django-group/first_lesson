from django.shortcuts import render, HttpResponse, Http404
from . import models

# Create your views here.
def main(request):
    try:
        data = models.Article.objects.all()
    except models.Article.DoesNotExist:
        raise Http404("Article does not exist")
    print(data)
    return render(request, "home.html", {"article": data})

def some(request, id):
    print(id)
    try :
        data = models.Article.objects.get(id=id)
    except models.Article.DoesNotExist:
        raise Http404( "Article does not exist" )
    print(data)
    return render ( request, "article.html", {"article": data})
