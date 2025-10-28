# The Monty Hall Problem illustrates a surprising fact of probability. The problem is loosely based on the old game show Let’s Make a Deal and its host, Monty Hall. In the Monty Hall Problem, you can pick one of three doors. Behind one door is a prize: a new car. Each of the other two doors opens onto a worthless goat. Say you pick Door #1. Before the door you choose is opened, the host opens another door (either #2 or #3), which leads to a goat. You can choose to either open the door you originally picked or switch to the other unopened door.

import random
import sys

BLANK = [
    "+------+",
    "|      |",
    "|   x  |",
    "|      |",
    "|      |",
    "|      |",
    "+------+",
]

CAR = [
    "+------+",
    "| CAR! |",
    "|    __|",
    "|  _/  |",
    "| /_ __|",
    "|   O  |",
    "+------+",
]

GOAT = [
    "+------+",
    "|  ((  |",
    "|  oo  |",
    "| /_/|_|",
    "|    | |",
    "|GOAT|||",
    "+------+",
]


def draw_doors(doors, door_graphics, open_doors=[]):
    for i in range(len(BLANK)):
        for j in range(len(doors)):
            print(door_graphics[doors[j]][i] if j in open_doors else BLANK[i].replace('x', str(j + 1)), end=' ')
        print()
        

def prompt_player(options):
    options = [x.upper() for x in options]
    while True:
        player_choice = input('> ').upper()
        if player_choice in options:
            return player_choice
        elif player_choice in ('Q', 'QUIT'):
            print('Thanks for playing!')
            sys.exit()
        else:
            print(f'Please choose from ({', '.join(options)}) or QUIT to exit.')

def monty_hall_game():
    doors = ['Car'] + ['Goat'] * 2
    door_graphics = {
        'Car': CAR,
        'Goat': GOAT
    }

    swap_wins = 0
    swap_losses = 0
    no_swap_wins = 0
    no_swap_losses = 0

    print('The Monty Hall Problem')
    while True:
        # Shuffle door contents
        random.shuffle(doors)

        draw_doors(doors, door_graphics)

        # Prompt player to choose door
        print('Pick a door (1, 2, 3) or QUIT to exit:')
        door_choice = int(prompt_player(('1', '2', '3'))) - 1

        # Open one of remaining goat doors
        open_door = next(x for x in range(len(doors)) if x != door_choice and doors[x] != 'Car')

        draw_doors(doors, door_graphics, [open_door])

        # Prompt player to swap doors
        print(f'Door {open_door + 1} contains a {doors[open_door]}!')
        print('Do you want to swap doors? Y/N')
        swap_doors = prompt_player(('Y', 'N'))
        if swap_doors == 'Y':
            door_choice = next(x for x in range(len(doors)) if x not in (door_choice, open_door))
            
        win = True if doors[door_choice] == 'Car' else False
        
        draw_doors(doors, door_graphics, [0, 1, 2])

        print(f'Door {door_choice + 1} has a {doors[door_choice]}!')
        print('You won!' if win else 'You lost!')

        if swap_doors == 'Y':
            swap_wins += win
            swap_losses += not win
        else:
            no_swap_wins += win
            no_swap_losses += not win
        
        swap_total = swap_wins + swap_losses
        no_swap_total = no_swap_wins + no_swap_losses

        print(f'\nSwapping:     {swap_wins} wins, {swap_losses} losses, success rate {swap_wins / swap_total if swap_total else 0:.02%}')
        print(f'Not swapping: {no_swap_wins} wins, {no_swap_losses} losses, success rate {no_swap_wins / no_swap_total if no_swap_total else 0:.2%}\n')

        input('Press enter to repeat the experiment...')

if __name__ in '__main__':
    monty_hall_game()