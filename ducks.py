# Creates a scrolling field of ASCII ducklings

import os
import random
import shutil
import sys
import time

WIDTH = shutil.get_terminal_size()[0]
HEIGHT = shutil.get_terminal_size()[1]


# Function to generate a random duck
def get_duck(size):
    small_duck_left = ['{}") '.format(random.choice(('=', '>'))),
                       '( {})'.format(random.choice(('^', '>'))),
                       ' ^^  ',]
    small_duck_right = [' ("{}'.format(random.choice(('=', '<'))),
                        '({} )'.format(random.choice(('^', '<'))),
                        ' ^^  ',]
    big_duck_left = ['{}{}) '.format(random.choice(('=', '>')), random.choice(('" ', '\'\'', '^^', '``'))),
                     '(  {})'.format(random.choice(('^', '>'))),
                     ' ^ ^ ',]
    big_duck_right = [' ({}{}'.format(random.choice((' "', '\'\'', '^^', '``')), random.choice(('=', '<'))),
                      '({}  )'.format(random.choice(('^', '<'))),
                      ' ^ ^  ',]
    if size == 0:
        return small_duck_left
    elif size == 1:
        return small_duck_right
    elif size == 2:
        return big_duck_left
    elif size == 3:
        return big_duck_right


# Calculate maximum and minimum number of ducks to display on terminal
max_ducks = WIDTH * HEIGHT // (5*3) // 15
min_ducks = max_ducks // 3

print('Duckling screensaver\nPress Ctrl + C to quit...')
time.sleep(2)

try:
    while True:
        # Create blank 2D array size of terminal
        canvas = []
        canvas = [[' '] * WIDTH for row in range(HEIGHT)]

        # Get number of ducks to plot
        num_ducks = random.randint(min_ducks, max_ducks)

        # Store coordinates of ducks on canvas
        duck_coords = []

        # For number of ducks
        for i in range(num_ducks):
            # Generate a random duck
            duck = get_duck(random.randint(0, 3))

            # Get duck dimensions
            duck_width = len(duck[0])
            duck_height = len(duck)

            # Get coords for new duck
            while True:
                x_coord = random.randint(1, WIDTH - len(duck[0]))
                y_coord = random.randint(1, HEIGHT - len(duck))
                
                # Get corner coordinates
                top_left = (x_coord, y_coord)
                top_right = (x_coord + duck_width - 1, y_coord)
                bottom_left= (x_coord, y_coord + duck_height - 1)
                bottom_right = (x_coord + duck_width - 1, y_coord + duck_height - 1)

                # Ensure ducks not overlapping
                if not (top_left in duck_coords or top_right in duck_coords or bottom_left in duck_coords or bottom_right in duck_coords):
                    break

            # Add duck to 2D canvas
            for y in range(duck_height):
                for x in range(duck_width):
                    canvas[y_coord + y][x_coord + x] = duck[y][x]
                    duck_coords.append((x_coord + x, y_coord + y))
        
        # Draw canvas
        for row in canvas:
            print(''.join(row))

        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

except KeyboardInterrupt:
    print('Program stopped by user.')
    sys.exit()
