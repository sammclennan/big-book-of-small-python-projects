# Prints a Collatz sequence from a starting number

import sys

print('Enter the starting integer (greater than 0) or QUIT')

while True:
    try:
        n = input('> ')
        if n.lower() == 'quit':
            sys.exit()
        n = int(n)
        if n > 0:
            break
        else:
            print('The number must be greater than 0!')
    except ValueError:
        print('Please enter a valid integer!')

print(n, end='')

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1

    print(', ' + str(n), end='')
    
