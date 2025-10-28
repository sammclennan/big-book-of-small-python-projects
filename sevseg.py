# Generates a string of seven-segment digits

def getSevSeg(number: int, padding: int=0):
    SEVSEG_DICT = {'0': [' __ ',
                         '|  |',
                         '|__|'],
                   '1': ['    ',
                         '   |',
                         '   |'],
                   '2': [' __ ',
                         ' __|',
                         '|__ '],
                   '3': [' __ ',
                         ' __|',
                         ' __|'],
                   '4': ['    ',
                         '|__|',
                         '   |'],
                   '5': [' __ ',
                         '|__ ' ,
                         ' __|'],
                   '6': [' __ ',
                         '|__ ',
                         '|__|'],
                   '7': [' __ ',
                         '   |',
                         '   |'],
                   '8': [' __ ',
                         '|__|',
                         '|__|'],
                   '9': [' __ ',
                         '|__|',
                         ' __|'],
                   '.': [' ',
                         ' ',
                         '.'],
                   '-': ['    ',
                         ' __ ',
                         '    '],}
  
    if not isinstance(number, (int, float)):
       raise TypeError('number must be of type int or float!')
    if not isinstance(padding, int):
       raise TypeError('padding must be of type int!')
    number = str(number)
 
    if padding > len(number):
       while padding > len(number):
          number = '0' + number
    
    sevsegStr = ''
 
    for i in range(3):
       for digit in number:
          sevsegStr += SEVSEG_DICT[digit][i] + ' '
       sevsegStr += '\n'
    
    return sevsegStr

if __name__ == '__main__':
    print(getSevSeg(-42.5))