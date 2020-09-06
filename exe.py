import random


guess_number = random.randint(0, 10)

number = int(input("Enter your number "))


if number > guess_number:
    print("too high")
elif number < guess_number:
    print("too low")
else:
    print("you win")

print(("the number was "), guess_number)
