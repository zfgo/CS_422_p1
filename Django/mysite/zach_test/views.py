# created 2023-04-22
# updated 2023-04-23 : convert uploaded files to json and save them in
#   the DB
# updated 2023-04-29 : create view for download page, list all
#   available files for downloand
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse
from .models import Document, Task
from .forms import DocumentForm, TaskForm, MetaDataForm, DocumentForm2
import zipfile, os
from django import template
from django.forms.models import modelformset_factory
register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def model_form_upload(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        file_form = DocumentForm((request.POST, request.FILES) or None)
        files_list = request.FILES.getlist('document') # this is the field name in the model
        files_list2 = request.FILES.getlist('document2')
        print(file_form.is_valid())
        if form.is_valid(): #form.is_valid(): and file_form.is_valid()
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
                doc_instance.file_name = doc_instance.document.name.split('/')[-1]
                doc_instance.save()
                print(doc_instance.document.name.split('/')[-1])
            for f in files_list2:
                doc_instance = Document(document=f, task=task_instance)
                doc_instance.if_test = False
                doc_instance.save()
                doc_instance.to_json() # convert the file to json
                doc_instance.save() # save the Document model again
                doc_instance.file_name = doc_instance.document.name.split('/')[-1]
                doc_instance.save()

            return redirect('metadata/')
        else:
            print(file_form.errors.as_data())
    else:
        form = TaskForm()
        file_form = DocumentForm()
    return render(request, 'zach_test/upload.html', {
        'form': form,
        'file_form': file_form,
    })

def model_form_upload2(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        file_form = DocumentForm2((request.POST, request.FILES) or None)
        files_list = request.FILES.getlist('document') # this is the field name in the model
        files_list2 = request.FILES.getlist('document2')
        print(file_form.is_valid())
        if form.is_valid(): #form.is_valid(): and file_form.is_valid()
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
                doc_instance.file_name = doc_instance.document.name.split('/')[-1]
                doc_instance.save()
                print(doc_instance.document.name.split('/')[-1])

            return redirect('metadata/')
        else:
            print(file_form.errors.as_data())
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
    if request.method == 'POST':
        name = request.POST.get('button_name')
        print("this is name", name)
        #the_task = Task.objects.filter(id=name)
        form = DocumentForm2(request.POST, request.FILES)
        files_list = request.FILES.getlist('document')
        file = files_list[0]
        #doc_instance = Document(document=file, task=the_task)

        if form.is_valid():
            doc_instance = form.save()
        return redirect("/home/")
    else:
        task = Task.objects.all()
        form = DocumentForm2()
        return render(request, 'download.html', {'documents' : task, 'form': form})

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
        print("post")
        task_obj = Task.objects.last()
        """documents = Document.objects.get(task=task_obj)"""
        qs = Document.objects.filter(task=task_obj)
        document_form_set = modelformset_factory(Document, form=MetaDataForm, extra=0)
        formset = document_form_set(request.POST or None, queryset=qs)
        print("before check")
        if formset.is_valid():
        # print("valid!")
            formset.save()

        return redirect("/home/")
    else:
        print("not post")
        task_obj = Task.objects.last()
        qs = Document.objects.filter(task=task_obj)
        document_form_set = modelformset_factory(Document, form=MetaDataForm, extra=0)
        formset = document_form_set(request.POST or None, queryset=qs) #cat
        qs_and_form = zip(qs,formset)
        return render(request, 'metadata.html',  {'task_obj': task_obj, "formset" : formset, 'qs': qs, 'qs_and_form': qs_and_form})

def home(request):
    return render(request, 'home.html')
def display_data(request):
    return render(request, 'data.html')
