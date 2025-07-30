import statistics, random, time, os, sys

version = "1.1.6"
seed = []
numbersList = []

def copy(seed):
    with open('noncode/seed.txt', 'w') as s:
        s.write(str(seed))
        print('Check seed.txt for your seed')

def loading_bar(duration=5, bar_length=20):
    RED = '\033[91m'      # Bright Red
    GREY = '\033[90m'     # Bright Black / Grey
    RESET = '\033[0m'     # Reset to default

    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        completed = RED + '-' * i + RESET
        remaining = GREY + '-' * (bar_length - i) + RESET
        sys.stdout.write(f'\r{percent:3}% [{completed}{remaining}]')
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    print()

def clear():
    os.system('clear')

def exit_program():
    sys.exit()

def is_an_integer(s):
    try: int(s); return True
    except ValueError: return False

def get_int(prompt):
    while True:
        i = input(prompt)
        if i == "-0":
            print('-0 is not an integer. Please try again.\n')
            continue
        elif i == "exit":
            exit_program()
        elif is_an_integer(i):
            return int(i)
        else:
            print(f'"{i}" is not an integer. Please enter an integer.\n')

loading_bar(duration=10, bar_length=50)
os.system('git restore * && git pull')
clear()
print(f"Running on version: {version}\n Check out the Github page here: https://github.com/randomdude79/RNG-Lite\nType 'exit' to exit the program")

def random_gen():
    global seed, numbersList
    numbersList = []
    seedq = input('Would you like to use a seed?\n').lower()
    if seedq == 'yes':
        seed = int(input('Enter a seed:\n'))
    if seedq == 'exit':
        exit_program()
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
