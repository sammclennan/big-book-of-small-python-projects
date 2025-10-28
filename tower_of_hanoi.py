# Tower of Hanoi puzzle game

import sys

HEIGHT = 7
POLE = '||'
DISC = '@'

def get_move():
    """Get valid move from player."""
    while True:
        print('Enter the letters of towers to move disks. (or QUIT)')
        print('(e.g.) enter AB to move a disk from tower A to tower B.')
        choice = input('> ').strip().upper()
        if choice == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif choice in ('AB', 'AC', 'BC', 'CB', 'CA', 'BA'):
            return choice[0], choice[1]


def draw_towers(towers):
    """Display tower graphics."""
    total_width = HEIGHT * 2 + len(POLE)

    print('||'.center(total_width) * 3)

    for i in range(HEIGHT - 1, -1, -1):
        for letter in towers.keys():
            if len(towers[letter]) > i:
                disc_size = towers[letter][i]
                print(f'{DISC * disc_size}_{disc_size}{DISC * disc_size}'.center(total_width), end='')
            else:
                print('||'.center(total_width, ' '), end='')
        print()
        
    for letter in 'A', 'B', 'C':
        print(letter.center(total_width), end='')
    print()


def main():
    towers = {
        'A': list(range(HEIGHT, 0, -1)),
        'B': [],
        'C': [],
    }

    print('Move the tower of disks, one at a time, to another tower. Larger disks cannot rest on top of a smaller disk.')

    while True:
        draw_towers(towers)

        # Check for winning condition
        if len(towers['B']) == HEIGHT or len(towers['C']) == HEIGHT:
            print('You solved the puzzle! Well done!')
            sys.exit()

        # Get move from player
        while True:
            move_from, move_to = get_move()
            if not towers[move_from]:
                print('You must pick a tower with disks.')
            elif towers[move_to] and towers[move_from][-1] > towers[move_to][-1]:
                print("You can't put larger disks on top of smaller ones.")
            else:
                break
        
        # Shift discs
        disk = towers[move_from].pop()
        towers[move_to].append(disk)


if __name__ == '__main__':
    main()