# NAME : Grapher.py
# DATE : 4/27/2023
# DESC : module for creating graph figures meant to be passed to the DJango framework for display
# AUTHORS : Kareem Taha
import matplotlib.pyplot as plt

def graphTS(xtest, ypred, ytrue, xtrain, ytrain, units='s'):
    '''Graphs a Timeseries given Train data (contrib), Actual data (contrib), Predicted data (DS/MLE)'''
    fig = plt.figure(figsize=(10,6))
    plt.plot(xtrain, ytrain, c='r', linewidth=0.5, label="Training Data", linestyle='--')
    plt.plot(xtest,ytrue,c='g', linewidth=0.5, label="Actual (Contributor)", linestyle='--')
    plt.plot(xtest,ypred,c='b', linewidth=0.5, label="Predicted (DS/MLE)", linestyle='--')
    plt.xlabel(f'Time ({units})')
    plt.ylabel(f'Values')
    plt.title('Timeseries Actual vs. Predicted')
    plt.legend()
    return fig
