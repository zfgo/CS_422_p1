# NAME : postprocessing.py
# DATE : 4/24/2023
# DESC : module completing data retrieval, processing, and storage via other-module implementation
# AUTHORS : Kareem Taha
import re
import pandas as pd
import os
import django
import json
import Backend.Grapher as Grapher
from django.core.files.base import ContentFile
django.setup()
from Backend.Metrics import Accuracy, np
from zach_test import models

def split_df(df) -> list:
    '''Convert a TimeSeries DataFrame into time (x) & values (y) as np.arrays, then returns'''
    time = df.iloc[:,0].values     # time values
    values = df.iloc[:,1].values   # TS values
    return time, values

def generate_df(Document):
    '''Retrieve a DJango document object (representing a task), parse and return the train & test contributor data'''
    fname = os.path.basename(Document.document.name) # Read data set
    fext = os.path.splitext(fname)[1]   # Get file-type and act accordingly
    with Document.document.open() as file: 
        f = file.read()
        if fext == '.csv': df = pd.read_csv(Grapher.io.StringIO(f.decode('utf-8')))
        if fext == '.json': df = pd.read_json(Grapher.io.StringIO(f.decode('utf-8')))
        if fext == '.xlsx': df = pd.read_excel(Grapher.io.StringIO(f.decode('utf-8')))
        x,y = split_df(df)
        return x,y

def generate_metrics():
    '''For all tasks, compare DS models to testing data set and save the metrics, graph to the database/zip-file '''

    # RETRIEVING: TASKS (and associated documents)
    tasks = models.Task.objects.all() # all tasks
    for task in tasks:
        docs = models.Document.objects.filter(task=task) # documents associated to that task
        for doc in docs:                                 # there will be 3
            if doc.if_test: xtest, ytest = generate_df(doc) # test set
            #elif doc.if_ds: xmle, ymle = generate_df(doc)   # ds/mle set
            else: xtrain, ytrain = generate_df(doc)         # train set
            xmle = np.random.choice(xtest, size=len(xtest), replace=True)
            ymle = np.random.choice(ytest, size=len(ytest), replace=True)

    # REPORTING: MODEL ACCURACY
        metrics = json.dumps(Accuracy.Run(ytest, ymle))
        graph = Grapher.graphTS(xtest=xtest, ypred=ymle, ytrue=ytest, xtrain=xtrain, ytrain=ytrain)
               
    # SAVING: TO MODELS OBJECT, DATABASE (accessible via downloadable zip)
        docs = models.Document.objects.filter(task=task) # documents associated to that task
        for doc in docs:
            #if doc.if_ds:                                 # attach metrics/graphs to DS model so multiple models can be uploaded (for more DS models)
                name = re.sub("documents/\d+/", "", os.path.splitext(doc.document.name)[0])
                image = Grapher.generate_image(graph, file_name= name)
                doc.image.save(name= f'{name}.png', content= image)
                file = ContentFile(metrics)
                doc.solution.save(name=f'{name}.json', content=file)
                doc.save()

generate_metrics()