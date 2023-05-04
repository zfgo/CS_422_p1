# created 2023-04-22
# updated 2023-04-23 : add to_json fxn
# updated 2023-04-29 : add id to the Document model (used to get the
#   correct file during download)
from django.db import models
import csv
import json
import pandas as pd
from .validators import validate_file_extension

class Task(models.Model):
    task_desc = models.CharField(max_length=255, blank=True, null=True)
    period = models.FloatField(null=True)
    n_forecasts = models.IntegerField(null=True)
    id = models.BigAutoField(primary_key=True)

def document_upload_path(instance, filename):
    return f"documents/{instance.task.id}/{filename}"

class Document(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True) # files are associated with a TS forecasting task
    #description = models.CharField(max_length=255, blank=True)
    if_test = models.BooleanField(default=True, null=True) # True for test data, False for train data
    document = models.FileField(upload_to=document_upload_path, validators=[validate_file_extension], null=True)
    document2 = models.FileField(upload_to=document_upload_path, validators=[validate_file_extension], null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    json_data = models.JSONField(null=True)
    id = models.BigAutoField(primary_key=True)
    fname = models.CharField(max_length=255, blank=True, null=True)
    fdescription = models.CharField(max_length=255, blank=True, null=True)
    funits = models.CharField(max_length=255, blank=True, null=True)
    fvector_size = models.IntegerField(null=True)
    flength = models.IntegerField(null=True)
    fsampling_period = models.FloatField(null=True)

    def to_json(self):
        # TODO: figure out the file type
        # for now, we assume that the file is CSV

        print(self.document.path)
        self.json_data = make_json(self.document.path)


    def json_to_csv(self):
        df = pd.read_json(self.json_data)
        df = df.transpose()

        # TODO: rename the file so that it's name is the same as the
        # name it got uploaded as (but with the right file extension)
        df.to_csv('downloads/tmp.csv', encoding='utf-8', index=False, header=True)


    #def __str__(self):
    #   return self.description


# Function to convert a CSV to JSON
# Takes the file paths as arguments
# https://www.geeksforgeeks.org/convert-csv-to-json-using-python/
def make_json(csv_file_path):
   
   # create a dictionary
   data = {}
   
   # Open a csv reader called DictReader
   with open(csv_file_path, mode="rt") as csvf:
       csvReader = csv.DictReader(csvf)
       
       # Convert each row into a dictionary
       # and add it to data
       for rows in csvReader:
           print(rows)
           # Assuming a column named 'No' to
           # be the primary key
           key = rows['time']
           data[key] = rows
   return json.dumps(data, indent=4)
