
import random
import sys
import time

PAUSE = 1
BEATS = {
    'ROCK': 'SCISSORS',
    'PAPER': 'ROCK',
    'SCISSORS': 'PAPER'
}

def get_player_choice():
    while True:
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        player_choice = input('> ').strip().upper()
        if player_choice in ('Q', 'QUIT'):
            print('Thanks for playing!')
            sys.exit()
        elif player_choice in ('R', 'P', 'S', 'ROCK', 'PAPER', 'SCISSORS'):
            return player_choice
        

def play_again():
    while True:
        print('Do you want to play again? (Y/N)')
        play_again = input('> ').strip().upper()
        if play_again in ('Y', 'YES'):
            return True
        elif play_again in ('N', 'NO'):
            return False


def main():
    print('PAPER, SCISSORS, ROCK')
    print('- Rock beats Scissors.\n- Paper beats Rock.\n- Scissors beats Paper.')

    wins, losses, ties = 0, 0, 0
    
    while True:
        player_choice = get_player_choice()

        if player_choice not in BEATS:
            player_choice = {'R': 'ROCK', 'P': 'PAPER', 'S': 'SCISSORS'}[player_choice]
        
        computer_choice = BEATS[player_choice]

        print(f'{player_choice} versus')
        time.sleep(PAUSE)
        for i in range(1, 4):
            print(f'{i}...')
            time.sleep(PAUSE)
        print(f'{computer_choice}')
        time.sleep(PAUSE)

        if player_choice == computer_choice:
            ties += 1
            print("It's a tie!")
        elif BEATS[player_choice] == computer_choice:
            wins += 1
            print('You win!')
        else:
            losses += 1
            print('You lose!')
        
        print(f'{wins} Wins, {losses} Losses, {ties} Ties')

        if not play_again:
            print('Thanks for playing!')
            sys.exit()

if __name__ == '__main__':
    main()