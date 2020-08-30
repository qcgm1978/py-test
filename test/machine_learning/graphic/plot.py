import numpy as np
import matplotlib.pyplot as plt
class Plot(object):
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