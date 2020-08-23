import pandas
from sklearn import linear_model
from sklearn.metrics import r2_score
from scipy import stats
import numpy as np
import math
import matplotlib.pyplot as plt
class DataTypes(object):
    def __init__(self, n):
        if isinstance(n, dict):
            self.info = n
            self.prop = list(
                filter(
                    lambda key: isinstance(n[key], (list, np.ndarray)) and key, n.keys()
                )
            )[0]
            self.list = self[self.prop]
            self.len = len(self.list)
        else:
            self.n = n
    def __getitem__(self, i):
        try:
            return self.info[i]
        except KeyError:
            return None
    def pyplot(self, bars=5):
        plt.hist(self.list, bars)
        plt.show()
    def polynomialRegressionLine(self):
        x = self.info["x"]
        y = self.info["y"]
        mymodel = np.poly1d(np.polyfit(x, y, 3))
        minX = min(x)
        maxX = max(x)
        maxY=max(y)
        myline = np.linspace(minX, maxX, maxY)
        self.scatter()
        plt.plot(myline, mymodel(myline))
        self.show()
    def predictMultipleRegression(self, file, predictVals):
        X = self.info['x']
        y=self.info['y']
        df = pandas.read_csv(file)
        regr = linear_model.LinearRegression()
        regr.fit(df[X],df[ y])
        #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300ccm:
        predictedCO2 = regr.predict([predictVals])
        return predictedCO2[0],list(regr.coef_)
    def predictPolynomialRegression(self,predictX):
        mymodel=self.getPolynomialModel()
        return mymodel(predictX)
    def getPolynomialModel(self):
        x = self.info["x"]
        y = self.info["y"]
        mymodel = np.poly1d(np.polyfit(x, y, 3))
        return mymodel
    def getRSquared(self):
        x = self.info["x"]
        y = self.info["y"]
        mymodel=self.getPolynomialModel()
        return (r2_score(y, mymodel(x)))
    def plotScatter(self):
        self.scatter()
        self.show()
    def scatter(self):
        x = self.info["x"]
        y = self.info["y"]
        plt.scatter(x, y)
    def show(self):
        plt.show()
    def getR(self):
        x = self.info["x"]
        slope, intercept, r, p, std_err = stats.linregress(x, self.info["y"])
        return r
    def predict(self, predictX):
        slope, intercept, r, p, std_err = stats.linregress(
            self.info["x"], self.info["y"]
        )
        return slope * predictX + intercept
    def getModel(self):
        x = self.info["x"]
        myfunc = self.predict
        mymodel = list(map(myfunc, x))
        return mymodel
    def scatterLine(self):
        mymodel = self.getModel()
        self.scatter()
        plt.plot(self.info["x"], mymodel)
        self.show()
    def Numerical(self):
        return self.Discrete() or self.Continuous()
    def Discrete(self):
        return isinstance(self.n, int)
    def Continuous(self):
        return isinstance(self.n, float)
    def Categorical(self):
        return "color"
    def Ordinal(self):
        return "school grades"
    def getMean(self):
        # return sum(self['speed'])/len(self['speed'])
        prop = self.prop
        return np.mean(self[prop])
    def getMedian(self):
        # speed = self['speed'].copy()
        # speed.sort()
        # return speed[len(speed)//2]
        return np.median(self.list)
    def getMode(self):
        return stats.mode(self.list)
    def getStd(self):
        return np.std(self.list)
    def get1stdProbability(self):
        mean = self.getMean()
        minusSquare = map(lambda x: (x - mean) ** 2, self.list)
        sumVal = sum(list(minusSquare))
        probability = math.sqrt(sumVal / self.len)
        return probability
    def getDistance1std(self):
        expect = self["expectation"]
        if expect:
            mean = self.getMean()
            unitStd = self.get1stdProbability()
            difference = expect - mean
            differenceStd = difference / unitStd
            return differenceStd
        else:
            return self.getStd()
    def getPercentile(self, percent):
        # listP = self.list.copy()
        # listP.sort()
        # lessIndex=round(self.len*percent)
        # val = listP[lessIndex-1]
        # return val
        return np.percentile(self.list, percent * 100)
    def getProbability(self):
        std = self.getDistance1std()
        std2decimal = round(std, 2)
        if std2decimal == 1.00:
            return 0.683
        elif std2decimal == 1.87:
            return 0.015
        elif std2decimal == 2.00:
            return 0.954
    def getVariance(self):
        # mean = self.getMean()
        # difference = map(lambda x: x - mean, self.list)
        # square = map(lambda x: x ** 2, difference)
        # squareList = list(square)
        # variance = sum(squareList) / len(squareList)
        variance = np.var(self["speed"])
        return variance
