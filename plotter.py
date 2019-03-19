import matplotlib.pyplot as plt

class plotter_class:

    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.fig=plt.figure(figsize=( 10, 7))
        self.ax1=self.fig.add_subplot(row,col,1)
        plt.tight_layout(pad=4, w_pad=1, h_pad=6)
        plt.draw()

    def plot_signal(self, pos, x, y, title, xLabel, yLabel, about):
        ax=self.fig.add_subplot(self.row,self.col,pos)
        line, =ax.plot(x,y,'-')#, label=about)
        ax.set_title(title)
        ax.set_xlabel(xLabel)
        ax.set_ylabel(yLabel)
        ax.grid(which='both', axis='both')
#        ax.legend(loc='best')
        plt.draw()

    def plot_show(self):
        plt.show()

    def plot_show(self):
        plt.show()

    def plot_draw(self,pause):
        plt.draw()
        plt.pause(pause)

    def plot_close(self):
        plt.close()


