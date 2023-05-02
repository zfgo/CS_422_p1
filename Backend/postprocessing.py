# NAME : postprocessing.py
# DATE : 4/24/2023
# DESC : module completing data processing to create metadata objects, complete metrics testing, etc.
# AUTHORS : Kareem Taha
import pandas as pd
import unittests
from Metrics import Metrics
from graph import graph_model
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
    return [time, values]

def generate_accuracy(true, pred) -> list:
    metrics = Metrics.Run(true, pred)
    return metrics

def graph_model(x, pred, true, units='s'):
    fig, ax = plt.subplots(figsize=(5,4))
    fig.plot(x,true,c='r')
    fig.plot(x,pred,c='b')
    ax.set_xlabel(f'Time {units}')
    ax.set_ylabel(f'Values')
    ax.set_title('Time Series Actual vs. Predicted')
    fig.show()
    return fig

def Test(): unittests.run()