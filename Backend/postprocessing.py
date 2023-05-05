# NAME : postprocessing.py
# DATE : 4/24/2023
# DESC : module completing data processing to create metadata objects, complete metrics testing, etc.
# AUTHORS : Kareem Taha
import pandas as pd
import unittests
from Metrics import Accuracy
from Grapher import graphTS
import matplotlib.pyplot as plt


# TODO

# Metadata
# Get metadata from front-end
# Create metadata object
# Store (however we want)

# Metrics
# Get actual test data from contributor (from db)
# Get predicted data from DS/MLE (from db)
# Graph them overlaying?
# Calculate metrics via functions and return to user

def convert_json(fname) -> list:
    '''Convert a TimeSeries JSON into DF, RETURN time & values'''
    df = pd.read_json(fname)        # pandas DF containing TS (converted from JSON)
    time = df.iloc[:,0].values      # time values
    values = df.iloc[:,1:].values   # TS values
    return time, values

def generate_accuracy(true, pred) -> list:
    metrics = Accuracy.Run(true, pred)
    return metrics

def model_compare(train, test, mle):
    '''Returns metrics/graph of DS/MLE model given filenames for: (contributor train, contributor test, DS/MLE prediction)'''
    xtrain, ytrain = convert_json(train)
    xtest, ytest = convert_json(test)
    xmle, ymle = convert_json(mle)
    metrics = generate_accuracy(ytest, ymle)
    graph = graphTS(xtest=xtest, ypred=ymle, ytrue=ytest, xtrain=xtrain, ytrain=ytrain)
    return metrics, graph

def Test(): unittests.run()