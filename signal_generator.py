import numpy as np

class signal_generator_class:
    def __init__(self):
        pass

    # funcion que recibe: fs frecuencia de sampleo, fo es la frec que quiero
    # para la senusoide A es la amplitud N el numero de muestras as tomar sim,
    # punto de simetria (conde esta el vertice
    def signal_triangular(self, fs, fo, A, N , sim):
        #inicializo para todos los samples que voy a tener
        tt = np.linspace(0, (N-1)/fs, N)
        ans=[0 for i in range(N)]
        for i in range(N):
            #calculo el porcentaje actual en funcion de i, y usando modulo para
            #ir repitiendo cuando llego a la fo
            percent=(tt[i]%(1/fo))/(1/fo) * 100
            #si me paso de lo pedido...
            if percent < sim:
                ans[i]=A/sim * percent
            else:
                ans[i]=A-(A/(100-sim) * (percent-sim))
        return ans, tt


    # funcion que recibe: fs frecuencia de sampleo, fo es la frec que quiero
    # para la senusoide A es la amplitud N el numero de muestras as tomar
    # cilco,  PWM en porcentaje
    def signal_quad(self, fs, fo, A, N , ciclo):
        #vector de N elementos, y aprovecho a cargarle la Amplitud negativa
        tt = np.linspace(0, (N-1)/fs, N)
        ans=[0 for i in range(N)]
        for i in range(N):
        #    #calculo para cada muestra en que parte del PWM estoy
            percent=(tt[i]%(1/fo))/(1/fo) * 100
            #si me paso de lo pedido...pongo el valor positivo.
            if percent < ciclo:
                ans[i]=A
        return ans, tt

    # funcion que recibe: fs frecuencia de sampleo, fo es la frec que quiero
    # para la senusoide A es la amplitud N el numero de muestras as tomar fase,
    # la fase en radianes
    def signal_sin(self, fs, fo, A, N , rad):
        #con esta magia greo un vector con N valores del seno de fo capturados
        #una distancia de 1/fs cada uno. Aplico %1 para que no arrastre error de pi a medida 
        #que el factor multiplicativo se hace mas grande.. como es periodica en 2*pi aprovecho eso
        tt = np.linspace(0, (N-1)/fs, N)
        ans =  A * np.sin( 2 * np.pi * fo * tt + rad)
        return ans, tt

    def signal_noise(self, fs, mean, deviation, N):
        tt =   [n/fs  for n in range(N)]
        ans = np.random.normal(mean, deviation, N )
        return ans, tt

