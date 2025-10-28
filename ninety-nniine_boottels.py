# In this version of the song “Ninety-Nine Bottles,” the program introduces small imperfections in each stanza by either removing a letter, swapping the casing of a letter, transposing two letters, or doubling a letter.

import random
import sys
import time

PAUSE = 1.5


def remove_letter(text):
    x = random.choice([i for i in range(1, len(text)) if text[i].isalpha()])
    new_text = text[:x] + ' ' + text[x + 1:]   
    return new_text

def swap_case(text):
    x = random.choice([i for i in range(1, len(text)) if text[i].isalpha()])
    new_text = text[:x] + (text[x].upper() if text[x].islower() else text[x].lower()) + text[x + 1:]
    return new_text

def transpose_letters(text):
    x, y = random.sample([i for i in range(1, len(text)) if text[i].isalpha()], 2)
    new_text = list(text)
    new_text[x], new_text[y] = new_text[y], new_text[x]
    return ''.join(new_text)

def double_letter(text):
    x = random.choice([i for i in range(1, len(text)) if text[i].isalpha()])
    new_text = text[:x] + text[x] * 2 + text[x + 1:]
    return new_text


song_lines = [
    ' bottles of beer on the wall,',
    ' bottles of beer,',
    'Take one down, pass it around',
    ' bottles of beer on the wall!',
]

alter_text = [
    remove_letter,
    swap_case,
    transpose_letters,
    double_letter,
]

try:
    print('Press Ctrl + C to quit.')
    for i in range(99, 0, -1):
        print(str(i) + song_lines[0])
        time.sleep(PAUSE)
        print(str(i) + song_lines[1])
        time.sleep(PAUSE)
        print(song_lines[2])
        time.sleep(PAUSE)
        print(str(i - 1) + song_lines[3] if i > 1 else 'No more bottles of beer on the wall!')
        time.sleep(PAUSE)
        print()
        func = alter_text[random.randint(0, 3)]
        line_to_change = random.randint(0, 3)
        song_lines[line_to_change] = func(song_lines[line_to_change])

except KeyboardInterrupt:
    sys.exit