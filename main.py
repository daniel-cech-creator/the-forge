import time, os, random

import weapons
from player import Player

def clear_terminal():
    #Windows
    if os.name == 'nt':os.system('cls')
    else:os.system('clear')

clear_terminal()
player = Player(f'{str(input('Name your vessel: '))}',weapons.wood_sword)
if player.name == '':player.name = 'Hero'
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
input('Enter to continue')
clear_terminal()

#Game Loop
while player.health > 0:
    
    print(f'HP - {player.health}/{player.max_health}')
    print(f'Stamina - {player.stamina}/{player.max_stamina}')
    print(f'Money - {player.money}')
    print(f'Equipped Weapon - {player.equipped_weapon.name}')

    print('-----------------')
    print('What will you do?')
    print('1 = Next room | 2 = Inventory')

    choice = str(input('> '))
    if choice == 'exit': exit()

    clear_terminal()