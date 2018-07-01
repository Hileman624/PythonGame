class Quest:
    def __init__(self, name, objective, gold, xp):
        self.name = name
        self.objective = objective
        self.gold = gold
        self.xp = xp


class Player:
    def __init__(self, name, max_health, max_mana):
        self.name = name
        self.health = max_health
        self.max_health = max_health

        self.mana = max_mana
        self.max_mana = max_mana

        self.gold = 0
        self.inventory = []
        self.crafting_inventory = []
        self.xp = 0
        self.weapons = []
        self.ammo = []
        self.shields = []
        self.raiseShield = 0

    def add_gold(self, gold):
        self.gold = self.gold + gold

    def add_xp(self, xp):
        self.xp = self.xp + xp
        if self.xp >= 100:
            print("You leveled up!")
            self.max_health = self.max_health + 10
            self.health = self.max_health
            self.max_mana = self.max_mana + 5
            self.mana = self.max_mana
            self.xp = 0


class Weapon:
    def __init__(self, name, min_damage, max_damage, damage_type, cost):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.damage_type = damage_type
        self.cost = cost


class Ammo:
    def __init__(self, name, min_damage, max_damage, damage_type, cost):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.damage_type = damage_type
        self.cost = cost


class Shield:
    def __init__(self, name, min_block, max_block, cost):
        self.name = name
        self.min_block = min_block
        self.max_block = max_block
        self.cost = cost


class Armor:
    def __init__(self, name, damage_reduction, cost):
        self.name = name
        self.damage_reduction = damage_reduction
        self.cost = cost


# ITEMS!
class HealthPotion:
    def __init__(self, name, restore_health, cost):
        self.name = name
        self.restore_health = restore_health
        self.cost = cost


class ManaPotion:
    def __init__(self, name, restore_mana, cost):
        self.name = name
        self.restore_mana = restore_mana
        self.cost = cost


# CRAFTING MATERIALS!
class Materials:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


# MONSTER!
class Monster:
    def __init__(self, name, max_health, min_damage, max_damage, weakness, xp):
        self.name = name
        self.max_health = max_health
        self.health = self.max_health
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.weakness = weakness
        self.xp = xp

