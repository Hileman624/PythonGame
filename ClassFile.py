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
        self.xp = 0
        self.weapons = []
        self.shields = []

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
    def __init__(self, name, min_damage, max_damage, damage_type):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.damage_type = damage_type


class Shield:
    def __init__(self, name, min_block, max_block):
        self.name = name
        self.min_block = min_block
        self.max_block = max_block


# ITEMS!
class HealthPotion:
    def __init__(self, name, restore_health):
        self.name = name
        self.restore_health = restore_health


class ManaPotion:
    def __init__(self, name, restore_mana):
        self.name = name
        self.restore_mana = restore_mana


# CRAFTING MATERIALS!
class Materials:
    def __init__(self, name):
        self.name = name


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

