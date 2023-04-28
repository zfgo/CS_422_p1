# NAME : tests.py
# DATE : 4/24/2023
# DESC : module performing test functionality (via unittests)
# AUTHORS : Kareem Taha
import unittest
import pandas as pd
import metrics

class Test_Accuracy_Metrics(unittest.TestCase):
    def test_accuracy(self):
        '''Tests accuracy score (# of correct predictions)'''
        print("========\nTest 1: Accuracy-Score\n# of predictions correct\n========")
        data = pd.read_csv('CS_422_p1/Backend/test_data/set1/temp.csv')
        actual = data['Daily minimum temperatures'].values
        predicted = data.sample(len(actual), replace=True)['Daily minimum temperatures'].values
        accuracy = metrics.accuracy(actual, predicted)
        print(f'Accuracy Score: {accuracy:.4f} proportion of predictions were correct')
        print(f'Accuracy Score: {accuracy * 100:.4f}% of predictions were correct')
        return accuracy
    
    def test_correlation(self):
        '''Tests correlation (how related change is between two variables)'''
        print("========\nTest 2: Correlation\nHow similar 2 variables are\n========")
        data = pd.read_csv('CS_422_p1/Backend/test_data/set1/temp.csv')
        data['Daily minimum temperatures'] = data['Daily minimum temperatures'].str.replace('[^\d.]+', '', regex=True).astype(float)
        actual = data['Daily minimum temperatures'].values
        predicted = data.sample(len(actual), replace=True)['Daily minimum temperatures'].values
        R = metrics.correlation(actual, predicted)
        print(f'r-value: {R:.4f}')
        return R
    
    def test_MAE(self):
        '''Tests MAE (the average difference between (actual, predicted) data)'''
        print("========\nTest 3: MAE (Mean-Absolute Error)\nAverage prediction error\n========")
        data = pd.read_csv('CS_422_p1/Backend/test_data/set1/temp.csv')
        data['Daily minimum temperatures'] = data['Daily minimum temperatures'].str.replace('[^\d.]+', '', regex=True).astype(float)
        actual = data['Daily minimum temperatures'].values
        predicted = data.sample(len(actual), replace=True)['Daily minimum temperatures'].values
        MAE = metrics.MAE(actual, predicted)
        print(f'Mean-Absolute Error (MAE): {MAE:.4f}')
        return MAE
    
    def test_MAPE(self):
        '''Tests MAPE (the average % difference between (actual, predicted) data))'''
        print("========\nTest 4: MAPE (Mean-Absolute Percentage Error)\nAverage prediction % \error\n========")
        data = pd.read_csv('CS_422_p1/Backend/test_data/set1/temp.csv')
        data['Daily minimum temperatures'] = data['Daily minimum temperatures'].str.replace('[^\d.]+', '', regex=True).astype(float)
        actual = data['Daily minimum temperatures'].values
        predicted = data.sample(len(actual), replace=True)['Daily minimum temperatures'].values
        MAPE = metrics.MAPE(actual, predicted)
        print(f'Mean-Absolute Percentage Error (MAPE): {MAPE:.4f}')
        return MAPE
    
    def test_SMAPE(self):
        '''Tests SMAPE (the average % difference between (actual, predicted) data))'''
        print("========\nTest 5: SMAPE (Symmetric Mean-Absolute Percentage Error)\nAverage prediction % \error\n========")
        data = pd.read_csv('CS_422_p1/Backend/test_data/set1/temp.csv')
        data['Daily minimum temperatures'] = data['Daily minimum temperatures'].str.replace('[^\d.]+', '', regex=True).astype(float)
        actual = data['Daily minimum temperatures'].values
        predicted = data.sample(len(actual), replace=True)['Daily minimum temperatures'].values
        SMAPE = metrics.MAE(actual, predicted)
        print(f'Symmetric Mean-Absolute Percentage Error (MAPE): {SMAPE:.4f}')
        return SMAPE
    
    def test_MSE(self):
        '''Tests MSE (the average squared difference between (actual, predicted) data'''
        print("========\nTest 6: MSE (Mean-Squared Error)\nAverage squared prediction error\n========")
        data = pd.read_csv('CS_422_p1/Backend/test_data/set1/temp.csv')
        data['Daily minimum temperatures'] = data['Daily minimum temperatures'].str.replace('[^\d.]+', '', regex=True).astype(float)
        actual = data['Daily minimum temperatures'].values
        predicted = data.sample(len(actual), replace=True)['Daily minimum temperatures'].values
        MSE = metrics.MSE(actual, predicted)
        print(f'Mean-Squared Error (MSE): {MSE:.4f}')
        return MSE
    
    
    def test_RMSE(self):
        '''Tests RMSE (the average % difference between (actual, predicted) data))'''
        print("========\nTest 7: RMSE (Root Mean-Squared Error)\nAverage root squared prediction error\n========")
        data = pd.read_csv('CS_422_p1/Backend/test_data/set1/temp.csv')
        data['Daily minimum temperatures'] = data['Daily minimum temperatures'].str.replace('[^\d.]+', '', regex=True).astype(float)
        actual = data['Daily minimum temperatures'].values
        predicted = data.sample(len(actual), replace=True)['Daily minimum temperatures'].values
        RMSE = metrics.MAE(actual, predicted)
        print(f'Root Mean-Squared Error (RMSE): {RMSE:.4f}')
        return RMSE
    

class Test_Metadata_Objects(unittest.TestCase):
    def test_set(self):
        '''Test object metrics'''
        pass
    
if __name__ == "__main__":
    AccuracySuite = unittest.TestSuite()
    AccuracySuite.addTest(Test_Accuracy_Metrics('test_accuracy'))
    AccuracySuite.addTest(Test_Accuracy_Metrics('test_correlation'))
    Runner = unittest.TextTestRunner()
    Runner.run(AccuracySuite)