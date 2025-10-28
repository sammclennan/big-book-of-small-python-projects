# Moving sinewave message generator

import math
import os
import sys
import time

TERMINAL_WIDTH = os.get_terminal_size()[0]
PAUSE = 0.1
STEP = 0.2


while True:
    print(f'Enter message to display? (Max {TERMINAL_WIDTH // 2} chars)')
    message = input('> ').strip()
    if 0 < len(message) < TERMINAL_WIDTH // 2:
        break
    else:
        print('Please enter a valid message.')

try:
    print('Press Ctrl + C to exit.')
    step = 0
    while True:
        padding = int((math.sin(step) + 1) / 2 * (TERMINAL_WIDTH - len(message)))
        print(' ' * padding + message)
        step += STEP
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
