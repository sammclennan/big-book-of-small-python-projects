# 2048

import copy
import random
import sys

BOARD_SIZE = 4
EMPTY_SPACE = ' '


def draw_board(board):
    """Print playing board on screen."""
    row_template = """+-----+-----+-----+-----+
|     |     |     |     |
|{:^5}|{:^5}|{:^5}|{:^5}|
|     |     |     |     |"""

    for row in board:
        print(row_template.format(*row))
    print('+-----+-----+-----+-----+')


def add_new_tile(board):
    """Add a new tile at a random empty position with a 90% chance of being a 2 and a 10% chance of being a 4."""
    while True:
        rand_y, rand_x = (random.randrange(BOARD_SIZE), random.randrange(BOARD_SIZE))
        if board[rand_y][rand_x] == EMPTY_SPACE:
            board[rand_y][rand_x] = 2 if random.random() < 0.9 else 4
            return


def get_player_move():
    """Get directional move from player."""
    while True:
        print('                             W')
        print('Enter a direction to move: A S D (or QUIT)')
        choice = input('> ').strip().upper()
        if choice == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif choice in ('W', 'A', 'S', 'D'):
            return choice


def update_board(board, move):
    """Slide and merge tiles based on player's directional move and calculate increase in score."""
    board = copy.deepcopy(board)
    score = 0
    merged = []

    forward = range(BOARD_SIZE)
    reverse = range(BOARD_SIZE - 1, -1, -1)

    for row in forward if move in ('W', 'A') else reverse:
        for col in forward if move in ('W', 'A') else reverse:

            if board[row][col] != EMPTY_SPACE and (
                move == 'W' and row >= 1 or 
                move == 'S' and row < BOARD_SIZE - 1 or
                move == 'A' and col >= 1 or
                move == 'D' and col < BOARD_SIZE - 1
            ):
                y, x = row, col
                next_y, next_x = (row-1, col) if move == 'W' else (row+1, col) if move == 'S' else (row, col-1) if move == 'A' else (row, col+1)   

                while board[next_y][next_x] == EMPTY_SPACE:
                    board[next_y][next_x], board[y][x] = board[y][x], EMPTY_SPACE

                    if move == 'W' and y > 1:
                        next_y -=1
                        y -= 1
                    elif move == 'S' and y < BOARD_SIZE - 2:
                        next_y += 1
                        y += 1
                    elif move == 'A' and x > 1:
                        next_x -=1
                        x -= 1
                    elif move == 'D' and x < BOARD_SIZE - 2:
                        next_x += 1
                        x += 1
                    else:
                        break
                    
                if board[next_y][next_x] == board[y][x] and (next_y, next_x) not in merged:
                    board[next_y][next_x], board[y][x] = board[y][x] * 2, EMPTY_SPACE
                    score += board[next_y][next_x]
                    merged.append((next_y, next_x))
                            
    return board, score


def no_more_moves(board):
    """Check if remaining moves exist on board."""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (
                board[row][col] == EMPTY_SPACE or
                row < BOARD_SIZE - 1 and board[row+1][col] == board[row][col] or
                col < BOARD_SIZE - 1 and board[row][col+1] == board[row][col]
            ):
                return False
    return True


def main():
    # Create 2D array for board
    board = [[EMPTY_SPACE] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    score = 0
    
    # Initiate board with two values
    for _ in range(2):
        add_new_tile(board)

    print('Slide all the tiles on the board in one of four directions. Tiles with like numbers will combine into larger-numbered tiles. A new 2 tile is added to the board on each move. You win if you can create a 2048 tile. You lose if the board fills up the tiles before then.')
    input('Press enter to begin...')

    while True:
        # Display board
        draw_board(board)
        print(f'Score: {score}')

        # Get move from player
        move = get_player_move()

        # Update board and increment score
        new_board, score_increase = update_board(board, move)
        score += score_increase

        # Add new 2 or 4 to board
        if new_board != board:
            add_new_tile(new_board)
            board = new_board

        # Check for full board
        if no_more_moves(board):
            draw_board(board)
            print('No more moves! Game over!')
            print(f'Final score: {score}')
            sys.exit()


if __name__ == '__main__':
    main()