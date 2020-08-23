from scipy import stats
import numpy as np
import math
class DataTypes(object):
    def __init__(self, n):
        if isinstance(n, dict):
            self.info = n
            self.prop = list(
                filter(lambda key: isinstance(n[key], list) and key, n.keys())
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
