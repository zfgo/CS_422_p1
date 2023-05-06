# created 2023-04-22
from django import forms
from .models import Document, Task


# front end document form class
class TaskForm(forms.ModelForm):
    """Form to grab all data associated with the task form object"""
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for key, field in self.fields.items(): 
           field.label = ""         
    class Meta:
        model = Task 
        fields = ['task_desc','period', 'n_forecasts',] #fields of Task to display. 
        #widgits help style the form fields. 
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

class DocumentForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for key, field in self.fields.items():
           field.label = ""               
    class Meta:
        model = Document
        fields = ('document',) # 'document2')
        widgets = {
            'document': forms.ClearableFileInput(attrs={'multiple': False, 'id':'mle', 'name':'test[]',}),
        }

#'id':'mle', 'name':'mle[]' 'id':'choose', 'name':'test[]', 'class': 'hidden but'

class MetaDataForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['fname','fdescription', 'funits', 'fvector_size', 'flength', 'fsampling_period'] # ('task_desc', 'period', 'n_forecasts', )
        widgets = {
            'fname': forms.TextInput(attrs={'class':'form__input',
				   'id':'name', 'placeholder':'Name of time series', 'autofocus':True, 'required':True,}),
            'fdescription': forms.TextInput(attrs={'class':'form__input',
				   'id':'desc', 'placeholder':'Time series description/keywords', 'required':True}),
            'funits': forms.TextInput(attrs={'class':'form__input',
				   'id':'units', 'placeholder':'Units','required':True}),
            'fvector_size': forms.TextInput(attrs={'class':'form__input',
				   'id':'size', 'placeholder':'Vector size', 'type':"number",'required':True}),
            'flength': forms.TextInput(attrs={'class':'form__input',
				   'id':'length', 'placeholder':'Length', 'type':"number",'required':True}),
            'fsampling_period': forms.TextInput(attrs={'class':'form__input',
				   'id':'period', 'placeholder':'Sampling period', 'type':"number", 'step':'any','required':True}),
        }



