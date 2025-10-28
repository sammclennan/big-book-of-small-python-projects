# Royal Game of Ur

import random
import sys

PLAYERS = ['X', 'O']
FLOWER_SQUARES = (4, 8, 14)
LETTER_KEY = {
    'X': ['home', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 's', 't', 'goal'],
    'O': ['home', 'a', 'b', 'c', 'd', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'goal']
}
BOARD_GRAPHICS = """                   {:.<7}           {:.<7}
                   Home              Goal
                     v                 ^
+-----+-----+-----+--v--+           +--^--+-----+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****h|    g|    f|    e|           |****t|    s|
+--v--+-----+-----+-----+-----+-----+-----+--^--+
|     |     |     |*****|     |     |     |     |
|  {}  >  {}  >  {}  >* {} *>  {}  >  {}  >  {}  >  {}  |
|    i|    j|    k|****l|    m|    n|    o|    p|
+--^--+-----+-----+-----+-----+-----+-----+--v--+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****d|    c|    b|    a|           |****r|    q|
+-----+-----+-----+--^--+           +--v--+-----+
                     ^                 v
                   Home              Goal
                   {:.<7}                {:.<7}
"""


def draw_board(board):
    def get_value(cell):
        return ''.join(cell) if cell else ' '

    board_values = [
        ''.join(board[0][0]), ''.join(board[15][0])
        ]
    board_values.extend(get_value(board[i][0]) for i in range(4, 0, -1))
    board_values.extend(get_value(board[i][0]) for i in range(14, 12, -1))
    board_values.extend(get_value(board[i][0] or board[i][1]) for i in range(5, 13))
    board_values.extend(get_value(board[i][1]) for i in range(4, 0, -1))
    board_values.extend(get_value(board[i][1]) for i in range(14, 12, -1))
    board_values.extend([
        ''.join(board[0][1]), ''.join(board[15][1])
        ])

    print(BOARD_GRAPHICS.format(*board_values))


print("""Two player_positions each begin with seven tokens in their home, and the first player to move all seven to the goal is the winner. Players take turns flipping four coins. The player can move a token one space for each head that comes up.
The tokens travel along the path indicated below.\n""")

print("""            X Home      X Goal
              v           ^
+---+---+---+-v-+       +-^-+---+
|v<<<<<<<<<<<<< |       | ^<|<< |
|v  |   |   |   |       |   | ^ |
+v--+---+---+---+---+---+---+-^-+
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^ |
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>v |
+^--+---+---+---+---+---+---+-v-+
|^  |   |   |   |       |   | v |
|^<<<<<<<<<<<<< |       | v<<<< |
+---+---+---+-^-+       +-v-+---+
              ^           v
            O Home      O Goal""")

print("\nOnly one token may exist on a space at a time. If a token lands on an opponent's token while in the shared middle path, the opponent's token is sent back home. If a token lands on the middle flower square, it is safe from being landed on. If a token lands on any of the other four flower tiles, the player gets to roll again.")

board = [[['X' for _ in range(7)], ['O' for _ in range(7)]]] + [[[], []] for _ in range(15)]

input('\nPress Enter to start...')

while True:
    for index, player in enumerate(PLAYERS):
        while True:
            # Print board
            draw_board(board)
            
            opponent_index = (index + 1) % len(PLAYERS)

            # Get number of spaces to move
            input(f'It is {player}\'s turn. Press Enter to flip...')
            flips = [random.choice(['H', 'T']) for i in range(4)]

            print(f'Flips: {'-'.join(flips)}', end=' ') 

            if all(flip == 'T' for flip in flips):
                input('You lose a turn. Press Enter to continue...')
                break

            spaces = flips.count('H')

            # Get available moves
            available_moves = []
            for j in range(16 - spaces):
                new_position = j + spaces
                if board[j][index]:
                    if new_position == 15 or not board[new_position][index]:
                        if new_position == 8 and board[new_position][opponent_index]:
                            continue
                        else:
                            available_moves.append(LETTER_KEY[player][j])

            if not available_moves:
                input('No available moves. Next player\'s turn. Press Enter to continue...')
                break

            # Get player move
            while True:
                print(f'Select move {spaces} spaces: {' '.join(available_moves)}')
                selected_token = input('> ').strip().lower()
                if selected_token == 'quit':
                    print('Thanks for playing!')
                    sys.exit()
                elif selected_token in available_moves:
                    selected_token = LETTER_KEY[player].index(selected_token)
                    break
                else:
                    print('That is not a valid move.')
            
            # Move token on board
            new_token_position = selected_token + spaces
            board[selected_token][index].pop()
            board[new_token_position][index].append(player)

            # Send opponent's token back if landed on
            if 5 <= new_token_position <= 12 and board[new_token_position][opponent_index]:
                board[new_token_position][opponent_index].pop()
                board[0][opponent_index].append(PLAYERS[opponent_index])
            
            # If player lands on flower square, player gets another turn
            if new_token_position in FLOWER_SQUARES:
                print(f'{player} landed on a flower space and goes again.')
                input('Press Enter to continue...')
                continue

            if len(board[15][index]) == 7:
                print(f'Player {player} has won the game!\nThanks for playing!')
                sys.exit()
            
            break