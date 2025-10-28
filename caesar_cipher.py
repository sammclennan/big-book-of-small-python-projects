# Caesar cipher. Encipher or decipher text by a key provided by user

import pyperclip

# Prompt user to encrypt or decrypt
while True:
    direction = input('Do you want to (e)ncrypt or (d)ecrypt? ').lower()
    if direction in ('d', 'e'):
        break
    else:
        print("Please enter 'e' to encrypt or 'd' to decrypt.")

# Get encryption key
while True:
    try:
        key = int(input('Enter key (0 - 25): '))
        if 0 <= key <= 25:
            break
        else:
            print('Key must be between 0 and 25!')
    except ValueError:
        print('Please enter an integer value!')

if direction == 'd': key = key  * -1

# Get message to encrypt or decrypt
message = input(f'Enter message to {"encrypt" if direction == 'e' else "decrypt"}: ')

ciphertext = ''

# Loop through text
for char in (message):
    # Append alphabetic character +/- key to ciphertext
    if char.isalpha():
        if char.isupper():
            new_char = chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            new_char = chr((ord(char) - 97 + key) % 26 + 97)
        ciphertext += new_char
    else:
        ciphertext += char

print(ciphertext)

# Copy ciphertext to clipboard
pyperclip.copy(ciphertext)

print(f'{'Encrypted' if direction == 'e' else 'Decrypted'} text copied to clipboard.')
