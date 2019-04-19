import matplotlib.pyplot as plt
import numpy as np
from plotter import *
from signal_generator import *
from scipy import signal as sig
import zplane as zp
import scipy.io

float_formatter = lambda x: f"{x:.2f}"
np.set_printoptions(formatter={'float_kind':float_formatter})

pl = plotter_class ( 3,1 )


mat = scipy.io.loadmat('file.mat')
ecg_lead           = mat['ecg_lead']
print(ecg_lead)
qrs_pattern1       = mat['qrs_pattern1']
heartbeat_pattern1 = mat['heartbeat_pattern1']
heartbeat_pattern2 = mat['heartbeat_pattern2']
qrs_detections     = mat['qrs_detections']

t=np.linspace(0,ecg_lead.size,ecg_lead.size)
pl.plot_signal(1,t/1000 ,ecg_lead   ,'ecg_lead' ,'time [sec]' ,'mVolt'  ,trace='-' )

det=np.zeros(ecg_lead.size)
j=0
for i in range(ecg_lead.size):
    if qrs_detections[j]==i :
        det[i]=2000
        j+=1
        if j>=qrs_detections.size:
            break

t=np.linspace(0,ecg_lead.size,ecg_lead.size)
pl.plot_signal( 1 ,t/1000 ,det   ,'ecg_lead' ,'time [sec]' ,'mVolt'  ,trace='-' )

t=np.linspace(0,heartbeat_pattern1.size,heartbeat_pattern1.size)
pl.plot_signal ( 2 ,t/1000 ,heartbeat_pattern1   ,'heartbeat_pattern1' ,'time [sec]' ,'mVolt'  ,trace='-' )

t=np.linspace(0,heartbeat_pattern2.size,heartbeat_pattern2.size)
pl.plot_signal ( 3 ,t/1000 ,heartbeat_pattern2   ,'heartbeat_pattern2' ,'time [sec]' ,'mVolt'  ,trace='-' )

pl.plot_show()


