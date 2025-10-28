# Calculates the probabilities resulting from rolling x die 1,000,000 times

import random

# Get number of die from user
print('Enter number of six-sided dice to roll')
while True:
    try:
        num_dice = int(input('> '))
        if num_dice > 0:
            break
        else:
            print('Number of dice must be positive!')
    except ValueError:
        print('Please enter an integer value.')

num_rolls = 1000000
roll_outcomes = dict()

print(f'Simulating {num_rolls:,} rolls of {num_dice} dice...')
for i in range(num_rolls):
    total = 0

    # Roll die
    for j in range(num_dice):
        total += random.randint(1, 6)

    # Store results in dictionary
    roll_outcomes[total] = roll_outcomes.get(total, 0) + 1

# Calculate probabilities
sorted_outcomes = dict(sorted(roll_outcomes.items()))

print(f'{'TOTAL':<5} - {'ROLLS':^10} - {'PERCENTAGE':<10}')
for outcome, rolls in sorted_outcomes.items():
    roll_prob = rolls / num_rolls * 100
    print(f"{outcome:<5} - {rolls:>10} - {roll_prob:>9.3f}%")