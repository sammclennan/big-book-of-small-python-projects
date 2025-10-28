# Multiplication table

print('  |', end='')
for row in range(13): print(f'{row:>3}', end=' ')
print()
print('--+' + '-' * 51)
for row in range(13):
    print(f'{row:>2}' + '|', end='')
    for col in range(13):
        print(f'{row * col:>3}', end=' ')
    print()