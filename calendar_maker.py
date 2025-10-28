import calendar
import datetime

# Get year
while True:
    try:
        year = int(input('Please enter year (1 - 9999): '))
        if 1 <= year <= 9999:
            break
        else:
            print('Year must be within range 1 - 9999!')
    except ValueError:
        print('Year value must be an integer!')

# Get month
while True:
    try:
        month = int(input('Enter month number (1 - 12): '))
        if 1 <= month <= 12:
            break
        else:
            print('Month must be within range 1 - 12!')
    except ValueError:
        print('Month value must be an integer!')

# Get day of week for 1st of month, days in month, and prior month
first_day_in_month = calendar.monthrange(year, month)[0]

days_in_month = calendar.monthrange(year, month)[1]

days_in_previous_month = calendar.monthrange(year - 1, 12)[1] if month == 1 else calendar.monthrange(year, month - 1)[1]

cal = []

# Append days to calendar
for day in range(1, days_in_month + 1):
    cal.append(day)

for i in range(first_day_in_month):
    cal.insert(0, days_in_previous_month - i)

extra_days = 1
while len(cal) % 7 != 0:
    cal.append(extra_days)
    extra_days += 1

# Draw calendar
print(f'{calendar.month_name[month]} {year}'.center(78))

print('...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..')

day = 0
for i in range(5 if len(cal) <= 35 else 6):
    print('+----------' * 7 + '+')
    for j in range(7):
        print('|' + str(cal[day]).rjust(2) + ' ' * 8, end='')
        day += 1
    print('|')
    for k in range(3):
        print(('|' + ' ' * 10) * 8, end='')
        print()
print('+----------' * 7 + '+')