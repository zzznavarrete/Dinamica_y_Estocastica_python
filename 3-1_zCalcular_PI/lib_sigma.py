import random
import math

# X mayúscula es la forma matemática de representar un array
def media(X):
    return sum(X) / len(X)

def varianza(X):
    # Lo primero es que debemos saber la media (mu)
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)


def desviacion_estandar(X):
    # Raíz cuadrada de la varianza
    return math.sqrt(varianza(X))


if __name__ == '__main__':
    # Según la diferencia entre estos números será lo grande de la desviación/variabilidad.
    X = [random.randint(9, 12) for i in range(20)]
    # mu señala la media de la población total
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'Arreglo X: {X}')
    print(f'Media: {mu}')
    print(f'Varianza: {Var}')
    print(f'Desviación estándar: {sigma}')