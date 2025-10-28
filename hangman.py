# Hangman

import json
import random
import sys


# Draw hangman and print word status
def draw_hangman():
    for row in HANGMAN_ARRAY:
        print(''.join(row))
    print(f'The category is: {category}.')
    print(f'Missed letters: {' '.join(missed_letters)}')
    for i in progress:
        print(i, end=' ')
    print()


# Prompt player to guess letter
def get_letter():
    while True:
        guess = input('Guess a letter.\n').upper()
        if not (guess.isalpha() and len(guess) == 1):
            print('Invalid input! Please enter a single letter!')
        elif guess in missed_letters or guess in progress:
            print('You already guessed that letter!')
        else:
            break
    return guess


HANGMAN_ARRAY = [
    [' ', '+', '-', '-', '+'],
    [' ', '|', ' ', ' ', '|'],
    [' ', ' ', ' ', ' ', '|'],
    [' ', ' ', ' ', ' ', '|'],
    [' ', ' ', ' ', ' ', '|'],
    [' ', ' ', ' ', ' ', '|'],
    ['=', '=', '=', '=', '=']
]

# Load JSON data
with open('hangman_words.json', 'r') as file:
    word_data = json.load(file)

category = random.choice(list(word_data.keys()))
word = random.choice(word_data[category]).upper()
progress = ['_'] * len(word)
missed_letters = []

print('Hangman')

while True:
    draw_hangman()

    guess = get_letter()

    # Add guess to word progress or incorrect letters
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                progress[i] = guess
    else:
        missed_letters.append(guess)
    
    # Add body parts to hang man
    if len(missed_letters) == 1:
        HANGMAN_ARRAY[2][1] = 'O'
    elif len(missed_letters) == 2:
        HANGMAN_ARRAY[3][1] = '|'
    elif len(missed_letters) == 3:
        HANGMAN_ARRAY[3][0] = '/'
    elif len(missed_letters) == 4:
        HANGMAN_ARRAY[3][2] = '\\'
    elif len(missed_letters) == 5:
        HANGMAN_ARRAY[4][0] = '/'
    elif len(missed_letters) == 6:
        HANGMAN_ARRAY[4][2] = '\\'
        draw_hangman()
        print(f"You're dead! The secret word was {word}")
        sys.exit()

    # If player guesses word
    if ''.join(progress) == word:
        for i in progress:
            print(i, end=' ')
        print()
        print(f'Yes! The secret word is {word}!')
        sys.exit()












