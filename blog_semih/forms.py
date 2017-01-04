from django import forms
from .models import Blogx

class BlogxForm(forms.ModelForm):

    class Meta:
        model = Blogx
        fields = ["namex", "descriptionx", "tagsx"]