# NAME : metrics.py
# DATE : 4/20/2023
# DESC : module for comparing various model accuracy metrics between (actual, predicted) data
# AUTHORS : Kareem Taha
from sklearn.metrics import accuracy_score, mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
import numpy as np

def accuracy(true, pred): 
    '''Returns proportion of properly predicted data'''
    return accuracy_score(true, pred)

def correlation(true, pred):
    '''Returns correlation between (actual, predicted) data'''
    return np.corrcoef(true,pred)[0,1]

def MAE(true, pred):
    '''Returns MAE (Mean-Absolute-Error) score, which is the expected deviation (i.e., avg(diff(true - pred)))'''
    return mean_absolute_error(true, pred)

def MAPE(true, pred):
    '''Returns MAPE (Mean-Absolute-Percentage-Error) score, which is the expected % deviation (i.e., MAE / True)''' 
    return mean_absolute_percentage_error(true, pred)

def SMAPE(true, pred):
    '''Returns SMAPE (Symmetric-Mean-Absolute-Percentage-Error) score, which is the expected % deviation from the average ([true + pred]/2) score'''
    return 1/len(true) * np.sum(2 * np.abs(pred-true) / (np.abs(true) + np.abs(pred))*100) # manual calculation because SKLEARN does not include sMAPE

def MSE(true, pred):
    '''Returns MSE (Mean-Squared-Error) score, which is the expected squared-deviation (punishes strong outliers)'''
    return mean_squared_error(true, pred)

def RMSE(true, pred):
    '''Return RMSE (Root-Mean-Squared-Error) score, which is the expected root-of the squared-deviation (like MAE but punishes strong outliers, more sensitive)'''
    return mean_squared_error(true, pred, squared=False)