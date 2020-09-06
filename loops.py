# For Loop

#users = ['Ed', 'ana', 'john', 'Podrick', 'Smith']

# for user in users:
#    print('hello there user')
#    print(user)


users = ['Ed', 'ana', 'john', 'Podrick', 'Smith']
# my_list = list(range(0, 10))  # generates a list 0 to 10

# for i in range(0, 20):
#    print('irun 20times')

name = 'Edwin'

for letter in name:
    print(letter)

# while Loop
age = 0
while age <= 20:
    age = age + 1  # age +=1
    if(age == 14):
        print('I am indepedent now')
        continue
        print(age)
