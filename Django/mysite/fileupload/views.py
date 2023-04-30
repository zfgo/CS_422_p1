from django.shortcuts import render
from .forms import FileUploadForm

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # handle the valid file
            pass
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})
