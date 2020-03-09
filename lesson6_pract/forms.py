from django.forms import ModelForm
from lesson6_pract.models import Comments


class CommentForm(ModelForm):
    class Meta:
        models = Comments
        fields = ['text']