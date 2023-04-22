from django.urls import path

from .import views

app_name = "zach_test"
urlpatterns = [
    path("", views.model_form_upload, name="upload"),
    path("zach_test/polls/", views.model_form_upload, name="upload2"),

]

