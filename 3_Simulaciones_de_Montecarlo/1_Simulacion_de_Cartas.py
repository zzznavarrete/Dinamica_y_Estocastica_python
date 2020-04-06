

"""
    Simulación de juego de cartas

    ¿Cómo son las barajas?
    Tienen 4 tipos (corazones, treboles, pica y diamante)
    Van desde el 'A' hasta el '10' y luego 3 cartas 'J', 'Q', 'K'.

    Nosotros primero tenemos que construir esta baraja y de esta baraja vamos a sacar cartas
    y vamos a ver cual es el resultado de las manos que obtendremos de las barajas
    para poder entender cuales son nuestras probabilidades dentro del juego para poder saber
    si debemos apostar o no.

"""

import random
import collections

# En python, por convención las constantes se declaran en mayúscula.
TIPOS = ['pica', 'corazon', 'rombo', 'trebol']
VALORES = ['A', '2', '3', '4', '5', '6', '7','8','9','10','J', 'Q', 'K']

def crear_baraja():
    barajas = []
    for tipo in TIPOS:
        for valor in VALORES:
            # Tuplas de tipo y valor
            barajas.append((tipo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano


def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            # Como el valor del tipo de la carta está en el índice 0, obtenemos el número de la carta que es el índice 1
            valores.append(carta[1])
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2 or val == 3:
                pares += 1
                break

    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} número de cartas, es de {probabilidad_par}')


if __name__ == '__main__':
    tamano_mano = int(input('De cuantas cartas será la mano: '))
    intentos = int(input('Cuantas veces se correrá la simulación: '))

    main(tamano_mano, intentos)


