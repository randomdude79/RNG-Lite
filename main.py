import statistics, random, time, os, sys

version = "1.12.3"
seed = []
numbersList = []

def copy(seed):
    with open('seed.txt', 'w') as s:
        s.write(str(seed))
        print('Check seed.txt for your seed')

def loading_bar(duration=5, bar_length=20):
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = '=' * i + '>' + ' ' * (bar_length - i)
        sys.stdout.write(f'\r{percent:3}% [{bar}]')
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    print()  # Move to the next line after done

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
        if i == "clear":
            clear()
            print('Console cleared!\n')
            random_gen()
        elif i == "updates":
            with open('noncode/UpdateLog.txt', 'r') as f:
                print(f.read())
            print(f'Current version: {version}')
            print('For more, check out https://github.com/randomdude79/RNG-Lite')
            random_gen()
        elif i == "update":
            clear()
            loading_bar(duration=10, bar_length=50)
            os.system('git restore * && git pull')
            clear()
            print('Done with downloading updates!')
            for _ in range(3):
                for dots in ["   ", ".  ", ".. ", "..."]:
                    sys.stdout.write(f'Restarting{dots}\r')
                    time.sleep(0.5)
            clear()
            print(f"You're now up to date with version: {version}")
            os.system('python main.py')
        elif i == "exit":
            exit_program()
        elif is_an_integer(i):
            return int(i)
        else:
            print(f'"{i}" is not an integer. Please enter an integer.\n')

def random_gen():
    global seed, numbersList
    numbersList = []
    randomInt1 = None
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
