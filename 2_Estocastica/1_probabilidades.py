import random

# Calculando las probabilidad de obtener ciertas combinaciones con dados

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_1 = 0
    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 += 1

    tiros_sin_1 = 0
    for tiro in tiros:
        if 1 not in tiro:
            tiros_sin_1 += 1

    probabilidad_tiros_sin_1 = tiros_sin_1 / numero_de_intentos
    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print(f'Probabilidad de obtener 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}')
    print(f'Probabilidad de NO obtener 1 en {numero_de_tiros} tiros = {probabilidad_tiros_sin_1}')
    return tiros


if __name__ == '__main__':
    '''
        Ejemplo sugerido: Basándose en la pregunta 5 del archivo '1_probabilidades.txt' de esta misma carpeta, 
        ingresemos al simulador que tire el dado 10 veces. Y en número de simulación lo más posible.
        (En un pc normal, unas 10000 veces estará ok), así podremos ver la probabilidad de obtener 1 al lanzar
        el dado 10 veces (igual como lo calculamos con las leyes en el archivo anterior nombrado, en el cual,
        según nuestro cálculo, el resultado era 0.8384). 
    '''
    print('*** Probabilidad de que obtengamos 1 al tirar un dado. ***')
    numeros_de_tiros = int(input('Cuantas veces tiro el dado?: '))
    # Mientras más veces corramos la simulación, más cerca estaremos del valor correcto.
    numero_de_intentos = int(input('Cuantas veces correrá la simulación?: '))

    main(numeros_de_tiros, numero_de_intentos)

