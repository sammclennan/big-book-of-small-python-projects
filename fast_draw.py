# Tests your reflex time. User must press Enter as quickly as possible after seeing the word 'DRAW' appear on the screen. User loses if too slow or presses Enter before the word appears

import random
import sys
import time

min_wait = 5
max_wait = 10

print("""Time to test your reflexes and see if you are the fastest draw in the west! When you see "DRAW", you have 0.3 seconds to press Enter, but you lose if you press Enter before "DRAW" appears.""")

while True:
    print('It is high noon...')

    # Pause before draw
    time.sleep(random.randint(min_wait, max_wait))

    print("DRAW!")

    # Start and stop timer, calculate reaction time
    start = time.time()
    input()
    reaction_time = round(time.time() - start, 4)

    # Print message
    if reaction_time < 0.001:
        print('You pressed enter before "DRAW"! You lose!')
    else:
        print(f'You took {reaction_time} seconds to draw. {'Nice!' if reaction_time < 0.3 else 'Too slow!'}')

    print('Enter QUIT to stop, or press Enter to play again.')
    if input('> ').upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()