# Simple substitution cipher

import random
import string

try:
    import pyperclip
except ImportError:
    pass

LETTERS = string.ascii_uppercase


def translate_text(text, key, encrypt):
    ciphertext = []
    for char in text:
        if char.isalpha():
            if encrypt:
                i = LETTERS.index(char.upper())
                ciphertext.append(key[i] if char.isupper() else key[i].lower())
            else:
                i = key.index(char.upper())
                ciphertext.append(LETTERS[i] if char.isupper() else LETTERS[i].lower())
        else:
            ciphertext.append(char)

    return ''.join(ciphertext)


def main():
    print('A simple substitution cipher has a one-to-one translation for each symbol in the plaintext and each symbol in the ciphertext.')

    # Get translation direction
    print('Do you want to (e)ncrypt of (d)ecrypt?')
    while True:
        choice = input('> ').strip().upper()
        if choice == ('E', 'D'):
            encrypt = True if choice == 'E' else False
            break
        else:
            print("Please enter 'e' to encrypt or 'd' to decrypt.")

    # Get encryption key
    print(f'Please specify the key to use. {'Or enter RANDOM to have one generated for you.' if encrypt else ''}')
    while True:
        key = input().strip().upper()
        if key == 'RANDOM' or (len(key) == 26 and key.isalpha() and len(key) == len(set(key))):
            break
        else:
            print(f'Key must consist of 26 unique letters corresponding to letters of the alphabet. Enter RANDOM to generate a random key.')

    # Generate random key
    if key == 'RANDOM':
        key = list(LETTERS)
        random.shuffle(key)
        key = ''.join(key)
        print(f'The key is {key}. KEEP THIS SECRET!')

    # Get message to translate
    while True:
        print(f'Enter the message to {'encrypt' if encrypt else 'decrypt'}.')
        text = input('> ').strip()
        if text:
            break

    # Translate text
    translated_text = translate_text(text, key, encrypt)

    print(f'The {'encrypted' if encrypt else 'decrypted'} message is:')
    print(translated_text)

    # Copy translated text to clipboard
    try:
        pyperclip.copy(translated_text)
        print(f'Full {'encrypted' if encrypt else 'decrypted'} text copied to clipboard.')
    except pyperclip.PyperclipException:
        print('Could not copy text to clipboard. Make sure pyperclip is installed.')


if __name__ == '__main__':
    main()