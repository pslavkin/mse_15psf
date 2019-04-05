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
a0 = 1	     # Volts
p0 = 0	# radianes
f0 = fs//4

dft_c=dft_class()
sg= signal_generator_class()

pl4= plotter_class(2,2)
offset=[0,0.01,0.25,0.5]
graph=0;
ans=[0 for i in range(5*3)]
for D in offset :
    signal ,time  = sg.signal_sin ( fs+D ,f0 ,a0 ,N ,p0 )
    fft    ,freq  = dft_c.abs ( fs+D ,N  ,signal    );
    #pl4.plot_signal ( 1 ,time ,signal ,'seno %f hz' %f0 ,'tiempo'  ,'volts' ,trace='-' )
    label="f0=" + str(f0) + "+" + str(D) + " pot centro=" + str(round(dft_c.power(fft,1024//4),4))
    pl4.stem_signal ( graph+1 ,freq[f0-10:f0+10] ,fft[f0-10:f0+10]  ,label ,'frecuencia' ,'normalizado'	 )
    ans[0+graph*3]=dft_c.power	 ( fft ,1024//4   )
    ans[1+graph*3]=dft_c.power	 ( fft ,1024//4+1 )
    ans[2+graph*3]=dft_c.power_sum ( fft ,1024//4   )
#    print (dft_c.power(fft,1024//4))
#    print (dft_c.power_sum(fft,1024//4))
    graph+=1

print (ans)
pl4.plot_show()


tus_resultados = [ ['$ \lvert X(f_0) \lvert$' ,
    '$ \lvert X(f_0+1) \lvert $' ,
    '$ \sum_{i=F} \lvert X(f_i) \lvert ^2 $'] ,
    ['' ,'' ,'$F:f \neq f_0$'] ,
    [str ( ans[0] ) ,str(ans[1])  ,str(ans[2])]  ,
    [str ( ans[3] ) ,str(ans[4])  ,str(ans[5])]  ,
    [str ( ans[6] ) ,str(ans[7])  ,str(ans[8])]  ,
    [str ( ans[9] ) ,str(ans[10]) ,str(ans[11])] ,
    ]

##
#a0 = 1       # Volts
#p0 = 0 # radianes
#f0 = 100   # Hz
#
#signal ,time  = sg.signal_sin ( fs ,f0 ,a0 ,N ,p0 )
#fft	,freq  = dft_c.dft_abs ( fs ,N	,signal    );
#pl4.plot_signal ( 3 ,time ,signal ,'seno %f hz' %f0 ,'tiempo'	   ,'volts' ,trace='-' )
#pl4.stem_signal ( 4 ,freq ,fft    ,'dft'  ,'frecuencia' ,'normalizado'      )
#
#
#a0 = 1       # Volts
#p0 = 10 # radianes
#f0 = 10   # Hz
#
#signal ,time  = sg.signal_quad ( fs ,f0 ,a0 ,N ,p0 )
#fft	,freq  = dft_c.dft_abs ( fs ,N	,signal    );
#pl4.plot_signal ( 5 ,time ,signal ,'cuadrada %f hz' %f0 ,'tiempo'     ,'volts' ,trace='-' )
#pl4.stem_signal ( 6 ,freq ,fft    ,'dft'  ,'frecuencia' ,'normalizado'      )
#pl4.plot_show()
#
#
#
