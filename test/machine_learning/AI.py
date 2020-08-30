# Machine Learning is a step into the direction of artificial intelligence (AI).
from sklearn.metrics import r2_score
from scipy import stats
class DoAI(object):
    def getRSquared(self, dataType="All"):
        x = self.info["x"]
        y = self.info["y"]
        x, y = self.getData(dataType)
        mymodel = self.getPolynomialModel()
        return r2_score(y, mymodel(x))
    def getR(self):
        x = self.info["x"]
        slope, intercept, r, p, std_err = stats.linregress(x, self.info["y"])
        return r