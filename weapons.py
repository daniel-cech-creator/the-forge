from enum import Enum

class WeaponType(Enum):
    MELEE = 'melee'
    RANGED = 'ranged'
    MAGIC = 'magic'

class Weapon:
    def __init__(self,name,type : WeaponType,info,dmg,value):
        self.name = name
        self.type = type
        self.info = info
        self.dmg = dmg
        self.value = value

#Name, Type, Info, Damage, Value
wood_sword = Weapon('Wooden Sword',WeaponType.MELEE,'Weak wooden sword',10,30)