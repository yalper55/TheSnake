import random


def bienvenidos():
    print("Bienvenidos a dados locos")
    print()
    print("lanzando...")
    print()
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
    print("--------------------------------------------------------------")


def play():
    x = input(
        "pulse una tecla para jugar, de lo contrario pulse x para terminar de jugar: ")
    print("--------------------------------------------------------------")
    while x != 'X' and x != 'x':
        dados()
        play()
        return
    else:
        print("Gracias por jugar!! , vuelva pronto")
        print("(◕‿◕)っ")


bienvenidos()
