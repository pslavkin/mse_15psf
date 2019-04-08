import matplotlib.pyplot as plt
import numpy as np
from plotter import *
from signal_generator import *
from dft import *

N  = 1024
fs = 1024
a0 = 1       # Volts
p0 = 0  # radianes
f0 = fs//4

dft_c=dft_class()
sg= signal_generator_class()

pl= plotter_class(2,2)
offset=[0,0.01,0.25,0.5]
graph=0;
ans=[0 for i in range(5*3)]
for D in offset :
    signal ,time  = sg.signal_sin ( fs+D ,f0 ,a0 ,N ,p0 )
    fft    ,freq  = dft_c.abs ( fs+D ,N  ,signal    );
    #pl.plot_signal ( 1 ,time ,signal ,'seno %f hz' %f0 ,'tiempo'  ,'volts' ,trace='-' )
    label="f0=" + str(f0) + "+" + str(D) + " pot centro=" + str(round(dft_c.power(fft,1024//4),4))
    pl.stem_signal ( graph+1 ,freq[f0-10:f0+10] ,fft[f0-10:f0+10]  ,label ,'frecuencia' ,'normalizado'  )
    ans[0+graph*3]=dft_c.power   ( fft ,1024//4   )
    ans[1+graph*3]=dft_c.power   ( fft ,1024//4+1 )
    ans[2+graph*3]=dft_c.power_sum ( fft ,1024//4   )
    graph+=1

print (ans)
pl.plot_show()

tus_resultados = [ ['$ \lvert X(f_0) \lvert$' ,
    '$ \lvert X(f_0+1) \lvert $' ,
    '$ \sum_{i=F} \lvert X(f_i) \lvert ^2 $'] ,
    ['' ,'' ,'$F:f \neq f_0$'] ,
    [str ( round(ans[0] ,3 )) ,str(round(ans[1]  ,3)) ,str(round(ans[2]  ,3))] ,
    [str ( round(ans[3] ,3 )) ,str(round(ans[4]  ,3)) ,str(round(ans[5]  ,3))] ,
    [str ( round(ans[6] ,3 )) ,str(round(ans[7]  ,3)) ,str(round(ans[8]  ,3))] ,
    [str ( round(ans[9] ,3 )) ,str(round(ans[10] ,3)) ,str(round(ans[11] ,3))] ,
    ]

