# Creates an endless animation of a winding cave

import random
import sys
import time

TOTAL_WIDTH = 70

tunnel_width = 10
left_dist = 25

print('Press Ctrl + C to quit')
time.sleep(2)

try:
    while True:
        print('#' * left_dist + ' ' * tunnel_width + '#' * (TOTAL_WIDTH - tunnel_width - left_dist))

        direction = random.randint(0, 1)
        if direction == 0 and left_dist > 1:
            left_dist -= 1
        elif left_dist < TOTAL_WIDTH - (tunnel_width + 1):
            left_dist += 1

        width_change = random.randint(0, 5)
        if width_change == 0 and tunnel_width > 3:
            tunnel_width -= 1
        elif width_change == 1 and tunnel_width < TOTAL_WIDTH - (left_dist + 1):
            tunnel_width += 1
            
        time.sleep(0.05)

except KeyboardInterrupt:
    print('Program stopped by user')
    sys.exit()