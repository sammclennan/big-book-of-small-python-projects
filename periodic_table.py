# This program presents this table and lets the player access additional information about each element, such as its atomic number, symbol, melting point, and so on.

import sys
import csv

TABLE = """                  Periodic Table of Elements        
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr"""


def print_element_info(element_info):
    ralign = 27
    print(f"""{'Atomic Number:':>ralign} {element_info[0]}
{'Symbol:':>ralign} {element_info[1]}
{'Element:':>ralign} {element_info[2]}
{'Origin of name:':>ralign} {element_info[3]}
{'Group:':>ralign} {element_info[4]}
{'Period:':>ralign} {element_info[5]}
{'Atomic weight:':>ralign} {element_info[6]}
{'Density:':>ralign} {element_info[7]}
{'Melting point:':>ralign} {element_info[8]}
{'Boiling point:':>ralign} {element_info[9]}
{'Specific heat capacity:':>ralign} {element_info[10]}
{'Electronegativity:':>ralign} {element_info[11]}
{'Abundance in earth\'s crust:':>ralign} {element_info[12]}\n""")


filename = 'periodictable.csv'

# Open csv file
try:
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        element_info = list(reader)
except FileNotFoundError:
    print(f'Error: File {filename} not found.')
    sys.exit()

while True:
    # Get user input
    while True:
        print('Enter a symbol or atomic number (1 - 118) to examine, or QUIT to quit.')
        user_input = input('> ').title().strip()
        if not user_input:
            continue
        elif user_input == 'QUIT':
            sys.exit()
        else:
            break

    # Search list for user input
    found = False
    for row in element_info:
        if user_input.isdecimal() and user_input == row[0] or len(user_input) <= 2 and user_input == row[1] or user_input == row[2]:
            print_element_info(row)
            found = True
            break
    
    if not found: print(f'Element {user_input} not found in file.')
    
    print('Press Enter to continue...')