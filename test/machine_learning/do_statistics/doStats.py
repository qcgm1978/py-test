from scipy import stats,constants
import math
class DoStats(object):
    def getMode(self):
        return stats.mode(self.list)
    def getLinregress(self, x=None):
        if x is None:
            x=self.info["x"]
        return stats.linregress(
            x, self.info["y"]
        )
    def getConstants(self):
        return constants
    def getBenfordLaw(self,n=1):
        return math.log10((n + 1) / n)