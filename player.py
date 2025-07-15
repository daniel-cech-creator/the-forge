class Player:
    def __init__(self, name, health=100, max_health=100, money=0, inventory=None):
        # If no inventory was given, create a new empty list
        if inventory is None:
            inventory = []

        self.name = name
        self.health = health
        self.max_health = max_health
        self.money = money
        self.inventory = inventory