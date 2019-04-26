import  matplotlib.pyplot as plt
import  numpy as np
from    plotter import *
from    signal_generator import *
import  scipy.io
from    filter import *
from    dft import *

pl          = plotter_class          ( 2,2 )
f           = filter_class           (     )
dft_c       = dft_class              (     )

fs=1000

lopass             = np.load("lopass_iir.npz")['ba']
hipass             = np.load("hipass_iir.npz")['ba']

#t=np.linspace ( 0 ,lopass.size ,lopass.size )
#pl.plot_signal( 1 ,t ,lopass ,'h(n) lopass FIR ' ,'time [msec]' ,'mvolt' ,trace='-' )
#lopass=np.append(lopass,np.zeros(5000))
#fft    ,freq  = dft_c.abs ( fs ,lopass.size  ,lopass);
#pl.stem_signal ( 2 ,freq ,fft ,'H(f) lopass FIR' ,'frecuencia','Pnormal.',center=40/(fs/(fft.size*2)),zoom=10/(fs/(fft.size*2)) )
#
#t=np.linspace ( 0 ,hipass.size ,hipass.size )
#pl.plot_signal( 3 ,t ,hipass ,'h(n) hipass FIR' ,'time [msec]' ,'mvolt' ,trace='-' )
#hipass=np.append(hipass,np.zeros(30000))
#fft    ,freq  = dft_c.abs ( fs ,hipass.size  ,hipass);
#pl.stem_signal ( 4 ,freq ,fft ,'H(f) hipass FIR' ,'frecuencia','Pnormal.',center=2/(fs/(fft.size*2)),zoom=2/(fs/(fft.size*2)) )

t=np.linspace ( 0 ,lopass[0].size ,lopass[0].size )
z=np.zeros (5000)
z[0]=1

y = f.iir       ( z,lopass[0],lopass[1] )
t = np.linspace ( 0,y.size,y.size )
pl.plot_signal  ( 1 ,t,y,' h(n) lopass IIR orden )' , 'time' ,'mvolt'  ,trace='-',center=y.size// 50,zoom=y.size// 50)
fft    ,freq  = dft_c.abs ( fs ,y.size  ,y);
pl.plot_signal  ( 2 ,freq ,20*np.log10(np.abs(fft)) ,'H(f) lopass IIR' ,'frecuencia','Pnormal [db]',trace='-',center= 30/(fs/(fft.size*2)),zoom= 30/(fs/(fft.size*2)) ) #

t=np.linspace ( 0 ,hipass[0].size ,hipass[0].size )
z=np.zeros (500000)
z[0]=1

y = f.iir       ( z,hipass[0],hipass[1] )
t = np.linspace ( 0,y.size,y.size )
pl.plot_signal  ( 3 ,t,y,' h(n) hipass IIR orden )' , 'time' ,'mvolt'  ,trace='-',center= 5,zoom= 5)
fft    ,freq  = dft_c.abs ( fs ,y.size  ,y);
pl.plot_signal  ( 4 ,freq ,20*np.log10(np.abs(fft)) ,'H(f) hipass IIR' ,'frecuencia','Pnormal [db]',trace='-',center= 0.20*y.size/(fs/2),zoom= 0.20*y.size/(fs/2)) #
pl.plot_show() 
