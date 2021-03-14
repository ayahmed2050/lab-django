from django import forms
from django.core.exceptions import ValidationError
from . models import Category, movies
not_allowed_name = ["admin"]

class customForm(forms.Form):
    name = forms.CharField(max_length=233)
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        name = self.cleaned_data.get("name")
        if name in not_allowed_name:
            return ValidationError("name is not allowed")


class movieForm(forms.ModelForm):
    class Meta:
        model = movies
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
