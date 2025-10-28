# Performs a brute-force attack on Caesar-ciphered message.

# Get encrypted message
message = input('Enter the encrypted Caesar cipher message to hack: ')

# Try one key at a time
for i in range(26):
    new_message = ''
    # Loop through message
    for char in message:
        # Append alphabetic character - key to new string
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - 65 - i) % 26 + 65)
            else:
                new_char = chr((ord(char) - 97 - i) % 26 + 97)
            new_message += new_char
        else:
            new_message += char
    print(f'Key {i}: {new_message}')