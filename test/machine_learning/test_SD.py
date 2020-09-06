from datatype import DataTypes
import unittest, pandas


class TDD_TEST_SD(unittest.TestCase):
    def test_test_SD(self):
        file = "py-test/test/machine_learning/data/metabolic.csv"
        X = ["Sex", "Metabolic rate"]
        y = "CO2"
        # predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300ccm:
        predictVals = [2300, 1300]
        d = DataTypes({"file": file, "x": X, "y": y})
        # df=d.readCsv(file)
        self.assertIsInstance(d.df, pandas.core.frame.DataFrame)
        mr = d.getDfCol(X[1])
        l = mr.values.tolist()
        self.assertAlmostEqual(d.getSD(l),694.4,1)
        
        # self.assertEqual(l, [])


if __name__ == "__main__":
    unittest.main()
