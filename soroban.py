# Japanese Soroban simulator

import sys

SOROBAN_COLUMNS = {
    0: ['0', '|', '|', '=', '|', '|', '|', '0', '0', '0', '0'],
    1: ['0', '|', '|', '=', '0', '|', '|', '|', '0', '0', '0'],
    2: ['0', '|', '|', '=', '0', '0', '|', '|', '|', '0', '0'],
    3: ['0', '|', '|', '=', '0', '0', '0', '|', '|', '|', '0'],
    4: ['0', '|', '|', '=', '0', '0', '0', '0', '|', '|', '|'],
    5: ['|', '|', '0', '=', '|', '|', '|', '0', '0', '0', '0'],
    6: ['|', '|', '0', '=', '0', '|', '|', '|', '0', '0', '0'],
    7: ['|', '|', '0', '=', '0', '0', '|', '|', '|', '0', '0'],
    8: ['|', '|', '0', '=', '0', '0', '0', '|', '|', '|', '0'],
    9: ['|', '|', '0', '=', '0', '0', '0', '0', '|', '|', '|'],
}

ADD_SUBTRACT_KEYS = {
    'q': 1000000000,
    'w': 100000000,
    'e': 10000000,
    'r': 1000000,
    't': 100000,
    'y': 10000,
    'u': 1000,
    'i': 100,
    'o': 10,
    'p': 1,
    'a': -1000000000,
    's': -100000000,
    'd': -10000000,
    'f': -1000000,
    'g': -100000,
    'h': -10000,
    'j': -1000,
    'k': -100,
    'l': -10,
    ';': -1,
}


def get_place_values(n):
    """Convert integer into a list of place values."""
    n = str(min(n, 9999999999))
    n = n.zfill(10)
    return [int(digit) for digit in n]


def draw_soroban(digit_list):
    """Draw ASCII Soroban."""
    print(digit_list)
    print('+' + '-' * 32 + '+')
    for i in range(10):
        print('+' if i == 3 else 'I' , end='')
        for j in digit_list:
            print(('==' if i == 3 else '  ') + SOROBAN_COLUMNS[j][i], end='')
        print(('==' if i == 3 else '  ') + ('+' if i == 3 else  'I'))
    print('+', end='')
    for i in digit_list:
        print('==' + str(i), end='')
    print('==+')
    print('  +q  w  e  r  t  y  u  i  o  p')
    print('  -a  s  d  f  g  h  j  k  l  ;')
    

def main():
    number = 0

    while True:
        draw_soroban(get_place_values(number))

        # Get user input
        while True:
            print('Enter a number or a stream of up/down letters (or QUIT).')
            choice = input('> ').strip().lower()
            if choice == 'quit':
                sys.exit()
            elif choice.isdecimal():
                number = int(choice)
                break
            else:
                for char in choice:
                    if char in ADD_SUBTRACT_KEYS:
                        number += ADD_SUBTRACT_KEYS[char]
                break

        # Soroban cannot display negative values
        number = max(number, 0)


if __name__ == '__main__':
    main()