# Lucky Stars multiplayer dice game. On your turn, you pull three random dice from the dice cup and roll them. You can roll Stars, Skulls, and Question Marks. If you end your turn, you get one point per Star. If you choose to roll again, you keep the Question Marks and pull new dice to replace the Stars and Skulls. If you collect three Skulls, you lose all your Stars and end your turn. When a player gets 13 points, everyone else gets one more turn before the game ends. Whoever has the most points wins. There are six gold dice, four silver dice, and three bronze dice in the cup. Gold dice have more Stars, bronze dice have more Skulls, and silver is even.

import random
import sys

STAR = [
    "     .     ",
    "    ,O,    ",
    " 'ooOOOoo' ",
    "   `OOO`   ",
    "   O' 'O   ",
]

SKULL = [
    "    ___    ",
    "   /   \\   ",
    "  |() ()|  ",
    "   \\ ^ /   ",
    "    VVV    ",
]

Q_MARK = [
    "           ",
    "           ",
    "     ?     ",
    "           ",
    "           ",
]

DICE_TYPES = {
    'gold': ['star'] * 3 + ['skull'] + ['q_mark'] * 2,
    'silver': ['star'] * 2 + ['skull'] * 2 + ['q_mark'] * 2,
    'bronze': ['star'] + ['skull'] * 3 + ['q_mark'] * 2,
}

DICE_CUP = ['gold'] * 6 + ['silver'] * 4 + ['bronze'] * 3


def draw_die(die, faces):
    print('+-----------+ ' * 3)
    for i in range(5):
        for face in faces:
            print('|', end='')
            print(STAR[i] if face == 'star' else SKULL[i] if face == 'skull' else Q_MARK[i], end='')
            print('|', end=' ')
        print()
    print('+-----------+ ' * 3)

    for dice in die:
        print(dice.upper().center(13), end=' ')
    print()


player_data = {}

i = 1
while True:
    print(f"Enter player {i}'s name and press ENTER (leave blank for no more players)")
    player_name = input('> ').strip()
    if player_name:
        player_data.update({player_name: 0})
    else:
        break
    i += 1

final_round = False
final_round_start = None
finish = False

print('LUCKY STARS')
print('Collect as many stars as you can on each turn. If you collect three skulls, you lose all your stars and end your turn!')

while True:
    # For each player
    for index, player in enumerate(player_data):
        if final_round:
            if index == (final_round_start + 1) % len(player_data):
                print('FINAL ROUND!')
            elif index == final_round_start:
                finish = True
                break

        # Each player starts with 0 stars and 0 skulls
        stars = 0
        skulls = 0

        input('Press Enter to continue...')
        for p in player_data:
            print(f'{p} stars: {player_data[p]}')
        print(f"It's {player}'s turn.")
        input('Press Enter to roll')

        while True:
            # Roll 3 die from cup
            die = random.sample(DICE_CUP, 3)
            roll = [random.choice(DICE_TYPES[dice]) for dice in die]

            # Display dice graphics
            draw_die(die, roll)

            # Increment score
            stars += roll.count('star')
            skulls += roll.count('skull')

            print(f'Stars collected: {stars}   Skulls collected: {skulls}')

            # Player loses stars and ends turn upon collecting 3 skulls
            if skulls >= 3:
                print(f"Oh no! {player}, you've lost all your stars!")
                break
            
            # Get player roll
            print(f'{player}, do you want to roll again? Y/N or QUIT')
            while True:
                roll_again = input('> ').upper()
                if roll_again in ('Q', 'QUIT'):
                    print('Thanks for playing!')
                    sys.exit()
                elif roll_again not in ('Y', 'N', 'YES', 'NO'):
                    print('Please enter Yes or No.')
                else:
                    break

            # Players collect stars at end of turn
            if roll_again in ('N', 'NO'):
                player_data[player] += stars

                # End game after last player on final round
                if final_round and index == (final_round_start - 1) % len(player_data):
                    break

                # Final round after a player collects 13 stars
                if player_data[player] >= 13 and not final_round:
                    print(f'{player} got {player_data[player]} stars. All other players get one more turn!')
                    final_round = True
                    final_round_start = index

                break

    if finish: break   

print('GAME OVER!')

for player in player_data:
    print(f'{player} score: {player_data[player]}')

high_score = max(player_data.values())
winners = [player for player in player_data if player_data[player] == high_score]

if len(winners) > 1:
    print(f"It's a tie between {', '.join(winners[:-1])} and {winners[-1]}!")
else:
    print(f'{winners[0]} wins!')
