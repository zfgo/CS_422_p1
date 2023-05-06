# NAME : Metrics.py
# DATE : 4/20/2023
# DESC : module for comparing various model accuracy metrics between (actual, predicted) data
# AUTHORS : Kareem Taha
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
import numpy as np

class Accuracy:

    @staticmethod
    def accuracy(true, pred) -> float: 
        '''Returns proportion of properly predicted data'''
        return np.sum(true==pred)/len(true) # manual calculation because SKLEARN AS doesn't function properly

    @staticmethod
    def correlation(true, pred) -> float:
        '''Returns correlation between (actual, predicted) data'''
        print("here", true, pred)
        if len(true) == len(pred):
            return np.corrcoef(true,pred)[0,1]
        else:
            return np.corrcoef([0],[0])[0,1]

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
        return 1/(len(true)+.0001) * np.sum(2 * np.abs(pred-true) / (np.abs(true) + np.abs(pred) + .001)*100) # manual calculation because SKLEARN does not include sMAPE

    @staticmethod
    def MSE(true, pred) -> float:
        '''Returns MSE (Mean-Squared-Error) score, which is the expected squared-deviation (punishes strong outliers)'''
        return mean_squared_error(true, pred)

    @staticmethod
    def RMSE(true, pred) -> float:
        '''Return RMSE (Root-Mean-Squared-Error) score, which is the expected root-of the squared-deviation (like MAE but punishes strong outliers, more sensitive)'''
        return mean_squared_error(true, pred, squared=False)
    
    @staticmethod
    def Run(true, pred) -> dict:
        '''Runs all metrics and returns as a dict'''
        if(true.dtype in ['str', 'str32', 'str64'] or pred.dtype in ['str','str32','str64']): return{'error':'cannot create metrics because time value is in strings'}
        return {'accuracy':Accuracy.accuracy(true, pred), 'MAE':Accuracy.correlation(true, pred), 
                'MAPE':Accuracy.MAE(true, pred), 'MAPE':Accuracy.MAPE(true, pred), 
                'SMAPE': Accuracy.SMAPE(true, pred), 'MSE':Accuracy.MSE(true, pred), 
                'RMSE':Accuracy.RMSE(true, pred)}
    
