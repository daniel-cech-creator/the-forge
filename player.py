class Player:
    def __init__(self, name, equipped_weapon, health=100, max_health=100, money=0, stamina=100, max_stamina=100, inventory=None):
        # If no inventory was given, create a new empty list
        if inventory is None:
            inventory = []

        self.name = name
        self.equipped_weapon = equipped_weapon
        self.health = health
        self.max_health = max_health
        self.money = money
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.inventory = inventory