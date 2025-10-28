# Gullible

while True:
    response =  input('Do you want to know how to keep a gullible person busy for hours? (Y/N)\n> ')
    if response.lower() in ('n', 'no'):
        break
    elif response.lower() in ('y', 'yes'):
        continue
    else:
        print(f'{response} is not a valid yes/no response')

print('Thank you. Have a nice day!')