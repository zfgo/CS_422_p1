# created 2023-04-22
# updated 2023-04-29 : new view for listing the documents available for
#   download (document_list and download_file)
from django.urls import path


from . import views


app_name = "zach_test"


urlpatterns = [
   path("", views.home, name="upload"),
   path("upload/", views.model_form_upload, name="upload"),
   path("upload/metadata/", views.document_metadata, name="metadata"),
   path("download/", views.document_list, name="download"),
   path("download_file/<int:file_id>/", views.download_file, name='download_file'),
   path("data/", views.display_data, name="display_data")
]



