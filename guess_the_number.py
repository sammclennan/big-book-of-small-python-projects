# Guess the number

import sys
import random

print("I'm thinking of a number between 1 and 100")

target_number = random.randint(1, 100)
guesses_left = 10

# While guesses remain
while guesses_left > 0:
    while True:
        try:
            guess = int(input(f'You have {guesses_left} guesses left. Take a guess\n> '))
            if 1 <= guess <= 100:
                break
            else:
                print('Please enter a number between 1 and 100!')
        except ValueError:
            print('Invalid input! Please enter a number between 1 and 100!')

    if guess == target_number:
        print(f'Correct! The number was {target_number}')
        sys.exit()
    elif guess < target_number:
        print('Your guess is too low')
    else:
        print('Your guess is too high')
    
    guesses_left -= 1

print(f'Sorry! You ran out of guesses. The number was {target_number}')