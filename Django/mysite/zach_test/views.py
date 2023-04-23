# created 2023-04-22
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
            doc_model.save()
            doc_model.to_json()
            doc_model.save()

            return redirect('/polls/')
    else:
        form = DocumentForm()
    return render(request, 'zach_test/upload.html', {
        'form': form
    })


"""
document = form.model

"""
