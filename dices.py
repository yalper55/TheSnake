import random


def welcome():
    dice()
    play()


def dice():
    a = random.randint(1, 6)
    print(a)

    b = random.randint(1, 6)
    print(b)
    print("sum...")

    c = a + b
    print("The result is: ", (c))


def play():

    x = input(
        "Press button to play , otherwise press x to finish the game: ")
    while x != 'X' and x != 'x':
        dice()
        play()
        return
    else:
        print("Thank you for playing this game")


welcome()
