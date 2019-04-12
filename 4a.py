import matplotlib.pyplot as plt
import numpy as np
from plotter import *
from signal_generator import *
from dft import *

N  = 1024
fs = 1024
a0 = 1
f0 = 9*fs//N
f1 = 8*fs//N

dft_c  = dft_class              (     )
sg     = signal_generator_class (     )
pl     = plotter_class          ( 2,1 )
ans    = np.zeros(3)

signal  ,time  = sg.signal_sin_cycles ( fs ,f0 ,a0 ,N ,0 ,1)
signal2 ,time  = sg.signal_sin_cycles ( fs ,f1 ,a0 ,N ,2 ,1)
signal=signal+signal2
z=np.zeros(10000)
N+=10000
signal=np.concatenate((signal,z),axis=0)

fft    ,freq = dft_c.abs            ( fs ,N  ,signal      );
pl.plot_signal ( 1 ,time ,signal  ,'seno %.2f hz N=%d' %((f0),N) ,'tiempo'  ,'volts' ,trace='-' )
ans[0] = dft_c.power_total ( fs, fft ,f0 )
ans[1] = dft_c.power_bin   ( fs, fft ,f0 )
ans[2] = dft_c.max_bin     ( fs, fft     )

pl.stem_signal ( 2 ,freq,fft,f"f0={f0}",'frecuencia','Pnormal',f"Ptot={ans[0]:.2f}, Pbin={ans[1]:.2f}, bin_max={ans[2]:.2f}",center=ans[2],zoom=N//20)
pl.plot_show()


