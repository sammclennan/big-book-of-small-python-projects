while True:
    try:
        start = int(input('Enter the starting number (e.g. 0) > '))
        break
    except ValueError:
        print('Please enter a whole number!')

while True:
    try:
        n = int(input('Enter how many numbers to display (e.g. 1000) > '))
        if n > 0:
            break
        else:
            print('Please enter a postive number!')
    except ValueError:
        print('Please enter a whole number!')

for i in range(start, start + n):
    print(f"DEC: {i}    HEX: {hex(i).replace('0x', '').upper()}    BIN: {bin(i).replace('0b', '')}")