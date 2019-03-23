import matplotlib.pyplot as plt
import numpy as np
from plotter import *
from signal_generator import *
from dft import *




#f0=500
#pl1= plotter_class(1,1)
#ans,tt=sg.signal_sin(fs ,f0 ,a0 ,N , np.pi/3 )
#pl1.plot_signal (1,tt,ans,'senoidal f0=%fhz' %f0 ,'tiempo' ,'a0',trace='-')
#pl1.plot_show()
#
#pl1= plotter_class(2,2)
#for f0 in range(5,21,5):
#    ans,tt=sg.signal_sin(fs ,f0 ,a0 ,N ,0 )
#    pl1.plot_signal (f0/5,tt,ans,'senoidal f0=%fhz' %f0 ,'tiempo' ,'a0')
#pl1.plot_draw(1)
#
#pl2= plotter_class(2,2)
#for M in range(1,5,1):
#    ans,tt=sg.signal_noise(fs, M ,2 ,N)
#    pl2.plot_signal (M,tt,ans,'noise mean=%f0' %M ,'tiempo' ,'a0')
#pl2.plot_draw(1)
#
#pl3= plotter_class(2,2)
#for f0 in range(5,21,5):
#    ans,tt=sg.signal_triangular(fs, f0, a0, N, 75)
#    pl3.plot_signal (f0/5,tt,ans,'triangular f0=%fhz' %f0 ,'tiempo' ,'a0')
#pl3.plot_draw(1)
#
#pl4= plotter_class(2,2)
#for F in range(5,21,5):
#    ans,tt=sg.signal_quad(fs, F, a0, N, 25)
#    pl4.plot_signal (F/5,tt,ans,'cuadrada F=%fhz' %F ,'tiempo' ,'a0')
#pl4.plot_draw(1)

N  = 1024
fs = 1024
a0 = 1       # Volts
p0 = 5 # radianes
f0 = 10.0   # Hz

dft_c=dft_class()
sg= signal_generator_class()

pl4= plotter_class(2,1)
signal ,time  = sg.signal_quad ( fs ,f0 ,a0 ,N ,p0 )
fft    ,freq  = dft_c.dft_full ( fs ,N  ,signal    );
pl4.plot_signal (1 ,time ,signal ,'seno' ,'tiempo'     ,'a0' ,trace='-')
#pl4.plot_signal (2 ,freq ,fft    ,'fft'  ,'frecuencia' ,'a0' ,trace='-')
pl4.stem_signal(2,freq,fft,'fft'  ,'frecuencia' ,'a0')

pl4.plot_show()




