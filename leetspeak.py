# Converts English text to Leetspeak

import random

import pyperclip

def main():
    text = input('Enter text to convert into Leetspeak: ')

    character_dict = {
        'A': ('A', 'a', '4', '@', 'Д'),
        'B': ('B', 'b', 'ß'),
        'C': ('C', 'c', '¢', '©'),
        'D': ('D', 'd', '|)', '[)'),
        'E': ('E', 'e', '3', '€'),
        'F': ('F', 'f', 'ƒ', '/=', 'ph'),
        'G': ('G', 'g', '(_+'),
        'H': ('H', 'h', '#', '/-/', '\\-\\'),
        'I': ('I', 'i', '1', '!'),
        'J': ('J', 'j', 'j', '_|', ']'),
        'K': ('K', 'k', '|<', '1<'),
        'L': ('L', 'l', '1', '|_'),
        'M': ('M', 'm', '/V\\', '|\\/|'),
        'N': ('N', 'n', 'ท', '/\\/'),
        'O': ('O', 'o', '0', '()', 'Ø'),
        'P': ('P', 'p', '⁋', '|*'),
        'Q': ('Q', 'q', '¶'),
        'R': ('R', 'r', 'Я'),
        'S': ('S', 's', '$', '5', '§'),
        'T': ('T', 't', '7', '+', '†'),
        'U': ('U', 'u', 'บ', '|_|'),
        'V': ('V', 'v', '\\/', '|/'),
        'W': ('W', 'w', '₩', 'ω', 'vv', '\\^/'),
        'X': ('X', 'x', '><', '}{'),
        'Y': ('Y', 'y', '¥', '`/'),
        'Z': ('Z', 'z', '2', '7_')
    }

    leet_text = ''

    for char in text:
        if char.upper() in character_dict:
            leet_text += random.choice(character_dict[char.upper()])
        else:
            leet_text += char

    print(leet_text)

    try:
        pyperclip.copy(leet_text)
        print('Text copied to clipboard.')
    except pyperclip.PyperclipException:
        print('Could not copy text to clipboard. Make sure pyperclip is installed.')

if __name__ == '__main__':
    main()