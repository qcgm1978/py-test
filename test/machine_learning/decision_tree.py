from datatype import DataTypes
import numpy as np
import unittest, pandas


class TDD_DECISION_TREE(unittest.TestCase):
    def test_read_data_set(self):
        file = "test/machine_learning/shows.csv"
        d = DataTypes()
        df = d.getCsvData(file)
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
        img='test/machine_learning/mydecisiontree.png'
        X = ["Age", "Experience", "Rank", "Nationality"]
        y = "Go"
        d1 = {"UK": 0, "USA": 1, "N": 2}
        d2 = {"YES": 1, "NO": 0}
        dictionary = {"Nationality": d1, "Go": d2}
        d = DataTypes()
        d\
            .getAndFormatData(file, dictionary)\
            .createDecisionTreeData(X, y)\
            .graphByData(img)\
            .show()
    def test_first_step(self):
        pass
    def test_gini(self):
        # Gini = 1 - (x/n)2 - (y/n)2
        # Where x is the number of positive answers("GO"), n is the number of samples, and y is the number of negative answers ("NO"), which gives us this calculation:
        file = "test/machine_learning/shows.csv"
        d = DataTypes()
        df = d.getCsvData(file)
        go = df["Go"]
        y = go
        self.assertIsInstance(y, pandas.core.series.Series)
        df = d.mapStrToNum({"Go": {"YES": 1, "NO": 0}})
        go = df["Go"]
        one = go == 1
        x = go[one].shape[0]
        n = df.shape[0]
        y = n - x
        Gini = 1 - (x / n) ** 2 - (y / n) ** 2
        self.assertAlmostEqual(Gini, 0.497, 3)
        self.assertEqual(n,13)
        value = [round(n * Gini), round(n * (1 - Gini))]
        self.assertEqual(value,[6,7])
        zero = go == 0
        dfZero = df[zero]
        rank = dfZero["Rank"]
        lessSpecifiedV = rank <= 6.5
        rank1 = rank[lessSpecifiedV]
        self.assertEqual(rank1.shape[0], 5)
        goCounts=dfZero[dfZero['Go']==1]
        self.assertEqual(goCounts.shape[0],0)
        # print(dfZero)


if __name__ == "__main__":
    unittest.main()
