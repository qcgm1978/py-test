from datatype import DataTypes
import unittest, pandas
class TDD_TEST_SD(unittest.TestCase):
    def setUp(self):
        file = "test/machine_learning/data/metabolic.csv"
        X = ["Sex", "Metabolic rate"]
        y = "CO2"
        predictVals = [2300, 1300]
        self.d = DataTypes({"file": file, "x": X, "y": y})
        self.l1 = self.d.queryDf('Sex == "Male"')
        self.l2 = self.d.queryDf('Sex == "Female"')
    def test_test_SD(self):
        self.assertIsInstance(self.d.df, pandas.core.frame.DataFrame)
        mr =self. d.getDfCol()
        self.assertIsInstance(mr,pandas.core.series.Series)
        l = self.d.convertSeriesToList(mr)
        self.assertEqual(l,[525.8, 605.7, 843.3, 1195.5, 1945.6, 2135.6, 2308.7, 2950.0, 727.7, 1086.5, 1091.0, 1361.3, 1490.5, 1956.1])
        self.assertAlmostEqual(self.d.getSD(mr), 694.4, 1)
        
        self.assertAlmostEqual(self.d.getSD(self.l1),836.6,1)
        self.assertAlmostEqual(self.d.getSD(self.l2),384.3,1)
    def test_plot(self):
        self.d.plotGroupedBar(
            observed=self.l1.values.tolist(),
            predicted=self.l2.values.tolist(),
            actual="Male",
            predict="Female",
            title='Furness data set on metabolic rates of northern fulmars',
            prop='Metabolic rate'
        )
if __name__ == "__main__":
    unittest.main()
