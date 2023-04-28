# NAME : graph.py
# DATE : 4/27/2023
# DESC : module for creating graph figures meant to be passed to the DJango framework for display
# AUTHORS : Kareem Taha
import matplotlib.pyplot as plt

def graph_model(x, y_pred, y_act, units='s'):
    fig, ax = plt.subplots(figsize=(5,4))
    fig.plot(x,y_act,c='r')
    fig.plot(x,y_pred,c='b')
    ax.set_xlabel(f'Time {units}')
    ax.set_ylabel(f'Values')
    ax.set_title('Time Series Actual vs. Predicted')
    fig.show()
    return fig