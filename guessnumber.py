import random

start = input('Please assign the unmber for the start: ')
end = input('Please assign the number for the end: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
c = 0

while True:
    c += 1
    g = input('Please guess a number: ')
    g = int(g)
    if g == r:
        print('Finally right !')
        print('You guess the ', c, ' times.')
        break
    elif g > r:
        print('Upper than the answer.')
    else:
        print('Lower than the answer.')
    print('You guess the ', c, ' times.')