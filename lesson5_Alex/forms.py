from django.forms import ModelForm, Form
from . import models
from django import forms
from .models import Human

class HumanOneForm(ModelForm):
    class Meta:
        model = Human
        fields = ['name', 'surname', 'age', 'company', 'salary']