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
django.setup()
from django.core.files.base import ContentFile
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
        print("here",x, y)
        return x,y

def generate_metrics():
    '''For all tasks, compare DS models to testing data set and save the metrics, graph to the database/zip-file '''

    # RETRIEVING: TASKS (and associated documents)
    for t in models.Task.objects.all():
        for doc in models.Document.objects.filter(task=t):# documents associated to that task
            if doc.is_test: xtest, ytest = generate_df(doc)          # test set
            elif doc.is_train: xtrain, ytrain = generate_df(doc)   # train set
            elif doc.is_mle:                                                    # ds/mle set
                # GENERATE: STATS
                print("save")
                xmle, ymle = generate_df(doc)  
                metrics = json.dumps(Accuracy.Run(ytest, ymle))
                print(metrics)
                graph = Grapher.graphTS(xtest=xtest, ypred=ymle, ytrue=ytest, xtrain=xtrain, ytrain=ytrain)
                # SAVING: TO MODELS OBJECT, DATABASE (accessible via downloadable zip)                            
                name = re.sub("documents/\d+/", "", os.path.splitext(doc.document.name)[0])# attach metrics/graphs to DS model so multiple models can be uploaded (for more DS models)
                image = Grapher.generate_image(graph, file_name= name)
                doc.image.save(name= f'{name}.png', content= image)
                file = ContentFile(metrics)
                doc.solution.save(name=f'{name}.json', content=file)
                doc.save()
            else: print('the document is not classified as any set')

