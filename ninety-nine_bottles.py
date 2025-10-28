# Ninety-Nine Bottles

import sys
import time

PAUSE = 1.5

try:
    for i in range(99, 1, -1):
        print(f"{i} bottles of milk on the wall,")
        time.sleep(PAUSE)
        print(f"{i} bottles of milk,")
        time.sleep(PAUSE)
        print(f"Take one down, pass it around,")
        time.sleep(PAUSE)
        print(f"{i - 1} {'bottles' if i > 2 else 'bottle'} of milk on the wall!")
        time.sleep(PAUSE)
        print()
        
    print('One bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('One bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    sys.exit()