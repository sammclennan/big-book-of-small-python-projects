# Finds prime numbers

import math
import time

PAUSE = 0.1


def is_prime(num):
    if num < 2: return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def main():
    print('Enter a number to display prime numbers from:')
    while True:
        i = input('> ').strip()
        if i.isdecimal():
            i = int(i)
            break
        print('Please enter a positive number')

    input('Press Ctrl + C to quit. Press Enter to begin...')
    while True:
        if is_prime(i):
            print(i, end=' ', flush=True)
            time.sleep(PAUSE)
        i += 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program stopped by user.')