import matplotlib.pyplot as plt
import numpy as np



def sin_signal(fs, fo, A, N , fase):
    aux = [A * np.sin( 2 * np.pi * fo * 1/fs * n + fase ) for n in range(N)]
    plt.plot(range(N), aux, 'o')
    plt.show()
    return aux





def my_testbench( sig_type ):
    fs = 1000.0 # frecuencia de muestreo (Hz)",
    N  = 1000   # cantidad de muestras",
    df = fs/N   # resolución espectral",
    tt = np.linspace(0, (N-1)*fs, N).flatten()
    ff = np.linspace(0, (N-1)*df, N).flatten()
    x=np.zeros(N)
#    x = np.array([], dtype=np.float)
#    x.reshape(N,0)


#    for this_freq in sig_type['frecuencia']:
#        # prestar atención que las tuplas dentro de los diccionarios también
#        # pueden direccionarse mediante \"ii\"\n",
    aux = 2 * np.sin( 2*np.pi*ff/N + 0 )
    print(ff)
#        # para concatenar horizontalmente es necesario cuidar que tengan iguales FILAS\n",
#        x = np.hstack([x, aux.reshape(N,1)] )
#        ii += 1
#

    plt.figure(1)
    plt.plot(ff/N, aux, 'o')

#    line_hdls = plt.plot(tt, x)
#    plt.title('Señal: ' + sig_type['tipo'] )
#    plt.xlabel('tiempo [segundos]')
#    plt.ylabel('Amplitud [V]')
#    plt.grid(which='both', axis='both')
#    axes_hdl = plt.gca()
#    axes_hdl.legend(line_hdls, sig_type['descripcion'], loc='upper right'  )
    plt.show()

#    sig_props = { 'tipo': 'ruido', 'varianza': (1, 2, 1) }                                          # Uso de tuplas para las frecuencias \n",
#    sig_props['descripcion'] = [ '$\\sigma^2$ = ' + str(a_var) for a_var in sig_props['varianza'] ] # Invocamos a nuestro testbench exclusivamente: \n",
sin_signal(1000,100,10,100, 0)
