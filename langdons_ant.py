# Langon's Ant cellular automata simulation

import os
import random
import sys
import time

from colorama import Back

TERMINAL_WIDTH = os.get_terminal_size()[0] - 1
TERMINAL_HEIGHT = os.get_terminal_size()[1] - 1
COLOR_1 = Back.GREEN
COLOR_2 = Back.RED
ANT_COUNT = 3
ORIENTATIONS = ('^', 'v', '<', '>')
PAUSE_TIME = 0.1


def draw_field(playfield, ants):
    for row in range(len(playfield)):
        for column in range(len(playfield[0])):

            # Check if cell contains ant
            ant_cell = next((ant for ant in ants if ant['coords'] == [row, column]), None)

            if playfield[row][column] == 'X':
                print(COLOR_1 + (ant_cell['orientation'] if ant_cell else ' '), end='')
            else:
                print(COLOR_2 + (ant_cell['orientation'] if ant_cell else ' '), end='')
        print()


def main():
    # Get ant coordinates and orientation
    while True:
        ant_data = [{'coords': [random.randrange(0, TERMINAL_HEIGHT), random.randrange(0, TERMINAL_WIDTH)], 'orientation': random.choice(ORIENTATIONS)} for _ in range(ANT_COUNT)]

        # Ensure no duplicate coords exist
        if len({tuple(ant['coords']) for ant in ant_data}) == len(ant_data):
            break

    # Create 2D array for playing field
    field = [['X' for _ in range(TERMINAL_WIDTH)] for _ in range(TERMINAL_HEIGHT)]

    turn_left = {
        '^': '<',
        '>': '^',
        'v': '>',
        '<': 'v'
    }

    turn_right = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^'
    }

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Draw playing field
        draw_field(field, ant_data)

        for ant in ant_data:
            # Change background color and ant orientation
            if field[ant['coords'][0]][ant['coords'][1]] == 'X':
                field[ant['coords'][0]][ant['coords'][1]] = 'Y'
                ant['orientation'] = turn_right[ant['orientation']]
            elif field[ant['coords'][0]][ant['coords'][1]] == 'Y':
                field[ant['coords'][0]][ant['coords'][1]] = 'X'
                ant['orientation'] = turn_left[ant['orientation']]

            # Move ant forward one space
            match ant['orientation']:
                case '^':
                    ant['coords'][0] -= 1
                case '>':
                    ant['coords'][1] += 1
                case 'v':
                    ant['coords'][0] += 1
                case '<':
                    ant['coords'][1] -= 1

            # Wrap and coordinates
            ant['coords'][0] %= TERMINAL_HEIGHT
            ant['coords'][1] %= TERMINAL_WIDTH

        time.sleep(PAUSE_TIME)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
