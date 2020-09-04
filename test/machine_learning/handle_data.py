# Machine Learning is making the computer learn from studying data and statistics.
import pandas,pydotplus
import numpy as np
import matplotlib.image as pltimg
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from mathMethods.doMath import DoMath
from do_statistics.doStats import DoStats
from mysql_data.mysqlOp import MysqlOp
class HandleData(DoMath,DoStats,MysqlOp):
    def __init__(self, n=None):
        unique=n['unique'] if 'unique' in n else None
        MysqlOp.__init__(self,'data',n['sqlData'],db='machine_learning',unique=unique)
        if isinstance(n, dict):
            if 'sqlData' in n:
                n=n['sqlData'][0]
            self.info = n
            listProp = list(
                filter(
                    lambda key: isinstance(n[key], (list, np.ndarray)) and key, n.keys()
                )
            )
            if len(listProp):
                self.prop = listProp[0]
                self.list = self[self.prop]
                self.len = len(self.list)
            if "target" in n:
                self.target = n["target"]
            if "file" in n:
                self.df = self.readCsv(n["file"])
                if "mapData" in n:
                    self.df = self.mapStrToNum(n["mapData"])
        else:
            self.n = n
    
    def __getitem__(self, i):
        try:
            return self.info[i]
        except KeyError:
            return None
    def getAndFormatData(self, file, dictionary):
        df = self.readCsv(file)
        self.mapStrToNum(dictionary, df)
        return self
    
    def graphByData(self, img):
        graph = pydotplus.graph_from_dot_data(self.graphData)
        graph.write_png(img)
        img = pltimg.imread(img)
        imgplot = plt.imshow(img)
        return self
    def scale(self, file, scaleCols):
        scale = StandardScaler()
        df = self.readCsv(file)
        X = df[scaleCols]
        scaledX = scale.fit_transform(X)
        return scaledX
    def readCsv(self, file):
        self.df = pandas.read_csv(file)
        return self.df
    def mapStrToNum(self, dictionary, df=None):
        if df is None:
            df = self.df
        for field, v in dictionary.items():
            df[field] = df[field].map(v)
        self.df = df
        return df
    def getData(self, dataType="All"):
        x = self.info["x"]
        y = self.info["y"]
        if dataType == "train":
            x = x[:80]
            y = y[:80]
        elif dataType == "test":
            x = x[80:]
            y = y[80:]
        return x, y
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
    
    def getStd(self):
        return np.std(self.list)
    
    def get1stdProbability(self):
        mean = self.getMean()
        minusSquare = map(lambda x: (x - mean) ** 2, self.list)
        probability = self.getMeanSqr(minusSquare)
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
