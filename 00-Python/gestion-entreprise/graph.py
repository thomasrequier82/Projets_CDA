import matplotlib as mil

mil.use('TkAgg')
import matplotlib.pyplot as plt
from entreprise import Entreprise
import constantes as C


class Graph():
    #GRAPHS = []
#Affiche Le Graphique
    def __init__(self, **args):
        [setattr(self, k, v) for k, v in args.items()]

    def showGraph(self):
        xValues = []
        for i in range(C.MOIS_MAX) :
            xValues.append(i)
        for e in Entreprise.ENTREPRISES:
            f = plt.figure(e.id +1,figsize=[0.58*C.MOIS_MAX,7])
            w = f.get_figwidth()*f.dpi
            fid = plt.gcf().number
            x = (fid -1)* w +10*fid
            f.canvas.manager.window.wm_geometry("+%d+%d" % (x,0))
            yValues = [None] * C.MOIS_MAX
            for i in range(len(e.historiquemois)):
                yValues[i] = e.historiquemois[i]
            self.createSubplot([25, 1, (2, 5)], xValues, yValues, "Entreprise" +str(e.id +1), self.xName, self.yName)
            for i in range(len(e.historiquevoituresmois)):
                yValues[i] = e.historiquevoituresmois[i]
            self.createSubplot([15, 1, (8, 10)], xValues, yValues, label="Voitures", xname= self.xName, yname= "Voitures", color="y")
            for i in range(len(e.historiquesalariemois)):
                yValues[i] = e.historiquesalariemois[i]
            self.createPlot(xValues, yValues, label="Salariés", xname= self.xName, color="m")
            for i in range(len(e.historiquechargesmois)):
                yValues[i] = e.historiquechargesmois[i]
            self.createSubplot([15, 1, (13, 15)], xValues, yValues, label="Charges", xname= self.xName, color="r",ylimit=500000)
            for i in range(len(e.historiquegainmois)):
                yValues[i] = e.historiquegainmois[i]
            self.createPlot(xValues, yValues, label="Gain", xname= self.xName, color="g",ylimit=500000)

            plt.grid(True)
        plt.figure(1)
        plt.show()

    def createSubplot(self, i, xvalues, yvalues, label="", xname="", yname="", title="", color=None, ylimit=0):
        if i is int:
            plt.subplot(i)
        else:
            plt.subplot(i[0], i[1], i[2])
        self.createPlot(xvalues,yvalues,label,xname,yname,title,color=color,ylimit=ylimit)

    @staticmethod
    def createPlot(xvalues,yvalues,label="",xname="",yname="",title="",color=None,ylimit=0):
        plt.plot(xvalues,yvalues,marker="o",label=label,color=color)
        plt.grid(True)
        plt.figlegend(loc="upper center")
        plt.xlabel(xname)
        plt.ylabel(yname)
        plt.title(title)
        plt.grid(True)
        plt.tick_params(axis="y")
        maxRange=[]
        for i in range(C.MOIS_MAX):
            maxRange.append(i+1)
        plt.xticks(xvalues,maxRange)
        if ylimit > 0:
            plt.ylim(0, ylimit)
            for x,y in zip(xvalues,yvalues):
                baseY = y
                textY= 10
                if y > ylimit:
                    texty=60
                    baseY=0
                    plt.arrow(x=x,y=y,dx=0,dy=-y + ylimit / 5*4, width=0.05, head_length=50000, zorder=2, color=color)
                if color == "r" and y <= ylimit:
                    plt.annotate(y, (x, baseY), textcoords="offset pixels", xytext=(0, textY), ha="center",va="center_baseline", size=8, color=color)
                else:
                    plt.annotate(y, (x, baseY), textcoords="offset pixels", xytext=(0, textY), ha="center", size=8,color=color)
            return
        for x,y in zip(xvalues, yvalues):
            plt.annotate(y, (x, y), textcoords="offset pixels", xytext=(0, 10), ha="center", size=8)