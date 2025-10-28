# Birthday Paradox simulator
import random

def generate_birthday():
    month_dict ={1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    month = random.randint(1, 12)
    day = random.randint(1, (30 if month in (9, 4, 6, 11) else 28 if month == 2 else 31))

    month = month_dict[month]

    return '{} {}'.format(month, day)

print('How many birthdays shall I generate? (2 <= x <= 100)')

while True:
    try:
        birthdays_to_generate = int(input('> '))
        if 2 <= birthdays_to_generate <= 100:
            break
        else:
            print('Please enter an integer between 2 and 100')
    except ValueError:
        print('Not a valid integer!')

birthday_list = []

for i in range(birthdays_to_generate):
    birthday_list.append(generate_birthday())

print('Here are {} birthdays:'.format(birthdays_to_generate))

print(', '.join(birthday_list))

birthday_counts = {}

for birthday in birthday_list:
    birthday_counts.setdefault(birthday, 0)
    birthday_counts[birthday] += 1

if any(value > 1 for value in birthday_counts.values()):
    print('In this simulation, multiple people have a birthday on', ', '.join(key for key, value in birthday_counts.items() if value > 1) + '.')
else:
    print('In this simulation, there were no shared birthdays.')

print('Generating {} random birthdays 100,000 times.'.format(birthdays_to_generate))
print('Press Enter to begin...')
input()

matching_birthdays = 0

for i in range(100000):
    if i % 10000 == 0:
        print('{} simulations run...'.format(i))
    # Empty birthday list
    birthday_list = []
    # Append x random birthdays to list
    for j in range(birthdays_to_generate):
        birthday_list.append(generate_birthday())
    # 
    seen = set()
    for birthday in birthday_list:
        if birthday in seen:
            matching_birthdays += 1
            break
        seen.add(birthday)

print('Out of 100,000 simulations of {} people, there was a matching birthday in that group {} times. This means that {} people have a {:.2%} chance of having a matching birthday in their group.\nThat\'s probably more than you would think!'.format(birthdays_to_generate, matching_birthdays, birthdays_to_generate, matching_birthdays/100000))