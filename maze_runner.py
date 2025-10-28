# Maze Runner game

import os
import random
import sys

from pathlib import Path

WALL = '░'
PATH = ' '
PLAYER = '@'
DIRECTION_MAPPING = {
    'W': (-1, 0),
    'A': (0, -1),
    'S': (1, 0),
    'D': (0, 1),
}


def load_maze(file):
    maze_array = []
    start_coords = None
    finish_coords = None

    # Open maze txt file
    with open(file, 'r') as f:
        # Create 2D array from rows
        for row in f:
            maze_array.append(list(row.rstrip()))

        # Get coordinates of maze start and finish
        for row_no in range(len(maze_array)):
            for col_no in range(len(maze_array[row_no])):
                if maze_array[row_no][col_no] == 'S':
                    start_coords = [row_no, col_no]
                elif maze_array[row_no][col_no] == 'E':
                    finish_coords = [row_no, col_no]

                # Set character to represent walls
                if maze_array[row_no][col_no] == '#':
                    maze_array[row_no][col_no] = WALL
        
        return (maze_array, start_coords, finish_coords)
    

def print_maze(array):
    os.system('clear' if os.name == 'posix' else 'cls')
    print('Press Ctrl + C to exit')
    for row in array:
        print(''.join(row))


def play_again():
    while True:
        print('Do you want to play again?')
        play_again_response = input('> ').upper()
        if play_again_response in ('Y', 'YES', 'N', 'NO'):
            return play_again_response in ('Y', 'YES')
        else:
            print('Invalid response! Please enter a YES/NO response.')


def get_move(player_coords, maze_array):
    while True:
        print('W'.rjust(19))
        print('Enter your move: ASD')

        move_input = input('> ').upper()
        
        if not move_input in DIRECTION_MAPPING:
            print('Invalid move. Enter one of: W, A, S, D')
        else:
            if maze_array[player_coords[0] + DIRECTION_MAPPING[move_input][0]][player_coords[1] + DIRECTION_MAPPING[move_input][1]] == WALL:
                print("You can't move in that direction!")
            else:
                return move_input


def move_player(player_coords, maze_array, player_move):
    change_y, change_x = DIRECTION_MAPPING[player_move]
    y_coord, x_coord = player_coords

    # Move player in direction until wall is hit or intersection reached
    while (0 <= y_coord + change_y < len(maze_array) and
           0 <= x_coord + change_x < len(maze_array[0]) and
           maze_array[y_coord + change_y][x_coord + change_x] != WALL):
        if player_move in ('W', 'S') and y_coord != player_coords[0]:
            if maze_array[y_coord][x_coord  - 1] == PATH or maze_array[y_coord][x_coord + 1] == PATH:
                break
        elif player_move in ('A', 'D') and x_coord != player_coords[1]:
            if maze_array[y_coord - 1][x_coord] == PATH or maze_array[y_coord + 1][x_coord] == PATH:
                break
            
        y_coord += change_y
        x_coord += change_x

    return [y_coord, x_coord]


def main(): 
    # Get maze file directory
    print('Enter maze file directory')
    maze_file_directory = Path(input('> '))
    maze_files = [file for file in maze_file_directory.iterdir() if file.is_file()]

    if not maze_files:
        raise FileNotFoundError('No files found in specified directory.')

    try:
        # Load a new file until user chooses to quit
        while True:
            maze_file = random.choice(maze_files)
            
            maze_array, start_coords, finish_coords = load_maze(maze_file)

            # Return error if start or finish not found
            if not start_coords:
                print(f'Error: Start position not found in {maze_file}.')
                sys.exit()
            elif not finish_coords:
                print(f'Error: Finish position not found in {maze_file}.')
                sys.exit()

            player_coords = start_coords

            while True:
                # Update player sprite
                maze_array[player_coords[0]][player_coords[1]] = PLAYER
                
                # Clear screen and print maze
                print_maze(maze_array)
                
                # Check for maze completion
                if player_coords == finish_coords:
                    print('Congratulations! You reached the end!')
                    if not play_again():
                        print('Thanks for playing!')
                        sys.exit()
                    else:
                        break

                # Get move from player
                player_move = get_move(player_coords, maze_array)
                
                # Clear existing player sprite
                maze_array[player_coords[0]][player_coords[1]] = PATH

                # Move player
                player_coords = move_player(player_coords, maze_array, player_move)

    except KeyboardInterrupt:
        print('\nProgram terminated by user')


if __name__ == '__main__':
    main()