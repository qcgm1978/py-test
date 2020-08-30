from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt
from predict import Predict
from handle_data import HandleData
from AI import DoAI
class DataTypes(HandleData,Predict,DoAI):
    
    def getGini(self, getSample=None):
        if callable(getSample):
            samples = getSample(self.df)
        else:
            samples = self.df
            # Gini = 1 - (x/n)2 - (y/n)2
        # Where x is the number of positive answers("GO"), n is the number of samples, and y is the number of negative answers ("NO"), which gives us this calculation:
        n = samples.shape[0]
        x=samples.loc[samples[self.target] == 1].shape[0]
        y = n - x
        Gini = 1 - (x / n) ** 2 - (y / n) ** 2
        return Gini,n,[y,x]
    
    def getDtree(self, features, y=None):
        if y is None:
            y=self.target
        df = self.df
        X = df[features]
        dtree = DecisionTreeClassifier()
        dtree = dtree.fit(X, df[y])
        return dtree
    
    
    def pyplot(self, bars=5):
        plt.hist(self.list, bars)
        self.show()
    def polynomialRegressionLine(self):
        x = self.info["x"]
        y = self.info["y"]
        mymodel = np.poly1d(np.polyfit(x, y, 3))
        minX = int(min(x))
        maxX = int(max(x))
        maxY = int(max(y))
        myline = np.linspace(minX, maxX, maxY)
        self.scatter()
        plt.plot(myline, mymodel(myline))
        self.show()
    
    def getPolynomialModel(self):
        x = self.info["x"]
        y = self.info["y"]
        mymodel = np.poly1d(np.polyfit(x, y, 4))
        return mymodel
    
    def plotScatter(self, dataType="All"):
        x = self.info["x"]
        y = self.info["y"]
        x, y = self.getData(dataType)
        self.scatter(x, y)
        self.show()
    
    def scatter(self, x=None, y=None):
        if x is None or y is None:
            x = self.info["x"]
            y = self.info["y"]
        plt.scatter(x, y)
    def show(self):
        plt.show()
    
    def scatterLine(self):
        mymodel = self.getModel()
        self.scatter()
        plt.plot(self.info["x"], mymodel)
        self.show()
    