from functions import *

def main():
    '''Funcion principal para el calculo y graficacion de la ecuacion del tiempo, y la altitud 
    maxima del sol, usa las funciones de la libreria functions'''
    lat = latitud()
    h, hora_str = hora_min()
    x, y = analema(h)
    declinacion(lat, x, hora_str, y)
    
if __name__ == '__main__':
    main()