# ASCII DNA visualization

import random
import sys
import time

nucleotides = (('G', 'C',), ('C', 'G'), ('A', 'T'), ('T', 'A'))

dna = ['     ##',
       '    #{}-{}#',
       '   #{}---{}#',
       '  #{}-----{}#',
       ' #{}------{}#',
       '#{}------{}#',
       '#{}-----{}#',
       ' #{}---{}#',
       ' #{}-{}#',
       '  ##']

print('Press Ctrl + C to stop.')
time.sleep(2)

try:
    while True:
        for i in range(1, len(dna)):
            pair = random.choice(nucleotides)
            print(dna[i].format(pair[0], pair[1]))
            time.sleep(0.1)

        for i in range(len(dna) - 2, -1, -1):
            pair = random.choice(nucleotides)
            print(dna[i].format(pair[0], pair[1]))
            time.sleep(0.1)
            
except KeyboardInterrupt:
    print('Program stopped by user.')
    sys.exit()