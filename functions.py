import matplotlib.pyplot as plt
import numpy as np

def verificar_hora():
    '''Esta funcion pide la hora y verifica que este en el rango entre 0 y 23 y la retorna '''
    numero = input('Ingrese la hora del dia: ') # recibe la hora como str
    if not numero.isnumeric() == True: # si el str no es solo numerico alerta de error
        return -1
    else:
        numero = int(numero)
        if numero >= 0 and numero <= 23:
            return numero
        else:
            return -1

def verificar_minutos():
    '''Esta funcion pide el minuto de la hora y verifique que este entre 0 y 59 y lo retorna'''
    numero = input('Ingrese el minuto de la hora: ') # recibe el minuto como str
    if not numero.isnumeric() == True: # si el str no es solo numerico alerta de error
        return -1
    else:
        numero = int(numero)
        if numero >= 0 and numero <= 59:
            return numero
        else:
            return -1

def verificar_latitud():
    '''Esta funcion pide la latitud de la tierra en grados y la retorna en radianes,
    los limites son 90 y -90'''
    numero = input('Ingrese la latitud del lugar que desea en grados: ') # recibe el minuto como str
    numero1 = numero
    numero1 = numero1.replace('-', '', 1)
    numero1 = numero1.replace('.', '', 1)
    if numero1.isnumeric() == False: # si el str no es solo numerico alerta de error
        return -100
    else:
        numero = float(numero)
        if numero >= -90 and numero <= 90:
            return numero
        else:
            return -100

def hora_min():
    '''Esta funcion usa las funciones de hora y minuto y retorna sus valores numeros y en string'''
    hora = verificar_hora()
    while hora == -1:
        print('hora incorrecta, vuelva a intentarlo...')
        hora = verificar_hora()

    minuto = verificar_minutos()
    while minuto == -1:
        print('Minuto incorrecto, vuelva a intentarlo...')
        minuto = verificar_minutos()
    hora_str = f'{hora}:{minuto}'
    print(f'La hora es {hora}h{minuto}m')
    return hora + minuto / 60, hora_str
   
def latitud():
    '''Esta funcion usa la funcion de verificar latitud y la retorna cuando se ingresa una valida'''
    lat = verificar_latitud()
    while lat == -100:
        print('Latitud incorrecta, vuelva a intentarlo...')
        lat = verificar_latitud()
    print(f'La latitud es {lat}')
    return (lat * np.pi) / 180

def analema(h):
    '''Esta funcion recibe la hora, calcula la ecuacion del tiempo y la grafica y retona los 
    valores de la desviacion angular y x que esta en funcion de N y h '''
    N = np.arange(1, 366)
    x = (2 * np.pi / 365) * (N - 1 + ((h - 12) / 24))

    fx =  229.18 * (0.000075 + 0.001868 * np.cos(x) - 0.032077*np.sin(x) - 0.014615 
    * np.cos(2 * x) - 0.040849 *np.sin(2 * x))

    plt.plot(fx, 'black',  [80, 80], [-20, 20], 'orange', [172, 172], [-20, 20],'blue', 
    [265, 265], [-20, 20], 'pink', [355, 355], [-20, 20],'g', linewidth = 3, )

    plt.xlabel('Año 2022')
    plt.ylabel('Minutos')
    plt.title('Analema Solar')
    plt.xlim(0, 365)
    plt.ylim(-20, 20)
    plt.legend(['Ecuacion del tiempo', 'Equinoccio de primavera',
    'Solsticio de verano', 'Equinoccio de otoño', 'Solsticio de invierno'])
    plt.grid()
    plt.show()
    y = fx * (15 / 60)
    return x, y

def declinacion(lat, x, hora_str, y):
    '''Esta funcion calcula y grafica la declinacion solar, y a partir de los parametros recibidos y
    calculados procede a calcular y graficar la altitud del sol dependiento la desviacion angular
    y la latitud '''
    declinacion_diaria = 0.006918 - 0.399912 * np.cos(x) + 0.070257* np.sin(x) - 0.006758* np.cos(2 * x)
    + 0.000907 * np.sin(2 * x) - 0.002697 * np.cos(3 * x) + 0.001480* np.sin(3 * x)

    a = -(lat - declinacion_diaria) * (180 / np.pi) 
    plt.plot(y, a, 'b', linewidth = 3)
    plt.xlabel('Angulo [ γ ]')
    plt.ylabel('Altitud [ α ]')
    plt.title(['Analema Solar', f'{hora_str}', f'λ = {round(lat * 180 / np.pi, 2)}°'])
    plt.grid()
    plt.show()
    plt.show()