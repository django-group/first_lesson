from django import forms


class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=100, help_text='Write what you want to find')
