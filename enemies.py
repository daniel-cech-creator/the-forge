# ENEMY CLASS AND ENEMY LIST

class Enemy:
    def __init__(self,name,health,max_health,dmg,loot):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.dmg = dmg
        self.loot = loot

    def attack_turn(self,defending):
        if defending is True:
            print(f'{self.name} attacked you for {self.dmg/2} damage.')
        else:
            print(f'{self.name} attacked you for {self.dmg} damage.')




# --- Entrance enemies --- 

#   Name, Health, Max Health, Damage, Loot
dummy = Enemy('Dummy', 30, 30, 0, 0)
giant_rat = Enemy('Giant Rat', 35, 35, 4, 0)
old_statue = Enemy('Old Statue', 50, 50, 6, 0)
rattman = Enemy('Rattman', 75, 75, 4, 124)
# kadimir = Enemy("Kadimir", 100, 100, 5, 10)



enemy_pool = [dummy,giant_rat,old_statue]


def battle(current_enemy, player):
    import utils, items

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
        
    else:
        utils.clear_term()
        print(utils.red('You lost!'))
        input()
        exit()