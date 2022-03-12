#этот код рисует несложный график пульса в терминале

from time import sleep
from os import system
start = 5
while True:
        for i in range(20):
            for k in range(20, 0, -1):
                if k == (start + i) % 20 or k == (start + i + 10) % 20:
                    print(' **')
                elif k == (start + i + 1) % 20 or k == (start + i + 11) % 20:
                    print(' ********')
                elif k == (start + i + 2) % 20 or k == (start + i + 12) % 20:
                    print('***')
                else:
                    print('*')
            sleep(0.2)
            system('cls')

    