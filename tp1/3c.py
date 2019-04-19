import matplotlib.pyplot as plt
import numpy as np
from plotter import *
from signal_generator import *
from dft import *

N  = 1024
fs = 1024
a0 = 1
p0 = 0
f0 = fs//4

D=0.5
dft_c  = dft_class              (     )
sg     = signal_generator_class (     )
ZZeros = [N//10,N,N*10]
graph  = 0;
ans    = np.zeros(3)


for zz in ZZeros :
    signal ,time  = sg.signal_sin_zero_padded ( fs ,f0+D ,a0 ,N ,p0, zz)
    fft    ,freq  = dft_c.abs( fs ,N+zz  ,signal    );
    ans[graph]    = np.abs((dft_c.max_bin(fs, fft)-(f0+D)))*100/(f0+D)
    graph        += 1

print(ans)



