import  matplotlib.pyplot as plt
import  numpy as np
from    plotter import *
from    signal_generator import *
import  scipy.io
from    filter import *
from    dft import *

fs = 1000

sg          = signal_generator_class()
pl          = plotter_class          ( 3,2 )
f           = filter_class           (     )
dft_c       = dft_class              (     )

mat                = scipy.io.loadmat('file.mat')
ecg_lead           = mat[ 'ecg_lead'           ]
qrs_pattern1       = mat[ 'qrs_pattern1'       ]
heartbeat_pattern1 = mat[ 'heartbeat_pattern1' ]
heartbeat_pattern2 = mat[ 'heartbeat_pattern2' ]
qrs_detections     = mat[ 'qrs_detections'     ]

lopass             = np.load("lopass_fir.npz")['ba'][0]
hipass             = np.load("hipass_fir.npz")['ba'][0]



zonas_sin_interf = (
        np.array([5, 5.2]) *60*fs, # minutos a muestras
        [4000, 5500], # muestras
        [10e3, 11e3], # muestras
        )

ecg_lead=np.append(ecg_lead[int(12.0*60*fs):int(13.00*60*fs)],ecg_lead[int(15.0*60*fs):int(15.2*60*fs)])
ecg_lead=ecg_lead[:ecg_lead.size].flatten()

t=np.linspace ( 0 ,ecg_lead.size ,ecg_lead.size )
pl.plot_signal( 1 ,t ,ecg_lead ,'ecg_lead' ,'time [msec]' ,'mvolt' ,trace='-' )

fft    ,freq  = dft_c.abs ( fs ,ecg_lead.size  ,ecg_lead[:].flatten( ));
pl.stem_signal ( 2 ,freq ,fft ,'fft' ,'frecuencia','Pnormal.',center=25/(fs/(fft.size*2)),zoom=25/(fs/(fft.size*2)) )

y = f.fir       ( ecg_lead,lopass )
t = np.linspace ( 0,y.size,y.size )
pl.plot_signal  ( 3 ,t[:t.size-lopass.size//2],y[lopass.size//2:] ,'fir' , 'time' ,'mvolt'  ,trace='-' )

fft    ,freq  = dft_c.abs( fs ,y.size  ,y    );
pl.stem_signal ( 4 ,freq ,fft ,'fft y' ,'frecuencia','Pnormal.',center=25/(fs/(fft.size*2)),zoom=25/(fs/(fft.size*2)))

y = f.fir       ( y,hipass )
t = np.linspace ( 0,y.size,y.size )
pl.plot_signal  ( 5 ,t[:t.size-hipass.size//2],y[hipass.size//2:]   ,'fir' , 'time' ,'mvolt'  ,trace='-' )

fft    ,freq  = dft_c.abs( fs ,y.size  ,y    );
pl.stem_signal ( 6 ,freq ,fft ,'fft y' ,'frecuencia','Pnormal',center=25/(fs/(fft.size*2)),zoom=25/(fs/(fft.size*2)))

pl          = plotter_class          ( 2,1 )
pl.plot_signal  ( 1 ,t,y ,'fir' , 'time' ,'mvolt'  ,trace='-' ,center=5000, zoom=2000)
pl.plot_signal  ( 2 ,t ,ecg_lead ,'ecg_lead' ,'time [msec]' ,'mvolt' ,trace='-',center=5000, zoom=2000 )                

pl.plot_show() 
