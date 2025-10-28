# Tic-Tac-Toe

import random
import sys


def draw_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col] + ('|' if col < 2 else ''), end='')
        print('  1 2 3' if row == 0 else '  4 5 6' if row == 1 else '  7 8 9')
        print('-+-+-' if row < 2 else '')


def get_player_move(board, player):
    while True:
        print(f'Enter move for Player {player} (1 - 9) (or QUIT)')
        choice = input('> ').strip().upper()
        if choice == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if choice.isdigit():
            x = int(choice)
            if 1 <= x <= 9:
                x = x - 1
                # Check position is not occupied
                if board[x // 3][x % 3] == ' ':
                    return x


def check_for_win(board):
    # Check horizontals/verticals
    for i in range(len(board)):
        if board[i][0] != ' '  and (board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]
        elif board[0][i] != ' ' and (board[0][i] == board[1][i] == board[2][i]):
            return board[0][i]
    # Check diagonals
    if board[0][0] != ' '  and (board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    elif board[0][2] != ' ' and (board[0][2] == board[1][1] == board[2][0]):
        return board[0][2]
    
    return None
    

def full_board(board):
    for row in board:
        if ' ' in row:
            return False
    
    return True


def main():
    # Create 2D array for board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    players = ['X', 'O']
    random.shuffle(players)

    print('Welcome to Tic-Tac-Toe!')

    while True:
        for player in players:
            move = get_player_move(board, player)

            board[move // 3][move % 3] = player

            draw_board(board)

            winner = check_for_win(board)
            if winner:
                print(winner + ' wins!')
                sys.exit()
            
            if full_board(board):
                print('The game is a tie!')
                sys.exit()
            

if __name__ == '__main__':
    main()
    
