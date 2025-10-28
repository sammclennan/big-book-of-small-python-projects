# Rainbow pixel art

import sys
import time

from colorama import Fore, init

CHAR = '#'
PAUSE = 0.02
INDENT = 60

init(autoreset=True)

try:
    while True:
        for x in range(2):
            for i in range(INDENT):
                print(' ' * (INDENT - i if x else i)
                      + Fore.RED + CHAR * 2
                      + Fore.YELLOW + CHAR * 2
                      + Fore.GREEN + CHAR * 2
                      + Fore.BLUE + CHAR * 2
                      + Fore.MAGENTA + CHAR * 2
                )
                time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()