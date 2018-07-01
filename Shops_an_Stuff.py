
from random import *
from ClassFile import Player
from ClassFile import Weapon
from ClassFile import Shield
from ClassFile import HealthPotion
from ClassFile import ManaPotion
from ClassFile import Monster
from MonsterEncounterFunction import monster_encounter

def springfield_shop(player):
    print("Welcome," + player.name)
    would_you_like_to_shop = input("Would you like to browse my wares? [YES/NO]")
    if would_you_like_to_shop.upper() == 'YES':
        is_valid = 0
        while is_valid == 0:
            print("We have consumables and materials.")
            shop = input("Which one would you like to browse? [CONSUMABLES/MATERIALS} If you have changed your mind, and would like to leave the shop [NO] ")
                if shop.upper() == 'CONSUMABLES':
                    is_valid = 1
                    shop_consumables = input('MINOR HEALTH POTION'
                                             'MINOR MANA POTION')

                    if shop_consumables.upper() == 'MINOR HEALTH POTION':
                        player.inventory.append(minor_health_potion)

                if shop.upper() == 'MATERIALS':
                    is_valid = 1
                    shop_materials = input('')
                if shop.upper() == 'NO':
                    is_valid = 1

    if would_you_like_to_shop.upper() == 'NO':
        print("Okay, if you change your mind, I'll be here!")
        return

def springfield_smith(player):
