# GAME LOOP AND CORE LOGIC
import time, os, random

import weapons, inventory, enemies, items
from player import Player
import utils

utils.clear_term()
#Title
print(r'''
   _____                    
  |  ___|__  _ __ __ _  ___ 
  | |_ / _ \| '__/ _` |/ _ \
  |  _| (_) | | | (_| |  __/
  |_|  \___/|_|  \__, |\___|
                 |___/  
          
 NOTHING STAYS BURIED FOREVER
''')
input()

# Setting name
utils.clear_term()
player = Player(f'{str(input('Name your vessel: '))}',weapons.wood_sword)
if player.name == '' :player.name = 'Vessel'
utils.clear_term()

#Game Loop
roomCount = 0
while player.health > 0:
    utils.clear_term()
    
    # Stats
    print(f'{utils.red('HP')} - {utils.red(player.health)}/{utils.red(player.max_health)}')
    print(f'{utils.blue('Stamina')} - {utils.blue(player.stamina)}/{utils.blue(player.max_stamina)}')
    print(f'{utils.yellow('Money')} - {utils.yellow(player.money)}')
    print(f'Equipped Weapon - {utils.green(player.equipped_weapon.name)} | {utils.red(f'{player.equipped_weapon.dmg} DMG')} | {utils.blue(f'{player.equipped_weapon.stamina_drain} Stamina Drain')}')
    print(f'room count: {roomCount}')
    print('-----------------')
    print(utils.azure('What will you do?\n'))
    print('1 = Next room | 2 = Inventory')

    choice = str(input('> '))
    if choice.upper() == 'EXIT': exit()

    # NEXT ROOM
    if choice == '1':
        print('\nGoing to the next room...')
        input()


        if roomCount != 0 and roomCount % 10 == 0:
            print(utils.yellow("A friendly voice welcomes you as you take step into the shopkeeper's keep."))
            input()
            roomCount += 1
            continue

        # Special room (5% chance)
        if random.random() <= 0.5:
            match random.randint(1,3):

                # Magical Fountain
                case 1:
                    print('Your path was interrupted by a mystical fountain...')
                    input()
                    utils.clear_term()
                    print(utils.azure('What will you do?\n'))
                    print('\n1 = Drink the water | 2 = Leave')
                    choice = str(input('> '))
                    utils.clear_term()
                    if choice == '1':
                        print('You took a sip from the fountain...')
                        input()
                        print('Your health was replenished!')
                        player.health = player.max_health
                        
                    else:
                        print("You've moved on without drinking the water.")
                        
                
                # Crystal Ball
                case 2:
                    print('crystal ball')

                # Totem of Solitude
                case 3:
                    print('totem of solitude')
            input()
            roomCount += 1
            continue
        
        
        #Choosing random room
        match random.randint(1,3):

            #Enemy room
            case 1:
                current_enemy = random.choice(enemies.enemy_pool)
                current_enemy.health = current_enemy.max_health

                print(utils.red(f'A {current_enemy.name} has appeared!'))
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
                            print(utils.red(f'\nYou attacked for {player.equipped_weapon.dmg} damage.'))
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
                    
                    # Loot
                    battle_loot = items.roll_loot(items.item_pool)
                    items.loot_display(battle_loot, current_enemy.loot, player)
                    player.inventory.extend(battle_loot)
                    input()
                    roomCount += 1
                else:
                    utils.clear_term()
                    print(utils.red('You lost!'))
                    input()
                    exit()
            

            #Chest room 
            case 2:
                print(utils.yellow("You've found a treasure room!"))
                input()
                utils.clear_term()
                print(utils.yellow("You've found a treasure room!"))
                chest_loot = items.roll_loot(items.item_pool)
                items.loot_display(chest_loot, random.randint(15,85),player)
                player.inventory.extend(chest_loot)
                input()
                roomCount += 1
            
            #Empty room
            case 3:
                print(utils.blue("The room is empty..."))
                input()
                if random.random() < 0.3:
                    found_coins = random.randint(45,95)
                    player.money += found_coins
                    print(utils.blue(f'But you found {found_coins} coins!'))
                    input()
                roomCount += 1

    # OPEN INVENTORY
    elif choice == '2':
        inventory.draw_inventory(player.inventory)
        input()
    else:
        print(utils.red('\nInvalid input!'))
        input()
    
    utils.clear_term()