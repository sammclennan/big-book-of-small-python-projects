# Carpet pattern from 'The Shining'

import os

TERMINAL_WIDTH, TERMINAL_HEIGHT = os.get_terminal_size()

PATTERN = [
    r'_ \ \ \_/ __',
    r' \ \ \___/ _',
    r'\ \ \_____/ ',
    r'/ / / ___ \_',
    r'_/ / / _ \__',
    r'__/ / / \___',
]

for i in range(TERMINAL_HEIGHT // len(PATTERN)):
    for row in PATTERN:
        for j in range(TERMINAL_WIDTH // len(PATTERN[0])):
            print(row, end='')
        print()