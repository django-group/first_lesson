from django.forms import ModelForm
from djstore import models


class CommentForm(ModelForm):
    class Meta:
        model = models.Review
        fields = ['text', 'rating']