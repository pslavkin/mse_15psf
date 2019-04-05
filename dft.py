import numpy as np
import scipy.fftpack as sc 

class dft_class:
    def __init__(self):
        pass

    def abs(self, fs, N, signal):
        freq = np.linspace(0, fs, N)
        return (2/N)*np.abs(sc.fft(signal))[:N//2], freq[:N//2]


    def full(self, fs, N, signal):
        freq = np.linspace(0, fs, N)
        return (1/N)*np.abs(sc.fft(signal))[:N//1], freq[:N//1]

    def power(self, signal,k):
        return np.abs(signal[k])

    def power_sum(self, signal,f0):
        ans=0.0
        for i in signal:
            ans+=i**2;
        return ans-(signal[f0]**2)

