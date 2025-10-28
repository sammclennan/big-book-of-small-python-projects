# Three-card monte

import os
import random
import time

SWAPS = 15
PAUSE = 1
SUITS = ['♣', '♦', '♥', '♠']
RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def display_cards(cards):
    for i in range(len(cards)):
        print(' ___ ', end=' ')
    print()
    for i in range(len(cards)):
        print(f'|{cards[i][1]:<2} |', end=' ')
    print()
    for i in range(len(cards)):
        print(f'| {cards[i][0]} |', end=' ')
    print()
    for i in range(len(cards)):
        print(f'|_{cards[i][1]:_>2}|', end=' ') # TODO
    print()
    

cards = {('♥', 'Q')}

# Draw random cards
while len(cards) < 3:
    card = (random.choice(SUITS), random.choice(RANK))
    if card != ('♥', 'Q'):
        cards.add(card)

cards = list(cards)

print('Find the Queen of Hearts! Keep an eye on how the cards move.')
print('Here are the cards:')
display_cards(cards)
input('Press enter when you are ready to start...')

# Swap cards
for i in range(SWAPS):
    x = random.randint(1, 3)
    if x == 1:
        cards[0], cards[1] = cards[1], cards[0]
        print('swapping left and middle...' if random.randint(0, 1) else 'swapping middle and left...')
    elif x == 2:
        cards[0], cards[2] = cards[2], cards[0]
        print('swapping left and right...' if random.randint(0, 1) else 'swapping right and left...')
    else:
        cards[1], cards[2] = cards[2], cards[1]
        print('swapping right and middle...' if random.randint(0, 1) else 'swapping middle and right...')
    
    time.sleep(PAUSE)

os.system('cls' if os.name == 'nt' else 'clear')

# Get user response
while True:
    print('Which card has the Queen of Hearts? (LEFT, MIDDLE, or RIGHT)')
    response = input('> ').strip().upper()
    if response in ('LEFT', 'MIDDLE', 'RIGHT'):
        if response == 'LEFT':
            response = 0
        elif response == 'MIDDLE':
            response = 1
        else:
            response = 2
        break

display_cards(cards)
if cards[response] == ('♥', 'Q'):
    print('You won!\nThanks for playing!')
else:
    print('Sorry!\nBetter luck next time!')

