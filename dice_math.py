# ASCII dice game. Rolls 2 - 6 dice per turn. Player must sum the values of the dice displyed on the terminal. Player gains 4 points for each correct answer and loses 1 point for each incorrect answer.

import random
import shutil
import sys
import time

WIDTH = shutil.get_terminal_size()[0]
HEIGHT = shutil.get_terminal_size()[1]

if WIDTH < 9 or HEIGHT < 5:
    print('Terminal is too small to display dice')
    sys.exit()

DICE = {1: ['+-------+',
            '|       |',
            '|   O   |',
            '|       |',
            '+-------+',],
        2: ['+-------+',
            '| O     |',
            '|       |',
            '|     O |',
            '+-------+',],
        3: ['+-------+',
            '|     O |',
            '|   O   |',
            '| O     |',
            '+-------+',],
        4: ['+-------+',
            '| O   O |',
            '|       |',
            '| O   O |',
            '+-------+',],
        5: ['+-------+',
            '| O   O |',
            '|   O   |',
            '| O   O |',
            '+-------+',],
        6: ['+-------+',
            '| O   O |',
            '| O   O |',
            '| O   O |',
            '+-------+',]}

# Player score
score = 0

print('Press Ctrl + C to quit')
time.sleep(2)

try:
    # For each turn
    while True:
        # Create blank 2D array for canvas
        canvas = []
        for row in range(HEIGHT):
            canvas.append([' '] * WIDTH)

        # Get number of dice
        num_dice = random.randint(2, 6)

        # Stores the the coordinates occupied by dice
        dice_coords = []

        dice_sum = 0

        for i in range(num_dice):
            # Roll dice
            roll = random.randint(1, 6)
            dice_sum += roll

            while True:
                # Get random coords
                x_coord = random.randint(1, WIDTH - 10)
                y_coord = random.randint(1, HEIGHT - 6)

                # Get coordinates of dice corners
                top_left = (x_coord, y_coord)
                top_right = (x_coord + 8, y_coord)
                bottom_left = (x_coord, y_coord + 4)
                bottom_right = (x_coord + 8, y_coord + 4)

                # Ensure dice aren't overlapping
                if not (top_left in dice_coords or top_right in dice_coords or bottom_left in dice_coords or bottom_right in dice_coords):
                    break

            # Add dice to canvas matrix
            for y in range(5):
                for x in range(9):
                    canvas[y_coord + y][x_coord + x] = DICE[roll][y][x]
                    dice_coords.append((x_coord + x, y_coord + y))

        # Print canvas
        for row in range(HEIGHT):
            print(''.join(canvas[row]))
        
        # Prompt player for sum
        while True:
            try:
                answer = int(input('Enter the sum: '))
                break
            except ValueError:
                print('The sum must be an integer!')

        # If correct, add 4 points. If incorrect, subtract 1 point unless score is 0
        if answer == dice_sum:
            score += 4
            print('Correct! + 4 points')
        elif score > 0:
            score -= 1
            print(f'Sorry! the answer was {dice_sum}! - 1 point')
        else:
            print(f'Sorry! The answer was {dice_sum}!')     
        
        # Display score
        print(f'Total score: {score}')

        time.sleep(2)   

except KeyboardInterrupt:
    print('\nProgram stopped by user')
    sys.exit()