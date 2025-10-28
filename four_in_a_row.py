# connect four 2-player game

import sys

# Function to draw board
def draw_board(grid):
    print(" 1234567")
    print("+-------+")
    for i in range(len(grid) - 1, -1, -1):
        print('|' + ''.join(grid[i]) + '|')
    print("+-------+")

# Function to prompt player for column
def get_column(player):
    while True:
        column_no = input(f"Player {player}, enter a column (1-7) or QUIT: ")
        if column_no.upper == 'QUIT':
            'Game Over'
            sys.exit()
        try:
            column_no = int(column_no)
            if 1 <= column_no <= 7:
                break
            else:
                print('Column must be within range 1-7!')
        except ValueError:
            print('Please enter a number between 1 and 7, or type QUIT')

    return column_no


# Create 2D array
grid = [['.' for i in range(7)] for j in range(6)]

draw_board(grid)

while True:
    player_x = get_column('X')

    for i in range(len(grid)):
        if grid[i][player_x - 1] == '.':
            grid[i][player_x - 1] = 'X'
            break
        if i == 5:
            print('This column is full! Please choose another')

    draw_board(grid)

    player_o = get_column('Y')

    for i in range(len(grid)):
        if grid[i][player_o - 1] == '.':
            grid[i][player_o - 1] = 'O'
            break
        if i == 5:
            print('This column is full! Please choose another')

    draw_board(grid)




#     while True:
#         player_x = input("Player X, enter a column (1-7) or QUIT")
#         if player_x.upper == 'QUIT':
#             'Game Over'
#             sys.exit()
#         elif player_x not in ('1', '2', '3', '4', '5', '6', '7'):
#             print('Column must be within range 1-7!')
#         else:
#             break

# while True:
#     while True:
#         player_x = input("Player X, enter a column (1-7) or QUIT: ")
#         if player_x.upper == 'QUIT':
#             'Game Over'
#             sys.exit()
#         try:
#             player_x = int(player_x)
#             if 1 <= player_x <= 7:
#                 break
#             else:
#                 print('Column must be within range 1-7!')
#         except ValueError:
#             print('Please enter a number between 1 and 7, or type QUIT')
    


