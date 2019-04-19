import matplotlib.pyplot as plt
import numpy as np
from plotter import *
from signal_generator import *
from dft import *

N  = 1024
fs = 1024
a0 = 1
p0 = 0
f0 = fs//4

dft_c  = dft_class              (     )
sg     = signal_generator_class (     )
pl     = plotter_class          ( 2,2 )
offset = [0,0.01,0.25,0.5]
graph  = 0;
ans    = [[0]*3 for i in range(4)]


for D in offset :
    signal ,time = sg.signal_sin ( fs ,f0+D ,a0 ,N ,p0)
    fft    ,freq = dft_c.abs     ( fs ,N  ,signal    );
    label=f"f0={f0} + {D} + Pcetral= {dft_c.power(fft,1024//4):.2f}"
    pl.stem_signal ( graph+1 ,freq[f0-10:f0+10] ,fft[f0-10:f0+10]  ,label ,'frecuencia','Pnormal.')
    ans[graph][0] = dft_c.power     ( fft ,1024//4   )
    ans[graph][1] = dft_c.power     ( fft ,1024//4+1 )
    ans[graph][2] = dft_c.power_sum ( fft ,1024//4   )
    graph+=1
#pl.plot_signal ( 5 ,time ,signal ,'seno %f hz' %f0 ,'tiempo'  ,'volts' ,trace='-' )
pl.plot_show()


