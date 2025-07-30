import statistics, random, time, os, sys
from functions import *

version = "1.0.11.1"
seed = []
numbersList = []

clear()
loading_bar(duration=5, bar_length=50)
os.system('git restore * && git pull')
print(f"You're now up to date with version: {version}")
time.sleep(1)
clear()

def random_gen():
    global seed, numbersList
    numbersList = []
    if input('Would you like to use a seed?\n').lower() == 'yes':
        seed = int(input('Enter a seed:\n'))
    else:
        seed = int(''.join(str(random.randint(0, 9)) for _ in range(20)))
    random.seed(seed)
    number1 = get_int('Choose your first number.\n')
    print()
    number2 = get_int('Choose your second number.\n')
    print()
    amount = get_int('How many numbers do you want to generate?\n')
    print()

    number1, number2 = max(number1, number2), min(number1, number2)

    if amount > 1:
        print('Your random numbers are:')
        for _ in range(amount):
            num = random.randint(number2, number1)
            print(num)
            numbersList.append(num)
        print()
        if input('Would you like to find the average of all your numbers?\n').lower() == 'yes':
            print('\nThe average of all your numbers is:', statistics.mean(numbersList), '\n')
        if input('Would you like to know your seed?\n').lower() == 'yes':
            print('Your seed is:', seed)
            if input('Would you like to copy the seed?\n').lower() == 'yes':
                copy(seed)
        print()
    else:
        print('Your random number is:\n', random.randint(number2, number1))
    random.seed()
    print()

while True:
    random_gen()
