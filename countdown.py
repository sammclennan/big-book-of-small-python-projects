 # Displays a countdown timer using seven-segment display

import sys
import time
import sevseg # Custom program for generating seven-segment digits

# Get seconds from user
while True:
    try:
        seconds_left = input('Enter countdown time in seconds: ')
        seconds_left = int(float(seconds_left))
        if seconds_left < 1:
            print('Countdown must be 1 or greater!')
        else:
            break
    except ValueError:
        print('Please enter a number!')

print('Ctrl + C to quit')

try:
    while seconds_left > 0:
        # Convert total 
        hours, secs = seconds_left // 3600, seconds_left % 3600
        mins, secs = secs // 60, secs % 60

        # Get hours, mins, secs as seven-segment display 
        sevseg_hours = sevseg.getSevSeg(hours, 2)
        sevseg_mins = sevseg.getSevSeg(mins, 2)
        sevseg_secs = sevseg.getSevSeg(secs, 2)

        # Split seven-segment numbers by lines
        hours_split = sevseg_hours.splitlines()
        mins_split = sevseg_mins.splitlines()
        secs_split = sevseg_secs.splitlines()

        # Display in digital clock format
        print(hours_split[0] + '     ' + mins_split[0] + '     ' + secs_split[0])
        print(hours_split[1] + '  *  ' + mins_split[1] + '  *  ' + secs_split[1])
        print(hours_split[2] + '  *  ' + mins_split[2] + '  *  ' + secs_split[2])

        seconds_left -= 1

        time.sleep(1)

        # Overwrite previous output
        sys.stdout.write('\033[3A')
        sys.stdout.write('\033[0J')

except KeyboardInterrupt:
    print('Program stopped by user')
    sys.exit()
