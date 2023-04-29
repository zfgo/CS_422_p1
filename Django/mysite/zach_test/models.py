# created 2023-04-22
# updated 2023-04-23 : add to_json fxn.
# updated 2023-04-29 : add id to the Document model (used to get the 
#   correct file during download).
#   Also, update functions to convert to and from JSON and CSV, as well
#   as add functions to convert to and from JSON and XLSX.
from django.db import models
import csv
import json
import openpyxl
from .validators import validate_file_extension

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    # document = models.FileField(upload_to='documents/')
    document = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    json_data = models.JSONField(null=True)
    id = models.BigAutoField(primary_key=True)

    def to_json(self):
        # TODO: figure out the file type
        # for now, we assume that the file is CSV

        print(self.document.path)
        self.json_data = make_json(self.document.path)

    def json_to_csv(self):
        """
        Method to convert the json data stored into the model to a CSV 
        file to be downloaded by the user
        """
        # create the file name
        # FIXME: everything after the '.' in the file name needs to be 
        # stripped and 'csv' needs to be appended
        csv_file_name = "downloads/" + self.document.name
        
        # Load the JSON data and extract the header row
        data = json.loads(self.json_data)
        header = list(data[0].keys())

        # Open the CSV file for writing and write the header row
        with open(csv_file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)

            # Write each row of data to the CSV file
            for row in data:
                writer.writerow([row[column] for column in header])

    def json_to_xlsx(self):
        # create the file name
        # FIXME: everything after the '.' in the file name needs to be 
        # stripped and 'csv' needs to be appended
        xlsx_file_name = "downloads/" + self.document.name
        # Load the JSON data and extract the header row
        data = json.loads(self.json_data)
        header = list(data[0].keys())

        # Create a new Excel workbook and worksheet
        wb = openpyxl.Workbook()
        sheet_name = "Sheet1"
        sheet = wb.active
        sheet.title = sheet_name

        # Write the header row to the worksheet
        sheet.append(header)

        # Write each row of data to the worksheet
        for row in data:
            sheet.append([row[column] for column in header])

        # Save the Excel workbook to a file
        wb.save(xlsx_file_name)

    def __str__(self):
        return self.description
 
 
def csv_to_json(csv_file_name, time_column_index):
    """
    Function to convert a CSV to JSON

    Take the path to the csv file and the column that holds time, and 
    convert to a JSON object. We assume that the time column is 1-based
    """
    time_column_index -= 1 # it is entered as 1-based, so we convert to 0-based indexing

    # Open the CSV file and read its contents
    with open(csv_file_name, 'rt') as csv_file:
        reader = csv.reader(csv_file)

        # Create a list to store the rows as dictionaries
        data = []
        header = []

        # Iterate through the CSV file and convert each row to a dictionary
        for row in reader:
            if not header:
                header = row
            else:
                row_data = {}
                for i in range(len(header)):
                    if i == time_column_index:
                        row_data[header[i]] = float(row[i])
                    else:
                        row_data[header[i]] = float(row[i])
                data.append(row_data)

    # Convert the list of dictionaries to a JSON object and return it
    return json.dumps(data)


def xlsx_to_json(xlsx_file_name):
    """
    Function to convert a XLSX (Excel) to JSON

    Take the path to the xlsx file and convert to a JSON object. We use 
    the openpyxl library to help us do this.
    """
    # Open the Excel file and select the first sheet
    wb = openpyxl.load_workbook(xlsx_file_name)
    sheet = wb.active

    # Create a list to store the rows as dictionaries
    data = []
    header = []

    # Iterate through the sheet and convert each row to a dictionary
    for row in sheet.iter_rows(values_only=True):
        if not header:
            header = row
        else:
            row_data = {}
            for i in range(len(header)):
                row_data[header[i]] = row[i]
            data.append(row_data)

    # Convert the list of dictionaries to a JSON object and return it
    return json.dumps(data)
