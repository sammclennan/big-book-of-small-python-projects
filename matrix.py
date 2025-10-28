# Prints a matrix-style stream of 'digital rain' to the terminal

import os
import random
import sys
import time

width = os.get_terminal_size()[0]

lastRow = ''
newRow = ''

for col in range(width):
    lastRow += random.choice((' ',) * 100 + ('0', '1'))

print('Ctrl + C to quit')
time.sleep(2)

print(lastRow)

try:
    while True:
        for col in range(width):
            if lastRow[col] == ' ':
                newRow += random.choice((' ',) * 100 + ('0', '1'))
            elif lastRow[col] in ('1', '0'):
                newRow += random.choice(('0', '1') * 2 + (' ',))
        print(newRow)

        lastRow = newRow
        newRow = ''

        time.sleep(0.1)

except KeyboardInterrupt:
    print('Program stopped by user')
    sys.exit()