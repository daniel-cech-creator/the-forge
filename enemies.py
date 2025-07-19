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
dummy = Enemy('Training Dummy', 30, 30, 0, 0)
giant_rat = Enemy('Giant Rat', 35, 35, 4, 0)

enemy_pool = [dummy,giant_rat]