# NAME : Metrics.py
# DATE : 4/20/2023
# DESC : module for comparing various model accuracy metrics between (actual, predicted) data
# AUTHORS : Kareem Taha
from sklearn.metrics import accuracy_score, mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
import numpy as np

class Metrics:

    @staticmethod
    def accuracy(true, pred) -> float: 
        '''Returns proportion of properly predicted data'''
        return accuracy_score(true, pred)

    @staticmethod
    def correlation(true, pred) -> float:
        '''Returns correlation between (actual, predicted) data'''
        return np.corrcoef(true,pred)[0,1]

    @staticmethod
    def MAE(true, pred) -> float:
        '''Returns MAE (Mean-Absolute-Error) score, which is the expected deviation (i.e., avg(diff(true - pred)))'''
        return mean_absolute_error(true, pred)

    @staticmethod
    def MAPE(true, pred) -> float:
        '''Returns MAPE (Mean-Absolute-Percentage-Error) score, which is the expected % deviation (i.e., MAE / True)''' 
        return mean_absolute_percentage_error(true, pred)

    @staticmethod
    def SMAPE(true, pred) -> float:
        '''Returns SMAPE (Symmetric-Mean-Absolute-Percentage-Error) score, which is the expected % deviation from the average ([true + pred]/2) score'''
        return 1/len(true) * np.sum(2 * np.abs(pred-true) / (np.abs(true) + np.abs(pred))*100) # manual calculation because SKLEARN does not include sMAPE

    @staticmethod
    def MSE(true, pred) -> float:
        '''Returns MSE (Mean-Squared-Error) score, which is the expected squared-deviation (punishes strong outliers)'''
        return mean_squared_error(true, pred)

    @staticmethod
    def RMSE(true, pred) -> float:
        '''Return RMSE (Root-Mean-Squared-Error) score, which is the expected root-of the squared-deviation (like MAE but punishes strong outliers, more sensitive)'''
        return mean_squared_error(true, pred, squared=False)
    
    @staticmethod
    def Run(true, pred) -> list:
        return [Metrics.accuracy(true, pred), Metrics.correlation(true, pred), Metrics.MAE(true, pred), Metrics.MAPE(true, pred),
                Metrics.SMAPE(true, pred), Metrics.MSE(true, pred), Metrics.RMSE(true, pred)]