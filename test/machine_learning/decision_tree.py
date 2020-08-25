from datatype import DataTypes
import numpy as np
import unittest, pandas
class TDD_DECISION_TREE(unittest.TestCase):
    def setUp(self):
        file = "test/machine_learning/shows.csv"
        d1 = {"UK": 0, "USA": 1, "N": 2}
        d2 = {"YES": 1, "NO": 0}
        mapData = {"Nationality": d1, "Go": d2}
        self.d = DataTypes({"file": file, "mapData": mapData,'target':"Go"})
        return super().setUp()
    def test_read_data_set(self):
        file = "test/machine_learning/shows.csv"
        d = DataTypes({"file": file})
        df = d.readCsv(file)
        # print(df)
        data = np.array(df)
        self.assertIsInstance(data, np.ndarray)
        self.assertEqual(data.ndim, 2)
        self.assertEqual(data.shape, (13, 6))
        self.assertEqual(data.size, data.shape[0] * data.shape[1])
        d1 = {"UK": 0, "USA": 1, "N": 2}
        d2 = {"YES": 1, "NO": 0}
        df = d.mapStrToNum({"Nationality": d1, "Go": d2})
        features = ["Age", "Experience", "Rank", "Nationality"]
        X = df[features]
        y = df["Go"]
        # print(X)
        # print(y)
    def test_decision_tree(self):
        file = "test/machine_learning/shows.csv"
        img = "test/machine_learning/mydecisiontree.png"
        X = ["Age", "Experience", "Rank", "Nationality"]
        y = "Go"
        d1 = {"UK": 0, "USA": 1, "N": 2}
        d2 = {"YES": 1, "NO": 0}
        dictionary = {"Nationality": d1, "Go": d2}
        d = DataTypes()
        # d\
        #     .getAndFormatData(file, dictionary)\
        #     .createDecisionTreeData(X, y)\
        #     .graphByData(img)\
        #     .show()
    def test_first_step(self):
        df = self.d.df
        y = df["Go"]
        self.assertIsInstance(y, pandas.core.series.Series)
        Gini, n ,value= self.d.getGini()
        self.assertAlmostEqual(Gini, .497, 3)
        self.assertEqual(n, 13)
        self.assertEqual(value, [6, 7])
        # print(dfZero)
    def test_second_true_step(self):
        gini, n,value = self.d.getGini( getSample=lambda df:df[df["Rank"] <= 6.5])
        self.assertEqual(gini, 0)
        self.assertEqual(n, 5)
        self.assertEqual(value, [5, 0])
    def test_second_false_step(self):
        getSample=lambda df:df[df["Rank"] > 6.5]
        Gini, n,value = self.d.getGini( getSample=getSample)
        self.assertAlmostEqual(Gini, .219, 3)
        self.assertEqual(n,8)
        self.assertEqual(value, [1,7])
if __name__ == "__main__":
    unittest.main()
