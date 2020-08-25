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
        go = df["Go"]
        y = go
        self.assertIsInstance(y, pandas.core.series.Series)
        # Gini = 1 - (x/n)2 - (y/n)2
        # Where x is the number of positive answers("GO"), n is the number of samples, and y is the number of negative answers ("NO"), which gives us this calculation:
        one = go == 1
        x = go[one].shape[0]
        n = df.shape[0]
        Gini, n = self.d.getGini()
        value = [round(n * Gini), round(n * (1 - Gini))]
        zero = go == 0
        dfZero = df[zero]
        rank = dfZero["Rank"]
        lessSpecifiedV = rank <= 6.5
        rank1 = rank[lessSpecifiedV]
        self.assertEqual(rank1.shape[0], 5)
        goCounts = dfZero[dfZero["Go"] == 1]
        self.assertEqual(goCounts.shape[0], 0)
        self.assertAlmostEqual(Gini, 0.497, 3)
        self.assertEqual(n, 13)
        self.assertEqual(value, [6, 7])
        # print(dfZero)

    def test_second_true_step(self):
        df = self.d.df
        go = df["Go"] == 0
        rank = df["Rank"]
        go1 = df[go]
        goRank = go1[go1["Rank"] <= 6.5]
        samples = goRank.shape[0]
        zero = goRank[goRank["Go"] == 0].shape[0]
        value = [zero, samples - zero]
        gini = samples - value[0]
        self.assertEqual(gini, 0)
        self.assertEqual(samples, 5)
        self.assertEqual(value, [5, 0])

    def test_second_false_step(self):
        df = self.d.df
        Nationality = df["Nationality"]
        Rank = df["Rank"]
        dfRank = df[Rank > 6.5]
        n = dfRank.shape[0]
        self.assertEqual(n, 8)
        dfRankGo = dfRank["Go"]
        x = dfRankGo[dfRankGo == 1].shape[0]
        getSample=lambda df:df[df["Rank"] > 6.5]
        self.assertEqual(x, 7)
        Gini, n = self.d.getGini( getSample=getSample)
        self.assertAlmostEqual(Gini, 0.219, 3)
    def test_DataFrame_loc(self):
        df = pandas.DataFrame(
            [[1, 2], [4, 5], [5, 8]],
            index=['cobra', 'viper', 'sidewinder'],
            columns=['max_speed', 'shield']
        )
        self.assertEqual(df.shape, (3, 2))
        l=df.loc[df['shield'] > 6]
        self.assertListEqual(list(l.values[0]),[5,8])

if __name__ == "__main__":
    unittest.main()
