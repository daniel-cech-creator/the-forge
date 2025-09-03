import os
from time import sleep
import utils
import random
from collections import Counter
from enum import Enum

class Item:
    def __init__(self,name,info,rarity):
        self.name = name
        self.info = info
        self.rarity = rarity


class Rarity(Enum):
    COMMON = 'common'
    RARE = 'rare'
    EPIC = 'epic'
    LEGENDARY = 'legendary'

# COMMON
meaty_slop = Item('Meaty Slop', 'Heals for +40 Health', Rarity.COMMON)
spaghetti_code = Item('spaghetti_code', 'player.health += 30', Rarity.COMMON)

# RARE
heart_charm = Item('Heart Charm', '+10 Maximum Health', Rarity.RARE)
dusek_sweets = Item("Dusek Sweets", "For your hard work", Rarity.RARE)

# EPIC
inside_friend = Item('Inside Friend', ' friend inside me.', Rarity.EPIC)

# LEGENDARY
shadow_shell = Item('Shadow Shell', '+12 Defense', Rarity.LEGENDARY)
slopware = Item("Slopware", "I worked at Blizzard for 1000 years.", Rarity.LEGENDARY)


def color_by_rarity(item):
    if item.rarity == Rarity.COMMON:
        return item.name
    
    elif item.rarity == Rarity.RARE:
        return utils.blue(item.name)
    
    elif item.rarity == Rarity.EPIC:
        return utils.purple(item.name)
    
    elif item.rarity == Rarity.LEGENDARY:
        return utils.rainbow(item.name)

def loot_display(battle_loot,gold,player):
    print()
    print('You found:\n')
    sleep(0.5)
    for item in battle_loot:
        print(' +'+color_by_rarity(item))
        sleep(0.1)
    print(utils.yellow(f' +{gold} gold'))
    player.money += gold
    print()


#testing item pool
item_pool = {
    heart_charm: 0.12, # 12%
    inside_friend: 0.1, # 10%
    shadow_shell: 0.1, # 10%
    meaty_slop: 0.2, # 20%
    spaghetti_code: 0.25, # 25%
    slopware: 0.05, # 5%
    dusek_sweets: 0.12 # 12%

}

def roll_loot(item_pool):
    loot = []

    for item, chance in item_pool.items():
        if random.random() < chance:
            loot.append(item)
    
    return loot

def display_inv(inventory):
    counted_inv = Counter(inventory)
    for item,amount in counted_inv.items():
        print(f'{color_by_rarity(item)} {amount}x')