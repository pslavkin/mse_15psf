import matplotlib.pyplot as plt
import numpy as np

# funcion que recibe:
# fs frecuencia de sampleo,
# fo es la frec que quiero para la senusoide
# A es la amplitud
# N el numero de muestras as tomar
# sim, punto de simetria (conde esta el vertice
def signal_triangular(fs, fo, A, N , sim):
    #inicializo para todos los samples que voy a tener
    ans=[0 for i in range(N)]
    for i in range(N):
        #calculo el porcentaje actual en funcion de i, y usando modulo para ir
        #repitiendo cuando llego a la fo
        percent=((i * 1/fs)%(1/fo))/(1/fo) * 100
        #si me paso de lo pedido...
        if percent < sim:
            ans[i]=A/sim * percent
        else:
            ans[i]=A-(A/(100-sim) * (percent-sim))
    return ans


# funcion que recibe:
# fs frecuencia de sampleo,
# fo es la frec que quiero para la senusoide
# A es la amplitud
# N el numero de muestras as tomar
# cilco,  PWM en porcentaje
def signal_quad(fs, fo, A, N , ciclo):
    #vector de N elementos, y aprovecho a cargarle la Amplitud negativa
    ans=[-A for i in range(N)]
    for i in range(N):
        percent=((i * 1/fs)%(1/fo))/(1/fo) * 100
        #si me paso de lo pedido...
        if percent < ciclo:
            ans[i]=A
    return ans

# funcion que recibe:
# fs frecuencia de sampleo,
# fo es la frec que quiero para la senusoide
# A es la amplitud
# N el numero de muestras as tomar
# fase, la fase en radianes
def signal_sin(fs, fo, A, N , rad):
    #con esta magia greo un vector con N valores del seno de fo capturados a
    #una distancia de 1/fs cada uno
    ans = [A * np.sin( 2 * np.pi * fo * 1/fs * n + rad ) for n in range(N)]
    return ans




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
N=1000
#plt.plot(range(N),signal_sin(1000,100,10,N, 0),'o')
plt.plot(range(N),signal_quad(1000,10,10,N, 35),'x')
#plt.plot(range(N),signal_triangular(1000,10,10,N, 35),'o')
plt.show()

