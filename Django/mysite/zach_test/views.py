# created 2023-04-22
# updated 2023-04-23 : convert uploaded files to json and save them in
#   the DB
# updated 2023-04-29 : create view for download page, list all
#   available files for downloand
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse
from .models import Document, Task
from .forms import DocumentForm, TaskForm, MetaDataForm

def model_form_upload(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        file_form = DocumentForm(request.POST, request.FILES)
        files_list = request.FILES.getlist('document') # this is the field name in the model
        files_list2 = request.FILES.getlist('document2')
        print(file_form.is_valid())
        if form.is_valid() and file_form.is_valid(): #form.is_valid(): and file_form.is_valid()
            # set commit to false when calling save returns an object
            # of the model that the modelForm is using, and does not
            # save it to the DB
            task_instance = form.save()
            for f in files_list:
                doc_instance = Document(document=f, task=task_instance)
                doc_instance.save()
                doc_instance.to_json() # convert the file to json
                doc_instance.save() # save the Document model again
            for f in files_list2:
                doc_instance = Document(document=f, task=task_instance)
                doc_instance.save()
                doc_instance.to_json() # convert the file to json
                doc_instance.save() # save the Document model again



            return redirect('metadata/')
    else:
        form = TaskForm()
        file_form = DocumentForm()
    return render(request, 'zach_test/upload.html', {
        'form': form,
        'file_form': file_form,
    })

def get_file_metadata(request, file_id):
    return HttpResponse("test (at file %s)." % file_id)



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

def document_metadata(request):
    task_obj = Task.objects.all()[len(Task.objects.all())-1]
    """documents = Document.objects.get(task=task_obj)"""
    documents = Document.objects.all()
    form = MetaDataForm(request.POST)
    return render(request, 'metadata.html',  {'documents': documents, 'task_obj': task_obj})

