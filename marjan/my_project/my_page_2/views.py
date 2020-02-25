from django.shortcuts import render, HttpResponse

# Create your views here.


def first_page(reqwests):
    return render(reqwests, 'my_page_2/index.html')
