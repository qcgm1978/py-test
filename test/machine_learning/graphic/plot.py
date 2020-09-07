import numpy as np
import matplotlib.patches as mpatches
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
        l1, l2,minLen = self.normalize(l1, l2)
        labels = range(1, minLen + 1)
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
    def normalize(self, l1, l2):
        lenO = len(l1)
        lenP = len(l2)
        if lenO <= lenP:
            minLen = lenO
            l2 = l2[:minLen]
        else:
            minLen = lenP
            l1 = l1[:minLen]
        return  l1, l2,minLen
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
    def scatterDots(self,x,y):
        self.scatter(x,y)
        self.show()
    def scatterGrouped(self,l,title='',xTxt='',yTxt=''):
        fig, ax = plt.subplots()
        ax.set_title(title)
        ax.set_xlabel(xTxt)
        ax.set_ylabel(yTxt)
        for ind,i in enumerate(l):
            y=i[1]
            if isinstance(i[0],str):
                x=[ind+1]*len(y)
            c='#F11F10' if len(y)==1 else '#0E0E0E'
            ax.scatter(x, y,c=c)
            # if ind%2:
            # labels[ind] = i[0]
        fig.canvas.draw()
        labels = [item.get_text() for item in ax.get_xticklabels()]
        labels[1] = l[0][0]
        labels[3] = l[1][0]
        labels[5] = l[2][0]
        labels[7] = l[3][0]
        ax.set_xticklabels(labels)
        self.demo_con_style(ax, "Male,Std. Dev.,{0}".format(round(self.getSD(l[0][1], ddof=1))),(1.6,2000))
        self.demo_con_style(ax, "Female,Std. Dev.,{0}".format(round(self.getSD(l[1][1], ddof=1))),(2.2,2000))
        self.show()
    def demo_con_style(self,ax, connectionstyle,position):
        x1, y1 = position[0]-.1, 2000
        x2, y2 = position[0]-.1, 1500
        ax.plot([x1, x2], [y1, y2])
        ax.annotate("",
                    xy=(x1, y1), xycoords='data',
                    xytext=(x2, y2), textcoords='data',
                    arrowprops=dict(arrowstyle="<->", color="0.5",
                                    # shrinkA=5, shrinkB=5,
                                    patchA=None, patchB=None,
                                    # connectionstyle=connectionstyle,
                                    ),
                    )
        ax.text(.05, .95, connectionstyle.replace(",", ",\n"),
                 position=position, va="top")
    def plotArrow(self,ax):
        x_tail = 0.1
        y_tail = 0.1
        x_head = 0.1
        y_head = 0.9
        dx = x_head - x_tail
        dy = y_head - y_tail
        arrow = mpatches.FancyArrowPatch(posA=(x_tail, y_tail), posB=(dx, dy),
                                 mutation_scale=10)
        ax.add_patch(arrow)
    def scatter(self, x=None, y=None):
        if x is None or y is None:
            x = self.info["x"]
            y = self.info["y"]
        l1, l2,minLen = self.normalize(x,y)
        plt.scatter(l1, l2)
    def show(self):
        plt.show()
    def scatterLine(self):
        mymodel = self.getModel()
        self.scatter()
        plt.plot(self.info["x"], mymodel)
        self.show()
