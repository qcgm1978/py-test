from datatype import DataTypes
import unittest
class TDD_REGRESSION(unittest.TestCase):
    def test_regression(self):
        x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
        y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
        d = DataTypes({'x': x, 'y': y})
        # d.polynomialRegressionLine()
        r=d.getRSquared()
        self.assertAlmostEqual(r,.94,2)
        speed = d.predictPolynomialRegression(17)
        self.assertAlmostEqual(speed,89,0)
    def test_bad_fit(self):
        x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
        y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
        d = DataTypes({'x': x, 'y': y})
        # d.polynomialRegressionLine()
        r = d.getRSquared()
        self.assertAlmostEqual(r,.01,2)
    def test_multiple_regression(self):
        file="test/machine_learning/cars.csv"
        X = ['Weight', 'Volume']
        y = 'CO2'
        #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300ccm:
        predictVals = [2300, 1300]
        d=DataTypes({'x':X,'y':y})
        predict=d.predictMultipleRegression(file,predictVals)
        self.assertAlmostEqual(predict[0],107,0)
        self.assertEqual(list(map(lambda x:round(x,3),predict[1])),[0.008, 0.008])
if __name__ == '__main__':
    unittest.main()
