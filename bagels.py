# Bagels. Player must guess 3-digit number based on clues
import random

again = True

while again:
    print("""I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:     That means:
    Pico          One digit is correct but in the wrong position.
    Fermi         One digit is correct and in the right position.
    Bagels        No digit is correct.
I have thought up a number.
You have 10 guesses to guess it.""")  

    num = '701' # str(random.randint(100, 999))

    for attempt in range(1, 11):
        print(f'Guess #{attempt}')

        while True:
            guess = input()
            if guess.isnumeric() and len(guess) == 3:
                break
            else:
                print('Please enter a 3-digit number')

        if guess == num:
            print('You got it!')
            break
        else:
            hits = 0
            for i in range(len(num)):
                if guess[i] == num[i]:
                    print('Fermi', end=' ')
                    hits += 1
                elif guess[i] in num:
                    print('Pico', end=' ')
                    hits += 1
            if not hits:
                print('Bagels', end = '')
            print()
    
    else:
        print('Better luck next time!')

    print('Do you want to play again? (yes or no)')
    while True:
        play_again = input().lower()
        if play_again in ('y', 'ye', 'yes'):
            again = True
            break
        if play_again in ('n', 'no', 'nop', 'nope'):
            again = False
            break
        else:
            print('Invalid input!')
        
print('Thanks for playing!')


