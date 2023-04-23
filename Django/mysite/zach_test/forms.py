# created 2023-04-22
from django import forms
from .models import Document


# front end document form class
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')

