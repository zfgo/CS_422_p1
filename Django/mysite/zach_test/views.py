# created 2023-04-22
# updated 2023-04-23 : convert uploaded files to json and save them in
#   the DB
# updated 2023-04-29 : create view for download page, list all
#   available files for downloand
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse
from .models import Document, Task
from .forms import DocumentForm, TaskForm, MetaDataForm
import zipfile, os
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

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
                doc_instance.if_test = True
                doc_instance.save()
                doc_instance.to_json() # convert the file to json
                doc_instance.save() # save the Document model again
                
            for f in files_list2:
                doc_instance = Document(document=f, task=task_instance)
                doc_instance.if_test = False
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
    task = Task.objects.all()

    return render(request, 'download.html', {'documents' : task})

def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

def download_file(request, file_id):
    file = get_object_or_404(Task, pk=file_id)
    # Assuming the file field is named 'file_field' in your model

    file_path = f"documents/{file.id}"
    zip_path = f"{file_path}.zip"
    zip_folder(folder_path=file_path, zip_path=zip_path)
    
    with open(zip_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file.id}.zip"'
    
    # Clean up the temporary zip file
    os.remove(zip_path)
    
    return response

    """
    zip_folder(folder_path=file_path, zip_path=f"{file_path}")
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/octet-stream')
        #response['Content-Disposition'] = 'attachment; filename=' + file.document.name
    return response
    """
"""
def document_metadata(request):
    if request.method == 'POST':

        task_obj = Task.objects.last()
        documents = Document.objects.get(task=task_obj)
        documents = Document.objects.all()
        form = MetaDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home/")

    else:
        documents = Document.objects.all()
        task_obj = Task.objects.all()[len(Task.objects.all())-1]
        form = MetaDataForm(request.POST)
        return render(request, 'metadata.html',  {'documents': documents, 'task_obj': task_obj, "file_form": form, })
"""

def document_metadata(request):
    if request.method == 'POST':

        task_obj = Task.objects.last()
        """documents = Document.objects.get(task=task_obj)"""
        documents = Document.objects.all()
        form_set = []
        for doc in documents:
            if doc.task == task_obj:
                form_set.append(MetaDataForm(request.POST or None, instance=doc))
        form = MetaDataForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("/home/")
    else:
        documents = Document.objects.all()
        task_obj = Task.objects.all()[len(Task.objects.all())-1]
        form = MetaDataForm(request.POST)
        return render(request, 'metadata.html',  {'documents': documents, 'task_obj': task_obj, "file_form": form,})

def home(request):
    return render(request, 'home.html')

