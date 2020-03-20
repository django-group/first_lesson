from django import forms
from shop import models


class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Reviews
        fields = ['text']

