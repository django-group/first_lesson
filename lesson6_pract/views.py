from django.shortcuts import render, HttpResponse, Http404
from lesson6_pract import models
from lesson6_pract import forms
from django.views import generic

# Create your views here.


def main(request):
    try:
        data = models.Article.objects.all()
    except models.Article.DoesNotExist:
        raise Http404("Article does not exist")
    print(data)
    return render(request, "home.html", {"data": data})



class ArticleView(generic.TemplateView):
    data = models.Article.objects.get(id=id)
    comments = models.Comments.objects.filter(article=id)

    def get(self, request):
        context = {
            "data": self.data,
            "comments": self.comments
        }
        return render(request, "article.html", context)

    def post(self, request):
        form_comment = forms.CommentForm(request.POST)
        context = {
            "data": self.data,
            "comments": self.comments,
            "form_cooment": form_comment
        }
        if form_comment.is_valid():
            res = form_comment.cleaned_data
            return render(request, 'article.html', context)
        else:
            return render(request, 'article.html', context)


# def some(request,id):
#     try:
#         data = models.Article.objects.get(id=id)
#         comments = models.Comments.objects.filter(article=id)
#
#     except models.Article.DoesNotExist:
#         raise Http404( "Article does not exist")
#
#     context = {
#         "data": data,
#         "comments": comments,
#     }
#     return render(request, "article.html", context)
#
#
# def add_comment(request):
#     form_comment = forms.CommentForm(request.POST)
#     if request.method == "POST":
#         form_comment.save()
#
#     context = {
#         "form_comment": form_comment
#     }
#     return render(request, 'article.html', context)
