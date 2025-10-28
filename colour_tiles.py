import os
import random

from colorama import Back

WIDTH, HEIGHT = os.get_terminal_size()
HORIZONTAL_TILES = 9
VERTICAL_TILES = 6
COLOURS = {
    'R': Back.RED,
    'G': Back.GREEN,
    'Y': Back.YELLOW,
    'B': Back.BLUE,
    'M': Back.MAGENTA,
    'C': Back.CYAN,
}
BORDER_COLOUR = Back.WHITE


def non_adjacent_sample(population, sample_size):
    """Samples a population, excluding adjacent values."""
    if len(population) < sample_size:
        raise ValueError('Sample size cannot be greater than population size.')

    sample = []
    
    population = list(set(population))
    random.shuffle(population)

    for x in population:
        if all(abs(x - y) > 1 for y in sample):
            sample.append(x)
        if len(sample) == sample_size:
            return sample        
    
    raise ValueError('Not enough non-adjacent values to form sample.')
    

# Create 2D array for canvas
canvas = [[' ' for col in range(WIDTH)] for row in range(HEIGHT)]

# Get tile borders
horizontal_separators = sorted(non_adjacent_sample(range(2, HEIGHT - 1), VERTICAL_TILES - 1) + [HEIGHT])
vertical_separators = sorted(non_adjacent_sample(range(2, WIDTH - 1), HORIZONTAL_TILES - 1) + [WIDTH])

# Assign colours to tiles
tiles = {}
for h in horizontal_separators:
    for v in vertical_separators:
        tiles[(h, v)] = random.choice(list(COLOURS))

for row_no in range(len(canvas)):
    for col_no in range(len(canvas[row_no])):
        if row_no in horizontal_separators or col_no in vertical_separators:
            canvas[row_no][col_no] = '#'
        else:
            for (bottom_edge, right_edge), colour in tiles.items():
                if row_no < bottom_edge and col_no < right_edge:
                    canvas[row_no][col_no] = colour
                    break

# Print canvas
for row in canvas:
    for col in row:
        if col == '#':
            print(BORDER_COLOUR + ' ', end='')
        else:
            print(COLOURS[col] + ' ', end='')