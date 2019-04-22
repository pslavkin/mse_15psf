import  matplotlib.pyplot as plt
import  numpy as np
from    plotter import *
from    signal_generator import *
from    scipy import signal as sig
import  zplane as zp
import  scipy.io
from    filter import *
from    dft import *

float_formatter = lambda x: f"{x:.2f}"
np.set_printoptions(formatter={'float_kind':float_formatter})

N  = 10000
fs = 1000

sg    = signal_generator_class (     )
pl    = plotter_class          ( 2,2 )
f     = filter_class           (     )
dft_c = dft_class              (     )

mat                = scipy.io.loadmat('file.mat')
ecg_lead           = mat[ 'ecg_lead'           ]
qrs_pattern1       = mat[ 'qrs_pattern1'       ]
heartbeat_pattern1 = mat[ 'heartbeat_pattern1' ]
heartbeat_pattern2 = mat[ 'heartbeat_pattern2' ]
qrs_detections     = mat[ 'qrs_detections'     ]

ecg_lead=ecg_lead[12*60*fs:int(12.4*60*fs)]
out=0
for i in range(100):
    signal ,time = sg.signal_sin ( fs ,40+i ,1 ,N ,0)
    out=out+signal
#ecg_lead=out
#ecg_lead=heartbeat_pattern1
z=np.zeros(1000)
ecg_lead=np.append(ecg_lead,z)
t=np.linspace ( 0 ,ecg_lead.size ,ecg_lead.size )
pl.plot_signal ( 1 ,t ,ecg_lead ,'ecg_lead' ,'time [msec]' ,'mvolt' ,trace='-' )

fft    ,freq  = dft_c.abs ( fs ,ecg_lead.size  ,ecg_lead[:].flatten( ));
pl.stem_signal ( 2 ,freq ,fft ,'fft' ,'frecuencia','Pnormal.',fft.size/2,zoom=fft.size/10 )

#t=np.linspace  ( 0,heartbeat_pattern1.size,heartbeat_pattern1.size)
#pl.plot_signal ( 3 ,t/1000 ,heartbeat_pattern1   ,'heartbeat_pattern1' ,'time [sec]' ,'mvolt'  ,trace='-' )

#h = np.array    ( [1/3,1/3,1/3] )

transfer=np.load("lopass.npz")
h=transfer['ba'][0]
y = f.fir       ( ecg_lead,h  )
t = np.linspace ( 0,y.size,y.size       )
pl.plot_signal  ( 1 ,t[:t.size-h.size//2],y[h.size//2:]   ,'fir' , 'time' ,'mvolt'  ,trace='-' )

fft    ,freq  = dft_c.abs( fs ,y.size  ,y    );
pl.stem_signal ( 4 ,freq ,fft ,'fft y' ,'frecuencia','Pnormal.')

pl.plot_show()
