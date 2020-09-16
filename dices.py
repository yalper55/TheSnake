import random
import time


def welcome():
    print("Welcome to crazy dice")
    print()
    print("throwing...")
    print()
    time.sleep(1)
    dice()
    play()


def dice():
    a = random.randint(1, 6)
    print(a)

    b = random.randint(1, 6)
    print(b)
    print("Adding up...")

    c = a + b
    time.sleep(1)
    print("The result is:", (c))
    print("--------------------------------------------------------------")


def play():
    time.sleep(.5)
    x = input(
        "Press a key to play , otherwise press x to finish the game: ")
    print("--------------------------------------------------------------")
    while x != 'X' and x != 'x':
        dice()
        play()
        return
    else:
        print("Thanks for playing!! , come back soon")
        print("っ(◕‿◕)っ")
        time.sleep(.5)
        print("Create by Yalper")


welcome()
