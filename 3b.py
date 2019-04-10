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

D=0.5
dft_c  = dft_class              (     )
sg     = signal_generator_class (     )
pl     = plotter_class          ( 3,2 )
ZZeros = [N//10,N,N*10]
graph  = 0;
ans    = [[0]*3 for i in ZZeros]


for zz in ZZeros :
    signal ,time = sg.signal_sin_zero_padded ( fs ,f0+D ,a0 ,N ,p0, zz)
    fft    ,freq = dft_c.abs( fs ,N+zz  ,signal    );
    pl.plot_signal ( graph*2+1 ,time ,signal ,'seno %.2f hz N=%d padd=%d ' %((f0+D),N+zz,zz) ,'tiempo'  ,'volts' ,trace='-' )
    label=f"f0={f0} + {D} + Pcentral= {dft_c.power_bin(fs,fft,f0+D):.2f}"
    bin    = int((f0*(N+zz))//fs)
    offset = (N+zz)//200
    pl.stem_signal ( graph*2+2 ,freq[bin-offset:bin+offset+1],fft[bin-offset:bin+offset+1],label ,'frecuencia','Pnormal.')
    ans[graph][0] = dft_c.power_bin      ( fs, fft ,f0+D )
    ans[graph][1] = dft_c.power_adjacent ( fs, fft ,f0+D )
    ans[graph][2] = dft_c.power_sum      ( fs, fft ,f0+D )
    graph+=1
pl.plot_show()


