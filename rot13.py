# ROT13 cipher

import string
import sys

try:
    import pyperclip
except ImportError:
    pass

LETTERS = string.ascii_lowercase


def rot_13_cipher(message):
    result = []

    for char in message:
        if char.isalpha():
            rot_13_char = LETTERS[(LETTERS.index(char.lower()) + 13) % 26]
            result.append(rot_13_char.lower() if char.islower() else rot_13_char.upper())
        else:
            result.append(char)

    return ''.join(result)


def main():
    while True:
        print('Enter a message to encrypt/decrypt (or QUIT):')
        message = input('> ')
        if message.upper() in ('Q', 'QUIT'):
            sys.exit()
        if not message:
            continue

        ciphertext = rot_13_cipher(message)
        print(ciphertext)

        try:
            pyperclip.copy(ciphertext)
            print('Text copied to clipboard.')
        except pyperclip.PyperclipException:
            print('Could not copy text to clipboard. Make sure pyperclip is installed.')

if __name__ == '__main__':
    main()
