import  matplotlib.pyplot as plt
import  numpy as np
from    plotter import *
from    signal_generator import *
from    scipy import signal as sig
import  zplane as zp
import  scipy.io
import  filter

float_formatter = lambda x: f"{x:.2f}"
np.set_printoptions(formatter={'float_kind':float_formatter})

pl = plotter_class ( 2,2 )


mat                = scipy.io.loadmat('file.mat')
ecg_lead           = mat['ecg_lead']
qrs_pattern1       = mat['qrs_pattern1']
heartbeat_pattern1 = mat['heartbeat_pattern1']
heartbeat_pattern2 = mat['heartbeat_pattern2']
qrs_detections     = mat['qrs_detections']

t=np.linspace  ( 0,ecg_lead.size,ecg_lead.size)
pl.plot_signal ( 1,t/1000 ,ecg_lead   ,'ecg_lead' ,'time [sec]' ,'mVolt'  ,trace='-' )

t=np.linspace  ( 0,ecg_lead.size,ecg_lead.size)
pl.plot_signal ( 2,t/1000 ,ecg_lead   ,'' ,'time [sec]' ,'mVolt'  ,trace='-', center=437000, zoom=3000)

t=np.linspace  ( 0,ecg_lead.size,ecg_lead.size)
pl.plot_signal ( 2 ,t/1000 , filter.qrs2ecg(qrs_detections,ecg_lead)  ,'ecg_lead zoom' ,'time [sec]' ,'mVolt'  ,trace='-', center= 437000,zoom= 3000 )

t=np.linspace  ( 0,heartbeat_pattern1.size,heartbeat_pattern1.size)
pl.plot_signal ( 3 ,t/1000 ,heartbeat_pattern1   ,'heartbeat_pattern1' ,'time [sec]' ,'mVolt'  ,trace='-' )

t=np.linspace  ( 0,heartbeat_pattern2.size,heartbeat_pattern2.size)
pl.plot_signal ( 4 ,t/1000 ,heartbeat_pattern2   ,'heartbeat_pattern2' ,'time [sec]' ,'mvolt'  ,trace='-' )

pl.plot_show()


