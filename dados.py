import random


def bienvenidos():
    dados()
    play()


def dados():
    a = random.randint(1, 6)
    print(a)

    b = random.randint(1, 6)
    print(b)
    print("sumando...")

    c = a + b
    print("El resultado es:", (c))


def play():

    x = input(
        "pulse una tecla para jugar , de lo contrario pulse x para terminar de jugar ")
    while x != 'X' and x != 'x':
        dados()
        play()
        return
    else:
        print("gracias por jugar")


bienvenidos()
