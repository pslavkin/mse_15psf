import numpy as np
import scipy.fftpack as sc 

class dft_class:
    def __init__(self):
        pass

    def dft_abs(self, fs, N, signal):
        freq = np.linspace(0, fs, N)
        return (2/N)*np.abs(sc.fft(signal))[:N//2], freq[:N//2]


    def dft_full(self, fs, N, signal):
        freq = np.linspace(0, fs, N)
        return (2/N)*np.abs(sc.fft(signal))[:N//1], freq[:N//1]
