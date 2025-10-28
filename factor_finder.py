# Finds the factors of a number input by user

import math
import sys

while True:
    # Get number from user
    print('Enter a number to factor (or QUIT)')
    number = input('> ')
    if number.upper() == 'QUIT':
        sys.exit()

    # Ensure input is positive integer
    if not (number.isdecimal() and int(number) > 0):
        continue
    number = int(number)

    factors = []

    # Iterate from 1 to square root of number
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            if number // i != i:
                factors.append(number // i)
                
    factors = sorted(factors)

    print(', '.join([str(factor) for factor in factors]))
    

