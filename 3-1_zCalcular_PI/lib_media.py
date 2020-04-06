import random

# X mayúscula es la forma matemática de representar un array
def media(X):
    return sum(X) / len(X)


if __name__ == '__main__':
    X = [random.randint(1, 21) for i in range(20)]
    # mu señala la media de la población total
    mu = media(X)

    print(X)
    print(mu)