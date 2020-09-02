from datatype import DataTypes
import unittest,numpy as np
class TDD_TEST_DATA(unittest.TestCase):
    def setUp(self):
        file = "test/machine_learning/shows.csv"
        d1 = {"UK": 0, "USA": 1, "N": 2}
        d2 = {"YES": 1, "NO": 0}
        mapData = {"Nationality": d1, "Go": d2}
        sqlData=[
            { 'id': 1, 'name': 'John', 'fav': 154},
            { 'id': 2, 'name': 'Peter', 'fav': 154},
            { 'id': 3, 'name': 'Amy', 'fav': 155},
            { 'id': 4, 'name': 'Hannah', 'fav':0},
            { 'id': 5, 'name': 'Michael', 'fav':0}
        ]
        self.d = DataTypes({"file": file, "mapData": mapData,'target':"Go",'sqlData':sqlData})
        return super().setUp()
    # def test_read_data_set(self):
    #     file = "test/machine_learning/shows.csv"
    #     d = DataTypes({"file": file})
    #     df = d.readCsv(file)
    #     # print(df)
    #     data = np.array(df)
    #     self.assertIsInstance(data, np.ndarray)
    #     self.assertEqual(data.ndim, 2)
    #     self.assertEqual(data.shape, (13, 6))
    #     self.assertEqual(data.size, data.shape[0] * data.shape[1])
    #     d1 = {"UK": 0, "USA": 1, "N": 2}
    #     d2 = {"YES": 1, "NO": 0}
    #     df = d.mapStrToNum({"Nationality": d1, "Go": d2})
    #     features = ["Age", "Experience", "Rank", "Nationality"]
    #     X = df[features]
    #     y = df["Go"]
        # print(X)
        # print(y)
    def test_mysql(self):
        val = { 'id': 1, 'name': 'John', 'fav': 154}
        r=self.d.insertInto(val)
        self.assertEqual(self.d.mycursor.rowcount, 1 if r else -1)
if __name__ == '__main__':
    unittest.main()
