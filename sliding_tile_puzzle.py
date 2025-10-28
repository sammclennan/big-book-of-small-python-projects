# Sliding tile puzzle

import random
import sys

N = 6
BLANK = ' '
SHUFFLES = 300

DIRECTION_KEY = {
    'W': (-1, 0),
    'A': (0, -1),
    'S': (1, 0),
    'D': (0, 1),
}


def get_moveable_tiles(board):
    """Get coordinates of moveable tiles and their corresponding directions of movement."""
    coordinate_key = {
        'W': (),
        'A': (),
        'S': (),
        'D': (),
    }

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == BLANK:
                if row < len(board) - 1:
                    coordinate_key['W'] = (row+1, col)
                if col < len(board[row]) - 1:
                    coordinate_key['A'] = (row, col+1)
                if row > 0:
                    coordinate_key['S'] = (row-1, col)
                if col > 0:
                    coordinate_key['D'] = (row, col-1)
                
                return coordinate_key


def shuffle_board(board):
    """Shuffle ordered tiles x times to create a solveable puzzle."""
    for _ in range(SHUFFLES):
        moveable_tiles = get_moveable_tiles(board)
        move = random.choice([key for key, value in moveable_tiles.items() if value])
        switch_tiles(board, moveable_tiles, move)


def switch_tiles(board, moveable_tiles, move):
    """Swap blank tile with adjacent tile in specified direction."""
    new_coordinates = [a + b for a, b in zip(moveable_tiles[move], DIRECTION_KEY[move])]

    current_y, current_x = moveable_tiles[move]
    new_y, new_x = new_coordinates

    board[current_y][current_x], board[new_y][new_x] = board[new_y][new_x], board[current_y][current_x]


def get_player_move(coordinate_key):
    """Get movement direction from player."""
    w_key, a_key, s_key, d_key = [key if value else ' ' for key, value in coordinate_key.items()]

    while True:
        print(f'                         ({w_key})')
        print(f'Enter WASD (or QUIT): ({a_key})({s_key})({d_key})')

        choice = input('> ').strip().upper()

        if choice == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif choice in coordinate_key and coordinate_key[choice]:
            return choice


def draw_board(board):
    """Draw puzzle board."""
    for i in range(N):
        print('+------' * N + '+')
        print('|      ' * N + '|')
        for j in range(N):
            print(f'|  {board[i][j]:2}  ', end='')
        print('|')
        print('|      ' * N + '|')
    print('+------' * N + '+')


def main():
    print("""Use the WASD keys to move the tiles
back into their original order e.g.
        1  2  3  4
        5  6  7  8
        9  10 11 12
        13 14 15""")
    input('Press Enter to begin...')

    # Create 2D array of shuffled tiles
    ordered_tiles = list(range(1, N ** 2)) + [BLANK]
    tiles = ordered_tiles.copy()
    board = [tiles[i:i+N] for i in range(0, len(tiles), N)]
    shuffle_board(board)

    while True:
        # Draw board
        draw_board(board)

        # Check for winning condition
        if [col for row in board for col in row] == ordered_tiles:
            print('You won!')
            sys.exit()
        
        # Find moveable tiles
        moveable_tiles = get_moveable_tiles(board)

        # Get move from player
        move = get_player_move(moveable_tiles)

        # Move tiles
        switch_tiles(board, moveable_tiles, move)
        

if __name__ == '__main__':
    main()