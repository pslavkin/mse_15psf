import matplotlib.pyplot as plt
import numpy as np
from plotter import *
from signal_generator import *
from dft import *
from scipy import signal

N  = 1024
fs = 40000
a0 = 1
p0 = 0
f0 = 500


avg = 1000


dft_c=dft_class()
sg= signal_generator_class()

pl4= plotter_class(2,2)
signa ,time  = sg.signal_sin ( fs ,f0 ,a0 ,N ,p0 )
noise  ,time  = sg.signal_noise ( fs ,0 ,0.1 ,N )
fft    ,freq  = dft_c.abs ( fs ,N  ,signa    );
pl4.plot_signal ( 1 ,time ,signa+noise ,'seno %f hz' %f0 ,'tiempo'     ,'volts' ,trace='-' )

pl4.stem_signal ( 2 ,freq ,fft    ,'dft'            ,'frecuencia' ,'normalizado')

#print (ans)
#pl4.plot_show()

h=[1/avg for i in range(avg)]
print(h)
print(signa)

y = signal.convolve(signa+noise,h)
pl4.plot_signal ( 3 ,time[:1000] ,y[:1000],'seno %f hz' %f0 ,'tiempo'     ,'volts' ,trace='-' )
pl4.plot_show()


