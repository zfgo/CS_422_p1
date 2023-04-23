# created 2023-04-22
# updated 2023-04-23 : add to_json fxn
from django.db import models
import csv
import json
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

    def __str__(self):
        return self.description
    
 
 
# Function to convert a CSV to JSON
# Takes the file paths as arguments
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
