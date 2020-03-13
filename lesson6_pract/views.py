from django.shortcuts import render, HttpResponse, Http404, redirect
from lesson6_pract import models
from lesson6_pract import forms
from django.views import generic
from django.urls import reverse

# Create your views here.


class BooksList(generic.ListView):
    model = models.Article
    template_name = "lesson6_pract/home.html"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class BooksDetail(generic.DetailView):
    models = models.Article
    template_name = "lesson6_pract/article.html"
    context_object_name = "data"
    comment_form = forms.CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = self.comment_form
        return context

    def get_queryset(self):
        product = models.Article.objects.filter(pk=self.kwargs.get("pk"))
        return product

    def post(self, request, *args, **kwargs):
        form = self.comment_form(request.POST)
        if form.is_valid():
            obj = self.get_object()
            form.instance.article = obj
            form.save()
            return redirect(reverse('one_page', args=[obj.id]))




# def main(request):
#     try:
#         data = models.Article.objects.all()
#     except models.Article.DoesNotExist:
#         raise Http404("Article does not exist")
#     print(data)
#     return render(request, "lesson6_pract/home.html", {"data": data})

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
