# created 2023-04-22
# updated 2023-04-23 : convert uploaded files to json and save them in 
#   the DB.
# updated 2023-04-29 : create view for download page, list all 
#   available files for download.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse
from .models import Document
from .forms import DocumentForm



def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # set commit to false when calling save returns an object 
            # of the model that the modelForm is using, and does not
            # save it to the DB 
            doc_model = form.save(commit=False)

            # now save the document model to the DB
            doc_model.save() # this makes the file's path to be accurate
            doc_model.to_json() # convert the file to json
            doc_model.save() # save the Document model again

            # TODO: this line should be in a different app where the 
            # participant downloads the data
            doc_model.json_to_csv()

            return redirect('doc_list/')

    else:
        form = DocumentForm()
    return render(request, 'zach_test/upload.html', {
        'form': form
    })


def document_list(request):
    documents = Document.objects.all()
    return render(request, 'download.html', {'documents' : documents})


def download_file(request, file_id):
    file = get_object_or_404(Document, pk=file_id)

    # Assuming the file field is named 'file_field' in your model
    file_path = file.document.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=' + file.document.name
        return response
