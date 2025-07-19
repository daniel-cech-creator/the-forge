# WEAPON CLASS AND WEAPON LIST

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

#Name, Type, Info, Damage, Stamina Drain, Value

# =======
#  MELEE
# =======

wood_sword = Weapon('Wooden Sword',WeaponType.MELEE,'Weak wooden sword',10,6,30)
rusty_sword = Weapon('Rusty Sword',WeaponType.MELEE,'Old, damaged blade',14,8,28)
sledge_hammer = Weapon('Sledge Hammer',WeaponType.MELEE,'Huge heavy blunt weapon',28,18,58)
thief_dagger = Weapon('Thief Dagger', WeaponType.MELEE, 'Small dagger used by bandits',8,3,25)
#spear
#steel_halberd