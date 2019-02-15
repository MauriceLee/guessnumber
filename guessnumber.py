import random

r = str(random.randint(1, 100))
c = 0

while True:
    g = input('Please guess a number: ')
    c = c + 1
    if g == r:
        print('Finally right !')
        print('You guess the ', c, ' times.')
        break
    elif g > r:
        print('Upper than the answer.')
    else:
        print('Lower than the answer.')