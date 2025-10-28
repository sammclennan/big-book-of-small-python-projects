# Powerball lottery simulator

import random

print("Each powerball lottery ticket costs $2. The jackpot for this game is $1.586 billion! It doesn't matter what the jackpot is, though, because the odds are 1 in 292,201,338, so you won't win.\n\nThis simulation gives you the thrill of playing without wasting money.\n")

PRICE_PER_TICKET = 2

# Get numbers from user
# Get numbers from user
print('Enter 5 different numbers from 1 to 69 with spaces between each number.(For example: 5 17 23 42 50 51).')
while True:
    try:
        player_numbers = list(map(int, input('> ').split()))
        if len(player_numbers) != 5:
            print('Please enter exactly 5 numbers.')
        elif not all(1 <= x <= 69 for x in player_numbers):
            print('All numbers must be between 1 and 69.')
        elif len(set(player_numbers)) != 5:
            print('You can only select each number once.')
        else:
            break

    except ValueError:
        print('Please enter whole numbers only.')

# Get powerball from user
print('Enter a powerball number from 1 to 26')
while True:
    try:
        player_powerball = int(input('> ').strip())
        if 1 <= player_powerball <= 26:
            break
        else:
            print('Please enter a number between 1 and 26.')

    except ValueError:
        print('Please enter whole numbers only.')

# Get number of tickets from user
print('How many tickets do you want to buy? (Max: 1,000,000)')
while True:
    try:
        num_tickets = int(input('> ').strip())
        if 1 <= num_tickets <= 1000000:
            break
        else:
            print('Please enter a number between 1 and 1,000,000.')

    except ValueError:
        print('Please enter whole numbers only.')

ticket_cost = num_tickets * PRICE_PER_TICKET

print(f"It costs ${ticket_cost:,} to play {num_tickets:,} times, but don't worry. I'm sure you'll win it all back.")
input('Press enter to start...')

for i in range(num_tickets):
    winning_numbers = random.sample(range(1, 70), 5)
    powerball = random.randint(1, 26)

    print(f'The winning numbers are {', '.join(map(str, winning_numbers))} and {powerball}', end='   ')
    if set(player_numbers) == set(winning_numbers) and player_powerball == powerball:
        print('Congratulations! You won!')
        break
    else:
        print('You lost.')

print(f'You have wasted ${ticket_cost:,}\nThanks for playing!')