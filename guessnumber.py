import random

r = str(random.randint(1, 100))

while True:
    g = input('Please guess a number: ')
    if g == r:
        print('Finally right !')
        break
    elif g > r:
        print('Upper than the answer.')
    else:
        print('Lower than the answer.')