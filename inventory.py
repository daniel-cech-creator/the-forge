# PLAYER INVENTORY FUNCTIONS

def draw_inventory(inventory):
    from utils import color_by_rarity
    from collections import Counter
    import utils

    print('\nOpening inventory')
    utils.clear_term()
    print(utils.azure('\nInventory:\n'))

    counted_inv = Counter(inventory)
    for item,amount in counted_inv.items():
        print(f'{color_by_rarity(item)} {amount}x')
    print('-----------------')
    print('(ne nemuzes s tim nic delat, je to ZATIM jen pro efekt)')