# Simulates dice rolling in Dungeons & Dragons-style games. e.g. 3d6 rolls three six-sided dice, and 1d10+2 rolls one ten-sided dice and adds a two-point bonus.

import random
import re
import sys

print("""Enter the number of dice to roll, the number of sides on the dice, followed by an optional bonus/penalty/multiplier.
For example:
3d6 equals three six-sided dice
1d10+2 equals one ten-sided dice plus a bonus of two
4d12-2 equals four twelve-sided dice minus a two-point penalty
4d6*2 equals four six-sided dice with a multiplier of two
QUIT to quit""")

# Get user input
while True:
    while True:
        roll_instructions = input('> ').lower()
        if roll_instructions == 'quit':
            sys.exit()
        res = re.search('(\d+)d(\d+)([+\-\*]\d+)?', roll_instructions)
        if not res:
            print('Input must be in the following format:\n[number of dice]d[number of sides][+/-/* bonus/penalty/multiplier] (optional)')
        elif res.group(1) == '0':
            print('You cannot roll zero dice!')
        elif res.group(2) == '0':
            print('A dice cannot have zero sides!')
        else:
            break

    # Get number of dice, number of faces, and bonus
    num_dice =  int(res.group(1))
    num_sides = int(res.group(2))
    bonus = res.group(3)

    # Store dice rolls and total
    num_list = []
    total = 0

    # Roll dice, adding results to list and total
    for roll_num in range(num_dice):
        roll = random.randint(1, num_sides)
        num_list.append(str(roll))
        total += roll

    # Append bonus
    if bonus:
        num_list.append(bonus)
        if bonus.startswith('*'):
            total *= int(bonus[1:])
        else:
            total += int(bonus)

    # Print result
    print(str(total) + ' (' + ', '.join(num_list) + ')')