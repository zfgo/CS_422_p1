# created 2023-04-22
from django import forms
from .models import Document, Task


# front end document form class
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ['task_desc', ] # ('task_desc', 'period', 'n_forecasts', )

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',) # 'document2')
        widgets = {
            'document': forms.ClearableFileInput(attrs={'multiple': True}),
        }
