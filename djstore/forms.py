from django.forms import ModelForm
from djstore import models
from django import forms


class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=100)


class CommentForm(ModelForm):
    class Meta:
        model = models.Review
        fields = ['text', 'rating']