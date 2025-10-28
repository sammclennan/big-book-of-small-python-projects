# Sound mimic memorization game

import os
import random
import sys
import time

try:
    import playsound3
except ImportError:
    print('Could not import playsound3. Please ensure module is installed.')
    sys.exit()

pattern = []
points = 0

print('Try to memorize a pattern of A S D F letters (each with its own sound) as it gets longer and longer.')
input('Press Enter to begin...')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    pattern.append(random.choice(('A', 'S', 'D', 'F')))

    for letter in pattern:
        print(letter, end=' ', flush=True)
        playsound3.playsound(f'sound{letter}.wav')
    
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('Enter the pattern:')
    response = input('> ').strip().upper()

    if response == ''.join(pattern):
        print('Correct!')
        points += 1
    else:
        print('Incorrect')
        print(f'The pattern was {' '.join(pattern)}')
    
    for letter in response:
        playsound3.playsound(f'sound{letter}.wav')
        
    if response != ''.join(pattern):
        print(f'You scored {points} points.')
        print('Thanks for playing!')
        sys.exit()
    
    time.sleep(1)





