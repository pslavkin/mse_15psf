import matplotlib.pyplot as plt
import numpy as np
from plotter import *
from signal_generator import *
from scipy import signal as sig
import zplane as zp

float_formatter = lambda x: f"{x:.2f}"
np.set_printoptions(formatter={'float_kind':float_formatter})

pl = plotter_class ( 2,2 )

b = np.array([1/3,1/3,1/3])
a = np.array([1,0,0])

ww  ,hh = sig.freqz(b,a);
pl.plot_signal ( 1 ,ww ,np.abs(hh)   ,f'Respuesta en frec {b}' ,'F=2*pi*f/fs' ,'Modulo [veces]'  ,trace='-' )
pl.plot_signal ( 3 ,ww ,np.angle(hh) ,'Respuesta de fase'      ,'F=2*pi*f/fs' ,'Fase [radianes]' ,trace='-' )
pl.zplane(b,a,4)
pl.plot_show()

