import sys

# Algoritmo tradicional de fibonacci
def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo( n - 1 ) + fibonacci_recursivo( n - 2 )

# Algoritmo fibonacci pero inyectado con programación dinámica. En esta ocasión, guardamos en
# valores en memoria los cálculos ya hechos para que en vez de volver a calcular, el algoritmo los
# re-utilice y optimice el tiempo de ejecución total de la función.
def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1, memo) + fibonacci_dinamico(n-2, memo)
        memo[n] = resultado

        return resultado


if __name__ == "__main__":
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un número: '))
    #resultado = fibonacci_recursivo(n)
    resultado = fibonacci_dinamico(n)
    print(resultado)

