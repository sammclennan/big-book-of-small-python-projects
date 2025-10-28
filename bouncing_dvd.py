# Bouncing DVD screensaver

import sys
import random
import time
import bext


WIDTH = bext.size()[0] - 1
HEIGHT = bext.size()[1] - 2
COLORS = ('black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white')


text = 'DVD'
logo_count = 10
logos = []

for i in range(logo_count):
    logos.append({'x': random.randint(1, WIDTH - len(text)), 'y': random.randint(1, HEIGHT), 'down': random.randint(0, 1), 'right': random.randint(0, 1), 'color': random.choice(COLORS)})


def main():
    bext.clear()
    print('Bouncing DVD screensaver. Press Ctrl + C to quit.')
    while True:
        for logo in logos:
            # Clear logo from current coords
            bext.goto(logo['x'], logo['y'])
            print(' ' * len(text), end='')

            # Set logo to random color on edge bounce
            if logo['x'] in (0, WIDTH - len(text)) or logo['y'] in (1, HEIGHT):
                logo['color'] = random.choice(COLORS)

            # x-cord bounce
            if logo['x'] == 0:
                logo['right'] = True
            if logo['x'] == WIDTH - len(text):
                logo['right'] = False

            # New x-cord
            if logo['right']:
                logo['x'] += 1
            else:
                logo['x'] -= 1

            # y-cord bounce
            if logo['y'] == 1:
                logo['down'] = True
            if logo['y'] == HEIGHT:
                logo['down'] = False

            # New y-cord
            if logo['down']:
                logo['y'] += 1
            else:
                logo['y'] -= 1

            # Go to new coords and print logo
            bext.goto(logo['x'], logo['y'])
            bext.fg(logo['color'])
            print(text)

        time.sleep(0.05)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        bext.clear()
        print('Program interrupted by user.')
        sys.exit()