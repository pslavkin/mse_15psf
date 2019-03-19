import matplotlib.pyplot as plt
import numpy as np
from plotter import *
from signal_generator import *

N  = 10
fs = 1000
a0 = 1       # Volts
p0 = np.pi/2 # radianes
f0 = fs/2    # Hz


sg= signal_generator_class()

f0=500
pl1= plotter_class(1,1)
ans,tt=sg.signal_sin(fs ,f0 ,a0 ,N , np.pi/3 )
pl1.plot_signal (1,tt,ans,'senoidal f0=%fhz' %f0 ,'tiempo' ,'a0' ,'senoidal')
pl1.plot_show()

pl1= plotter_class(2,2)
for f0 in range(5,21,5):
    ans,tt=sg.signal_sin(fs ,f0 ,a0 ,N ,0 )
    pl1.plot_signal (f0/5,tt,ans,'senoidal f0=%fhz' %f0 ,'tiempo' ,'a0' ,'senoidal')
pl1.plot_draw(1)

pl2= plotter_class(2,2)
for M in range(1,5,1):
    ans,tt=sg.signal_noise(fs, M ,2 ,N)
    pl2.plot_signal (M,tt,ans,'noise mean=%f0' %M ,'tiempo' ,'a0' ,'noise')
pl2.plot_draw(1)

pl3= plotter_class(2,2)
for f0 in range(5,21,5):
    ans,tt=sg.signal_triangular(fs, f0, a0, N, 75)
    pl3.plot_signal (f0/5,tt,ans,'triangular f0=%fhz' %f0 ,'tiempo' ,'a0' ,'triangular')
pl3.plot_draw(1)

pl4= plotter_class(2,2)
for F in range(5,21,5):
    ans,tt=sg.signal_quad(fs, F, a0, N, 25)
    pl4.plot_signal (F/5,tt,ans,'cuadrada F=%fhz' %F ,'tiempo' ,'a0' ,'cuadrada')
pl4.plot_draw(1)

#pl.plot_signal ( 2 ,range(N ) ,sg.signal_sin        (fs ,F        ,a0 ,N       ,0)       ,'senoidal F=%f' %F ,'tiempo' ,'a0' ,'señal senoidal')
#for F in range(MIN_FREC,MAX_FREC+1):
#    plt.clf()
#    pl.plot_signal ( 1 ,range(N ) ,sg.signal_quad       (fs ,F        ,a0 ,N       ,50)      ,'cuadrada'         ,'tiempo' ,'a0' ,'señal cuadrada')
#    pl.plot_signal ( 2 ,range(N ) ,sg.signal_sin        (fs ,F        ,a0 ,N       ,0)       ,'senoidal F=%f' %F ,'tiempo' ,'a0' ,'señal senoidal')
#    pl.plot_signal ( 3 ,range(N ) ,sg.signal_triangular (fs ,F        ,a0 ,N       ,50)      ,'triangular'       ,'tiempo' ,'a0' ,'señal triangular')
#    pl.plot_signal ( 4 ,range(N ) ,sg.signal_noise      (0  ,a0 ,N )      ,'noise' ,'tiempo' ,'a0'         ,'señal random')
#    pl.plot_draw(0.5)
#

#pl= plotter_class(1,1)
#for F in range(MIN_p0,MAX_p0):
#    ts = [i * 1/fs for i in range(N)]
#    plt.clf()
#    pl.plot_signal ( 1 ,ts ,sg.signal_quad       (fs ,10                     ,a0 ,N       ,(F/MAX_p0)*100)     ,'cuadrada'   ,'tiempo' ,'a0' ,'señal cuadrada')
#    pl.plot_signal ( 1 ,ts ,sg.signal_sin        (fs ,10                     ,a0 ,N       ,(F/MAX_p0)*2*np.pi) ,'senoidal'   ,'tiempo' ,'a0' ,'señal senoidal')
#    pl.plot_signal ( 1 ,ts ,sg.signal_triangular (fs ,10                     ,a0 ,N       ,(F/MAX_p0)*100)     ,'triangular' ,'tiempo' ,'a0' ,'señal triangular')
#    pl.plot_signal ( 1 ,ts ,sg.signal_noise      (0  ,(F/MAX_p0)*a0 ,N )      ,'noise' ,'tiempo'               ,'a0'   ,'señal random')
#    pl.plot_draw(0.1)
#pl.plot_show()

