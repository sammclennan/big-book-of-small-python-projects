# ASCII snail race

import os
import random
import sys
import time

TERMINAL_WIDTH = os.get_terminal_size()[0]
TRACK_LENGTH = 40
MAX_SNAILS = 8
MAX_NAME_LENGTH = 20
SNAIL = '@v'
SPEED = 20

length = min(TERMINAL_WIDTH - 2, TRACK_LENGTH)

# Get number of snails
try:
    while True:
        print(f'How many snails will race? (Max {MAX_SNAILS})')
        snail_count = input('> ').strip()
        if snail_count.isdecimal():
            snail_count = int(snail_count)
            if 1 < snail_count <= MAX_SNAILS:
                break
        print(f'Enter a number between 2 and {MAX_SNAILS}.')

    snail_data = {}

    # Get snail names
    for i in range(1, snail_count + 1):
        while True:
            print(f"Enter snail #{i}'s name:")
            snail_name = input('> ').strip()
            if not snail_name:
                print('Please enter a name.')
            elif snail_name in snail_data:
                print("Enter a name that hasn't already been used.")
            else:
                break
        snail_name = snail_name[:MAX_NAME_LENGTH]
        snail_data[snail_name] = 0

    winner = []

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print('GO!')
    time.sleep(1)

    while True:
        # Print track
        os.system('cls' if os.name == 'nt' else 'clear')
        print('START' + ' ' * (length - 9) + 'FINISH')
        print('|' + ' ' * length + '|')

        for name, distance in snail_data.items():
            print(' ' * distance + name)
            print('.' * distance + SNAIL)
            # Move snails
            if random.randint(0, 1):
                snail_data[name] += 1
            # Check for winner
            if distance > length:
                winner.append(name)
        time.sleep(1 / SPEED)
        
        if winner:
            if len(winner) > 1:
                print(f"It's a tie between {', '.join(winner[:-1])} and {winner[-1]}!")
            else:
                print(f'{winner[0]} wins!')
            sys.exit()

except KeyboardInterrupt:
    sys.exit()