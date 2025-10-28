# Conway's Game of Life

import copy
import random
import time

WIDTH = 30
HEIGHT = 10

# Create 2d array populated randomly with 'living' or 'dead' cells
current_gen = []

for i in range(HEIGHT):
    current_gen.append([])

for row in current_gen:
    for i in range(WIDTH):
        if random.randint(0, 1) == 1:
            row.append('#')
        else:
            row.append(' ')

# Until program stopped by user
try:
    while True:
        # Print current generation
        for row in current_gen:
            print(''.join(row))
        
        # Create copy of current generation
        next_gen = copy.deepcopy(current_gen)

        # Get status of neighbouring cells
        for y in range(HEIGHT):
            for x in range(WIDTH):
                neighbors = ''
                for i in range(-1, 2):
                    if (y == 0 and i == -1) or (y == HEIGHT - 1 and i == 1):
                        continue
                    for j in range(-1, 2):
                        if (x == 0 and j == -1) or (x == WIDTH - 1 and j == 1):
                            continue
                        if not (i == 0 and j == 0):
                            neighbors += current_gen[y+i][x+j]
     
                # Living cells die if living neighbour count is not 2 or 3
                if current_gen[y][x] == '#' and neighbors.count('#') not in (2, 3):
                    next_gen[y][x] = ' '

                # Dead cells come alive if living neighbour count is 3
                if current_gen[y][x] == ' ' and neighbors.count('#') == 3:
                    next_gen[y][x] = '#'
        
        current_gen = next_gen

        time.sleep(0.5)
        print(f'\033[{HEIGHT}A', end='')

except KeyboardInterrupt:
    print('Program stopped by user')
