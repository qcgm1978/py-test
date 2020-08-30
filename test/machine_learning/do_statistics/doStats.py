from scipy import stats
class DoStats(object):
    def getMode(self):
        return stats.mode(self.list)
    def getLinregress(self, x=None):
        if x is None:
            x=self.info["x"]
        return stats.linregress(
            x, self.info["y"]
        )