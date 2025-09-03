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
            match random.randint(1,4):

                # Magical Fountain
                case 1:
                    print(utils.blue('Your path was interrupted by a mystical fountain...'))
                    input()
                    answered = False
                    while answered == False:
                        utils.clear_term()
                        print(utils.azure('What will you do?\n'))
                        print('\n1 = Drink the water | 2 = Leave')
                        choice = str(input('> '))
                        
                        if choice == '1':
                            utils.clear_term()
                            print('You took a sip from the fountain...')
                            input()
                            print(utils.green('Your health was replenished!'))
                            answered = True
                            player.health = player.max_health
                        elif choice == '2':
                            utils.clear_term()
                            print("You've moved on without drinking the water.")
                            answered = True
                            
                        else:
                            print(utils.red('Invalid input!'))
                            input()
                    input()
                        
                
                # Crystal Ball
                case 2:
                    print(utils.purple('You entered a dimly lit room with a table holding a crystal ball.'))
                    input()

                # Rattman
                case 3:
                    print(utils.green("Your path is blocked by a strange looking man rat."))
                    input()
                    utils.clear_term()
                    print("\"Hey kid... you look like someone whos looking for a profit, eh? Well lucky you... I got\na game here you'll love.\"")
                    input()
                    answered = False
                    while answered == False:
                        utils.clear_term()
                        print("\"So what do you say, kid? Down for a game or two?\"")
                        print(utils.azure('What will you do?\n'))
                        print('\n1 = Play a game | 2 = Leave | 3 = Fight')
                        choice = str(input('> '))
                        if choice == '1':
                            print("\"\nYeah that's right! Let's do this...\"")
                            input()
                            answered = True
                        elif choice == '2':
                            print("\"\nHuh? Whatever you want... I could've made you a fortune.\"")
                            input()
                            answered = True
                        elif choice == '3':
                            print(utils.red("\"Huh... you're smarter than you look...\""))
                            input()
                            enemies.battle(enemies.rattman, player)
                            answered = True
                        else:
                            print(utils.red('Invalid input!'))
                            input()
                case 4:
                    print(utils.red("You stumble upon a lonely talking campfire..."))
                    input()
                    utils.clear_term()
                    print("\"Greetings traveler... I'm the fire of wisdom, knower of all and more.\"")
                    input()
                    print("\"If you do not wish to talk, that is understandable, you can just enjoy my warmth\"")
                    input()
                    answered = False
                    while answered == False:
                        utils.clear_term()
                        print("\"Feel free to ask any questions.\"")
                        print(utils.azure('\nWhat will you do?\n'))
                        print('\n1 = Rest | 2 = Leave | 3 = Talk')
                        choice = str(input('> '))

                        if choice == '1':
                            print("\nYou sat down next to the fire and rested...")
                            input()
                            print(utils.green("Your stamina was replenished!"))
                            player.stamina = player.max_stamina
                            input()
                        elif choice == '2':
                            print("\n\"Good luck on your journey, traveler...\"")
                            input()
                            answered = True
                        elif choice == '3':
                            print("\n\"Very well, what's your question?\"")
                            input()
                        else:
                            print(utils.red('Invalid input!'))
                            input()


            #input()
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
                enemies.battle(current_enemy, player)
                roomCount += 1

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
                if random.random() < 0.9:
                    found_coins = random.randint(45,95)
                    player.money += found_coins
                    print(f'But you found {utils.yellow(f'{found_coins} coins')}!')
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