# Creates a Fibonacci sequence

print('How many Fibonacci numbers do you want to calculate?')

while True:
    try:
        n = int(input('> '))
        if n > 0:
            break
        else:
            print('N must be a positive number!')
    except ValueError:
        print('N must be an integer!')

fib_list = []
a, b = 0, 1
for i in range(n):
    fib_list.append(str(a))
    a, b = b, a + b

print(', '.join(fib_list))

