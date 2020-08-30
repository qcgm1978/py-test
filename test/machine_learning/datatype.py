from sklearn.tree import DecisionTreeClassifier
import numpy as np
from predict import Predict
from handle_data import HandleData
from AI import DoAI
from graphic.plot import Plot
class DataTypes(HandleData,Predict,DoAI,Plot):
    
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
    
    
    