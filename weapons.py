from enum import Enum

class WeaponType(Enum):
    MELEE = 'melee'
    RANGED = 'ranged'
    MAGIC = 'magic'

class Weapon:
    def __init__(self,name,type : WeaponType,info,dmg,stamina_drain,value):
        self.name = name
        self.type = type
        self.info = info
        self.dmg = dmg
        self.stamina_drain = stamina_drain
        self.value = value

#Name, Type, Info, Damage, Value

# =======
#  MELEE
# =======

wood_sword = Weapon('Wooden Sword',WeaponType.MELEE,'Weak wooden sword',10,6,30)
#rusty_sword
#sledge_hammer
#thief_dagger
#spear
#steel_halberd