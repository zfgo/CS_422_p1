# created 2023-04-22
# updated 2023-04-23 : convert uploaded files to json and save them in the DB
from django.shortcuts import render
from .models import Document
from .forms import DocumentForm
from django.shortcuts import redirect
# Create your views here.

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # set commit to false when calling save returns an object 
            # of the model that the modelForm is using, and does not
            # save it to the DB 
            doc_model = form.save(commit=False)

            # TODO: we will convert the document to a json

            # now save the document model to the DB
            doc_model.save() # this makes the file's path to be accurate
            doc_model.to_json() # convert the file to json
            doc_model.save() # save the Document model again

            doc_model.json_to_csv()

            return redirect('/polls/')

    else:
        form = DocumentForm()
    return render(request, 'zach_test/upload.html', {
        'form': form
    })


"""
document = form.model

"""
