# created 2023-04-22
# updated 2023-04-23 : add to_json fxn
from django.db import models
import csv
import json
import pandas as pd
from .validators import validate_file_extension

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    # document = models.FileField(upload_to='documents/')
    document = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    json_data = models.JSONField(null=True)

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

    def __str__(self):
        return self.description
 
 
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
