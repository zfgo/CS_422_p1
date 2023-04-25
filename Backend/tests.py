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
        comparison = metrics.accuracy(actual, predicted)
        print(f'Accuracy Score: {comparison:.4f} proportion of predictions were correct')
        print(f'Accuracy Score: {comparison * 100:.4f}% of predictions were correct')
        return comparison
    
    def test_correlation(self):
        '''Tests correlation (how related change is between two variables)'''
        print("========\nTest 2: Correlation\nHow similar 2 variables are\n========")
        data = pd.read_csv('CS_422_p1/Backend/test_data/set1/temp.csv')
        data['Daily minimum temperatures'] = data['Daily minimum temperatures'].str.replace('[^\d.]+', '', regex=True).astype(float)
        actual = data['Daily minimum temperatures'].values
        predicted = data.sample(len(actual), replace=True)['Daily minimum temperatures'].values
        comparison = metrics.MAE(actual, predicted)
        print(f'Mean-Absolute Error (MAE): {comparison:.4f}')
        return comparison

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