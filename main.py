# GAME LOOP AND CORE LOGIC
import time, os, random

import weapons
from player import Player
import inventory
import enemies
import utils


utils.clear_term()
player = Player(f'{str(input('Name your vessel: '))}',weapons.wood_sword)
if player.name == '' :player.name = 'Vessel'
utils.clear_term()

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
utils.clear_term()

#Game Loop
while player.health > 0:
    
    # Stats
    print(f'HP - {player.health}/{player.max_health}')
    print(f'Stamina - {player.stamina}/{player.max_stamina}')
    print(f'Money - {player.money}')
    print(f'Equipped Weapon - {player.equipped_weapon.name} | {player.equipped_weapon.dmg} DMG | {player.equipped_weapon.stamina_drain} Stamina drain')

    print('-----------------')
    print(utils.azure('What will you do?\n'))
    print('1 = Next room | 2 = Inventory')

    choice = str(input('> '))
    if choice.upper() == 'EXIT': exit()

    if choice == '1':
        utils.write_out('\nGoing to the next room...')
        input()

        #Choosing random room
        match random.randint(1,3):

            #Enemy room
            case 1:
                current_enemy = random.choice(enemies.enemy_pool)
                current_enemy.health = current_enemy.max_health

                utils.write_out(utils.red(f'A {current_enemy.name} has appeared!'))
                input()
                
                #Battle loop
                while current_enemy.health > 0 and player.health > 0:
                    utils.clear_term()
                    print(f'{player.name} HP - {player.health}/{player.max_health}')
                    print(f'{player.name} Stamina - {player.stamina}/{player.max_stamina}\n')
                    print(f'{current_enemy.name} HP - {current_enemy.health}/{current_enemy.max_health}')
                    print('-----------------')
                    print(utils.azure('What will you do?\n'))
                    print('1 = Attack | 2 = Inventory | 3 = Defend')
                    choice = str(input('> '))

                    # Attacking
                    if choice == '1':
                        if player.stamina > player.equipped_weapon.stamina_drain:

                            current_enemy.health -= player.equipped_weapon.dmg
                            player.stamina -= player.equipped_weapon.stamina_drain
                            utils.write_out(utils.red(f'\nYou attacked for {player.equipped_weapon.dmg} damage.'))
                            input()
                        else:
                            print(utils.blue('\nNot enough stamina!'))
                            input()
                            continue
                    
                    # Defending
                    elif choice == '3':
                        player.defending = True
                        player.stamina += 15
                        print('\nYou are defending!')
                        input()

                    # Invalid input
                    else:
                        print(utils.red('Invalid input!'))
                        input()
                        continue
                    
                    # ENEMY TURN
                    if current_enemy.health > 0:
                        current_enemy.attack_turn(player.defending)
                        if player.defending is True:
                            player.health -= current_enemy.dmg/2
                        else:
                            player.health -= current_enemy.dmg
                        input()

                        if player.defending == True:
                            print(utils.yellow('You are no longer defending.'))
                            player.defending = False
                            input()
                    else:
                        print('The enemy died before it could attack.')
                        input()
                    player.stat_check()
                
                # Battle results
                if player.health > 0 and current_enemy.health < 1:
                    utils.clear_term()
                    print(utils.yellow('You won!'))
                    input()
                else:
                    utils.clear_term()
                    print(utils.red('You lost!'))
                    input()

            #Chest room 
            case 2:
                utils.write_out(utils.yellow("You've found a treasure room!"))
                input()
            
            #Empty room
            case 3:
                utils.write_out(utils.blue("The room is pretty much empty."))
                input()
        

    elif choice == '2':
        print('\nOpening inventory')
        input()
    else:
        print(utils.red('\nInvalid input!'))
        input()
    
    utils.clear_term()


#fix enemy health not reseting