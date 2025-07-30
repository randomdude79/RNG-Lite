from main import *

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
      elif i == "exit":
          exit_program()
      elif is_an_integer(i):
          return int(i)
      else:
          print(f'"{i}" is not an integer. Please enter an integer.\n')
