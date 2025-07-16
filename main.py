# GAME LOOP AND CORE LOGIC
import time, os, random

import weapons
from player import Player
import inventory
import enemies
from utils import *



clear()
player = Player(f'{str(input('Name your vessel: '))}',weapons.wood_sword)
if player.name == '' :player.name = 'Vessel'
clear()

#Title
print(r'''
 _____                    
|  ___|__  _ __ __ _  ___ 
| |_ / _ \| '__/ _` |/ _ \
|  _| (_) | | | (_| |  __/
|_|  \___/|_|  \__, |\___|
               |___/      
''')
input('Enter to continue')
clear()

#Game Loop
while player.health > 0:
    
    # Stats
    print(f'HP - {player.health}/{player.max_health}')
    print(f'Stamina - {player.stamina}/{player.max_stamina}')
    print(f'Money - {player.money}')
    print(f'Equipped Weapon - {player.equipped_weapon.name}')

    print('-----------------')
    print('What will you do?\n')
    print('1 = Next room | 2 = Inventory')

    choice = str(input('> '))
    if choice.upper() == 'EXIT': exit()

    if choice == '1':
        print('\nGoing to the next room...')
        input()
    elif choice == '2':
        print('\nOpening inventory')
        input()
    else:
        print(red('\nInvalid input!'))
        input()
    
    clear()