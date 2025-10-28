# Cho-Han. Japanese dice game. Two six-sided dice are rolled in a cup, and players must guess if the sum is even (Cho), or odd (Han).

import random
import sys

JAPANESE_NUMS = {1: 'Ichi', 2: 'Ni', 3: 'San', 4: 'Yon', 5: 'Go', 6: 'Roku'}

print('In this traditional Japanese dice game, two dice are rolled in a bamboo cup by the dealer sitting on the floor. The player must guess if the dice total to an even (丁) or odd (半) number.')

print('You have 5000 文. How much do you want to be t? (or QUIT)')

while True:
    try: 
        bet = input('> ')
        if bet.lower() in ('q', 'quit'):
            print('Goodbye')
            sys.exit()
        bet = int(bet)
        if 1 <= bet <= 5000:
            break
        else:
            print('You can only bet between 1 and 5000 文.')
    except ValueError:
        print('Please enter an integer number!')
    
print('The dealer swirls the cup and you hear the rattle of dice. The dealer slams the cup on the floor, still covering the dice, and asks for your bet.')

print("Even ('丁' or 'Cho') or odd ('半' or 'Han')?")

while True:
    choice = input('> ').lower()
    if choice in ('丁', '半', 'cho', 'han'):
        break
    else:
        print("Please choose between '丁' or 'Cho' for even and '半' or 'Han' for odd.")

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)

print('The dealer lifts the cup to reveal:')

print(f'{JAPANESE_NUMS[dice_1]:^4} - {JAPANESE_NUMS[dice_2]:^4}')
print(f'{dice_1:^4} - {dice_2:^4}')

if (choice in ('丁', 'cho') and (dice_1 + dice_2) % 2 == 0) or (choice in ('半', 'han') and (dice_1 + dice_2) % 2 == 1):
    print(f'You won! You take {bet * 2} 文!\nThe house takes a {int(bet * 0.05)} 文 fee.')
else:
    print(f'You lost! You lose {bet} 文!')