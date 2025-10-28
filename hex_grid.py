import os

terminal_width = os.get_terminal_size()[0]
terminal_height = os.get_terminal_size()[1]

for i in range(terminal_height // 2):
    for j in range(terminal_width // 4):
        print(r'/ \_', end='')
    print()
    for j in range(terminal_width // 4):
        print(r'\_/ ', end='')
    print()