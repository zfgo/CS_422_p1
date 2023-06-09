# created 2023-04-23
# https://stackoverflow.com/questions/3648421/only-accept-a-certain-file-type-in-filefield-server-side
import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [
        '.csv',
        '.xlsx',
        '.json',
    ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
