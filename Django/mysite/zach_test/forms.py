# created 2023-04-22
from django import forms
from .models import Document, Task


# front end document form class
class TaskForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #   super().__init__(*args, **kwargs)
    #   for key, field in self.fields.items():   # FLEEBER WANTS THESE 4 LINES TO STAY!
    #       field.label = ""                    #they are currently disabled for easier debugging!!!!!
    class Meta:
        model = Task 
        fields = ['task_desc', ] # ('task_desc', 'period', 'n_forecasts', )
        widgets = {
            'task_desc': forms.TextInput(attrs={'class':'form__input',
				   'id':'desc', 'placeholder':'Task description', 'autofocus':True}),
        }
        #TODO fields: [name/keywords,  forecasting period,  num of forecasts]

class DocumentForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #   super().__init__(*args, **kwargs)
    #   for key, field in self.fields.items():   # FLEEBER WANTS THESE 4 LINES TO STAY!
    #       field.label = ""                    #they are currently disabled for easier debugging!!!!!
    class Meta:
        model = Document
        fields = ('document',) # 'document2')
        widgets = {
            'document': forms.ClearableFileInput(attrs={'multiple': True}),
        }
