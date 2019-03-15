import matplotlib.pyplot as plt

class plotter_class:
   
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.fig=plt.figure(1)
        self.ax=self.fig.add_subplot(row,col,2)
        plt.draw()

    def plot_signal(self, pos, x, y, title, xLabel, yLabel, about):
        ax=self.fig.add_subplot(self.row,self.col,pos)
        line, =ax.plot(x,y,'o', label=about)
        ax.set_title(title)
        ax.set_xlabel(xLabel)
        ax.set_ylabel(yLabel)
        ax.grid(which='both', axis='both')
        ax.legend(loc='best')
        plt.draw()

    def plot_show(self):
        plt.show()

    def plot_draw(self,pause):
        plt.draw()
        plt.pause(pause)

