import matplotlib.pyplot as plt
import numpy as np
from plotter import *
from signal_generator import *

N=200
MAX_PHASE=10
MAX_FREC=10
sg= signal_generator_class()
pl= plotter_class(1,3)
for F in range(MAX_PHASE):
    plt.clf()
    pl.plot_signal ( 1 ,range(N) ,sg.signal_quad       (1009 ,10 ,10 ,N ,(F/MAX_PHASE)*100)     ,'cuadrada'   ,'samples' ,'amplitud' ,'señal cuadrada')
    pl.plot_signal ( 2 ,range(N) ,sg.signal_sin        (1009 ,10 ,10 ,N ,(F/MAX_PHASE)*2*np.pi) ,'senoidal'   ,'samples' ,'amplitud' ,'señal senoidal')
    pl.plot_signal ( 3 ,range(N) ,sg.signal_triangular (1009 ,10 ,10 ,N ,(F/MAX_PHASE)*100)     ,'triangular' ,'samples' ,'amplitud' ,'señal triangular')
    pl.plot_draw(0.1)
for F in range(MAX_FREC):
    F +=1
    plt.clf()
    pl.plot_signal ( 1 ,range(N) ,sg.signal_quad       (1009 ,F ,10 ,N ,50) ,'cuadrada'   ,'samples' ,'amplitud' ,'señal cuadrada')
    pl.plot_signal ( 2 ,range(N) ,sg.signal_sin        (1009 ,F ,10 ,N ,0)  ,'senoidal'   ,'samples' ,'amplitud' ,'señal senoidal')
    pl.plot_signal ( 3 ,range(N) ,sg.signal_triangular (1009 ,F ,10 ,N ,50) ,'triangular' ,'samples' ,'amplitud' ,'señal triangular')
    pl.plot_draw(0.1)
pl.plot_show()

