# Vigenere cipher

from string import ascii_lowercase
try:
    import pyperclip
except ImportError:
    pass


def encrypt_decrypt(message, key, direction):
    """Encrypts/decrypts text using a Vigenere cipher."""
    key_indices = [ascii_lowercase.find(letter) for letter in key]

    new_text = []

    i = 0
    for j in range(len(message)):
        if message[j].isalpha():
            char_index = ascii_lowercase.find(message[j].lower())
            new_index = (char_index + key_indices[i] if direction == 'encrypt' else char_index - key_indices[i]) % 26
            
            new_char = ascii_lowercase[new_index]
            if message[j].isupper(): new_char = new_char.upper()
            new_text.append(new_char)

            i = (i + 1) % len(key_indices)
        else:
            new_text.append(message[j])

    return ''.join(new_text)


def main():
    # Get translation direction from user
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    while True:
        response = input('> ').strip().lower()
        if response in ('e', 'd'):
            direction = 'encrypt' if response == 'e' else 'decrypt'
            break
        else:
            print("Please enter 'e' to encrypt or 'd' to decrypt.")

    # Get encryption key from user
    print('Please specify the key to use.\nIt can be a word or any combination of letters:')
    while True:
        key = input('> ').strip().lower()
        if key.isalpha():
            break
        else:
            invalid_chars = {char for char in key if not char.isalpha()}
            print(f'Key cannot contain characters: {''.join(invalid_chars)}')

    # Get message to translate from user
    print(f'Please enter the message to {direction}.')
    message = input('> ')

    # Translate text
    new_text = encrypt_decrypt(message, key, direction)

    print(f'{direction.title()}ed message:')
    print(new_text)
    try:
        pyperclip.copy(new_text)
        print(f'{direction.title()}ed text copied to clipboard.')
    except:
        pass


if __name__ == '__main__':
    main()


