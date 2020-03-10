from django.forms import ModelForm
from lesson6_pract.models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text']