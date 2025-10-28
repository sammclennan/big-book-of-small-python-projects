# Hacking minigame

import random
import sys

GARBAGE_CHARS = '!@#$%^&*()[]{}|+-=:;_<>,.?/~'

# Function to draw computer memory art
def draw_memory_string(words, chars):
    col_1_index = 4432
    col_2_index = 4688
    memory_words = words + [''] * 4
    random.shuffle(memory_words)
    for i in range(len(memory_words)):
        print(hex(col_1_index + i // 2 if i % 2 == 0 else col_2_index + i // 2), end='  ')
        word_pos = random.randrange(10)
        for j in range(10):
            if j == word_pos:
                if memory_words[i]:
                    print(memory_words[i], end='')
                else:
                    for k in range(7):
                        print(random.choice(chars), end='')
            else:
                print(random.choice(chars), end='')
        print('    ', end='')
        if i % 2 != 0:
            print('')

file_name = 'sevenletterwords.txt'

# Open text file
try:
    with open(file_name) as text_file:
        all_words = [line.strip().upper() for line in text_file.readlines()]
except FileNotFoundError:
    print(f'Error: File {file_name} does not exist')

if len(all_words) > 10:
    word_sample = random.sample(all_words, 10)
else:
    print(f'Length of {file_name} is less than 10')
    sys.exit
password = random.choice(word_sample)

draw_memory_string(word_sample, GARBAGE_CHARS)
print("Find the password in the computer's memory:")

tries = 6

# Prompt user to guess password while tries remain
while tries > 0:
    while True:
        guess = input(f'Enter password: ({tries} tries remaining)\n> ').upper()
        if not guess:
            print('Please enter a value!')
        else:
            break

    if guess == password:
        print('A C C E S S   G R A N T E D')
        sys.exit()
    else:
        hits = 0
        for i in range(len(password)):
            if i < len(guess):
                if guess[i] == password[i]:
                    hits += 1
        draw_memory_string(word_sample, GARBAGE_CHARS)
        print(f'Access denied ({hits}/{len(password)} correct)')
        tries -= 1

print(f'Out of tries. The password was {password}.')
