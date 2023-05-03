# created 2023-04-22
# updated 2023-04-29 : new view for listing the documents available for
#   download (document_list and download_file)
from django.urls import path


from . import views


app_name = "zach_test"


urlpatterns = [
   path("", views.model_form_upload, name="upload"),
   path("metadata/", views.document_metadata, name="metadata"),
   path("doc_list/", views.document_list, name="download"),
   path("download_file/<int:file_id>/", views.download_file, name='download_file'),
]

