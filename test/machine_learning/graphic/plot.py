import numpy as np
import matplotlib.pyplot as plt


class Plot(object):
    def plotGroupedBar(
        self,
        l1,
        l2,
        title="Grouped bar chart with labels",
        l1txt="observed",
        l2txt="Predict",
        prop="Frenquency",
        txt=None,
    ):
        if txt is None:
            compare = self.compareByVariance([l1, l2])
            txt = "Variance Ratio: " + str(round(compare, 2))

        lenO = len(l1)
        lenP=len(l2)
        if lenO<=lenP:
            minLen=lenO
            l2=l2[:minLen]
        else:
            minLen=lenP
            l1=l1[:minLen]
        labels = range(1, minLen+1)
        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, l1, width, label=l1txt)
        rects2 = ax.bar(x + width / 2, l2, width, label=l2txt)
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(prop)
        ax.set_title(title)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        plt.figtext(
            0.5, 0.01, txt, wrap=True, horizontalalignment="center", fontsize=12
        )

        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate(
                    "{}".format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha="center",
                    va="bottom",
                )

        autolabel(rects1)
        autolabel(rects2)
        fig.tight_layout()
        self.show()

    def plotBar(
        self, height, x=None,
    ):
        if x is None:
            x = self.list
        plt.bar(x, height)
        self.show()

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
