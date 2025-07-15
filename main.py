import time, os, random

import weapons
from player import Player

def clear_terminal():
    #Windows
    if os.name == 'nt':os.system('cls')
    else:os.system('clear')

clear_terminal()
player = Player(f'{str(input('Enter your name: '))}')
clear_terminal()

#Title
print(r'''
 _____                    
|  ___|__  _ __ __ _  ___ 
| |_ / _ \| '__/ _` |/ _ \
|  _| (_) | | | (_| |  __/
|_|  \___/|_|  \__, |\___|
               |___/      
''')
input()
clear_terminal()

#Game Loop
while player.health > 0:
    print('What will you do?')
    print('1 = Next room | 2 = Inventory')

    choice = str(input('> '))
    if choice == 'exit': exit()
    clear_terminal()