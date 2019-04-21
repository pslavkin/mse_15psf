import numpy as np
from numpy import convolve as np_convolve
from scipy.signal import fftconvolve, lfilter, firwin
from scipy.signal import convolve as sig_convolve
from scipy.ndimage import convolve1d

class filter_class:

    def __init__(self):
        pass

    def qrs2ecg(self,qrs,ecg):
        det=np.zeros(ecg.size)
        j=0
        for i in range(ecg.size):
            if qrs[j]==i :
                det[i]=5000
                j+=1
                if j>=qrs.size:
                    break
        return det

    def fir(self,x,h):
        y=np.zeros(x.size)
        for n in range(x.size):
            for k in range(n-h.size+1,n+1):
#                if (n-k)<(h.size):
                y[n]=y[n]+x[k]*h[n-k]
#        y=lfilter(h,[1.0],x)
        return y
