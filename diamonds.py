# Draws ASCII art diamonds of varying sizes

def draw_diamond_outline(size):
    for i in range(size):
        print(' ' * (size - 1 - i) + '/' + ' ' * (i * 2) + '\\')
    for i in range(size):
        print(' ' * i + '\\' + ' ' * ((size - 1 - i) * 2) + '/')

def draw_solid_diamond(size):
    for i in range(size):
        print(' ' * (size - 1 - i) + '/' + '/' * i + '\\' * i + '\\')
    for i in range(size):
        print(' ' * i + '\\' * (size - 1 - i) + '\\' + '/' * (size - 1 - i) + '/')

if __name__ == '__main__':
    for size in range(6):
        draw_diamond_outline(size)
        draw_solid_diamond(size)