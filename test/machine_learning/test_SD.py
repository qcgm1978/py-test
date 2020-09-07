from datatype import DataTypes
import unittest, pandas
from mysql_data.decorators_func import singleton


class TDD_TEST_SD(unittest.TestCase):
    @singleton
    def setUp(self):
        file = "test/machine_learning/data/metabolic.csv"
        X = ["Sex", "Metabolic rate"]
        y = "CO2"
        predictVals = [2300, 1300]
        self.__class__.d = DataTypes({"file": file, "x": X, "y": y})
        self.__class__.l1 = self.__class__.d.queryDf('Sex == "Male"')
        self.__class__.l2 = self.__class__.d.queryDf('Sex == "Female"')
        self.__class__.s1 = self.__class__.d.getSD(self.__class__.l1, ddof=1)
        self.__class__.s2 = self.__class__.d.getSD(self.__class__.l2, ddof=1)

    def test_test_SD(self):
        self.assertIsInstance(self.d.df, pandas.core.frame.DataFrame)
        mr = self.d.getDfCol()
        self.assertIsInstance(mr, pandas.core.series.Series)
        self.assertAlmostEqual(self.d.getSD(mr), 694.4, 1)
        self.assertAlmostEqual(self.s1, 894.37, 2)
        self.assertAlmostEqual(self.s2, 420.96, 2)

    def test_plot(self):
        # self.d.plotGroupedBar(
        #     l1=self.l1,
        #     l2=self.l2,
        #     l1txt="Male",
        #     l2txt="Female",
        #     title='Furness data set on metabolic rates of northern fulmars',
        #     prop='Metabolic rate'
        # )
        y1 = self.l1
        y2 = self.l2
        mMean = self.d.getMean(self.l1)
        fMean=self.d.getMean(self.l2)
        self.d.scatterGrouped(
            [
                ("Male", y1 + [mMean]),
                ("Female", y2+[fMean]),
                ("Male Mean", [mMean]),
                ("Female Mean", [fMean]),
            ],
            title="Metabolic rate versus sex for 14 northern fulmars",
            yTxt="Matabolic rate",
            xTxt="Sex",
        )


if __name__ == "__main__":
    unittest.main()
