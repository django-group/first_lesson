from django.shortcuts import render, Http404

# Create your views here.

from .models import Author

def authtors(request):
    try:
        authors = Author.objects.all()
    except Author.DoesNotExist:
        raise Http404("Author does not exist")
    return render(request, 'authors.html', {"authors": authors})