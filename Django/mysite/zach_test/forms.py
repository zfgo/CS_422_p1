# created 2023-04-22
from django import forms
from .models import Document, Task


# front end document form class
class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for key, field in self.fields.items(): 
           field.label = ""         
    class Meta:
        model = Task 
        fields = ['task_desc','period', 'n_forecasts',] # ('task_desc', 'period', 'n_forecasts', )
        widgets = {
            'task_desc': forms.TextInput(attrs={'class':'form__input',
				   'id':'t1', 'placeholder':'Task description', 'autofocus':True}),
                     'period': forms.TextInput(attrs={'class':'form__input',
				   'id':'t2', 'placeholder':'Period', 'type':'number'}),
            'n_forecasts': forms.TextInput(attrs={'class':'form__input',
				   'id':'t3', 'placeholder':'Number of forecasts', 'type':'number'}),
        }
        """
         'period': forms.TextInput(attrs={'class':'form__input',
				   'id':'form', 'placeholder':'Period'}),
            'n_forecasts': forms.TextInput(attrs={'class':'form__input',
				   'id':'form', 'placeholder':'n_forecasts'}),
        """
        #TODO fields: [name/keywords,  forecasting period,  num of forecasts]

class DocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for key, field in self.fields.items():
           field.label = ""               
    class Meta:
        model = Document
        fields = ('document','document2') # 'document2')
        widgets = {
            'document': forms.ClearableFileInput(attrs={'multiple': True, 'id':'test', 'name':'test[]'}),
            'document2': forms.ClearableFileInput(attrs={'multiple': True, 'id':'training', 'name':'training[]'}),
        }

class MetaDataForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name','set_description', 'vector_size',] # ('task_desc', 'period', 'n_forecasts', )
        widgets = {
            'name': forms.TextInput(attrs={'class':'form__input',
				   'id':'name', 'placeholder':'Name of set', 'autofocus':True}),
            'set_description': forms.TextInput(attrs={'class':'form__input',
				   'id':'desc', 'placeholder':'Set description/keywords', 'type':"number"}),
            'vector_size': forms.TextInput(attrs={'class':'form__input',
				   'id':'size', 'placeholder':'Vector size', 'type':"number"}),
        }

