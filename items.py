import os
from time import sleep
import utils
import random
from collections import Counter

class Item:
    def __init__(self,name,info,rarity):
        self.name = name
        self.info = info
        self.rarity = rarity

meaty_slop = Item('Meaty Slop', 'Heals for +40 Health', 'common')
spaghetti_code = Item('spaghetti_code', 'player.health += 30', 'common')
heart_charm = Item('Heart Charm', '+10 Maximum Health', 'rare')
inside_friend = Item('Inside Friend', ' friend inside me.', 'epic')
shadow_shell = Item('Shadow Shell', '+12 Defense', 'legendary')


def color_by_rarity(item):
    if item.rarity == "common":
        return item.name
    elif item.rarity == "rare":
        return utils.blue(item.name)
    elif item.rarity == "epic":
        return utils.purple(item.name)
    elif item.rarity == "legendary":
        return utils.rainbow(item.name)

def loot_display(battle_loot,money):
    print('You found:\n')
    sleep(0.5)
    for item in battle_loot:
        print(' +'+color_by_rarity(item))
        sleep(0.1)
    print(utils.yellow(f' +{money} gold'))
    print()


#testing item pool
item_pool = {
    heart_charm: 0.12, # 12%
    inside_friend: 0.1, # 10%
    shadow_shell: 0.1, # 10%
    meaty_slop: 0.2, # 20%
    spaghetti_code: 0.25, # 25%
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