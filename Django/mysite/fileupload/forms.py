from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os
from .constants import ALLOWED_EXTENSIONS

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # get the file extension
    if not ext.lower() in ALLOWED_EXTENSIONS:
        raise ValidationError(_('Invalid file type. Only CSV and JSON files are allowed.'))

class FileUploadForm(forms.Form):
    file = forms.FileField(validators=[validate_file_extension])
