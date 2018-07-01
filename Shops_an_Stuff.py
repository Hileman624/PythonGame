
import random
from ClassFile import Player
from ClassFile import Weapon
from ClassFile import Shield
from ClassFile import HealthPotion
from ClassFile import ManaPotion
from ClassFile import Monster
from MonsterEncounterFunction import monster_encounter

# Defined Consumables
minor_health_potion = HealthPotion(name='MINOR HEALTH POTION', restore_health=12, cost=10)
minor_mana_potion = ManaPotion(name='MINOR MANA POTION', restore_mana=5, cost=10)

# Defined Melee Weapons
rough_iron_sword = Weapon(name='ROUGH IRON SWORD', min_damage=8, max_damage=12, damage_type='Slash', cost=20)
rusty_spiked_club = Weapon(name='RUSTY SPIKED CLUB', min_damage=6, max_damage=10, damage_type='Blunt', cost=18)

# Defined Ranged Weapons
hunting_bow = Weapon(name='HUNTING BOW', min_damage=8, max_damage=16, damage_type='Distraction', cost=25)
rusty_flint_lock_pistol = Weapon(name='RUSTY FLINT LOCK PISTOL', min_damage=10, max_damage=20, damage_type='Explosive', cost=30)

# Defined Shields



def springfield_shop(player):
    print("Welcome," + player.name)
    would_you_like_to_shop = input("Would you like to browse my wares? [YES/NO]")
    print(" ")
    if would_you_like_to_shop.upper() == 'YES':
        is_valid = 0
        while is_valid == 0:
            print(" ")
            print("We have consumables and materials.")
            print("1) CONSUMABLES")
            print("2) MATERIALS")
            print(" ")
            shop = input()
            if shop.upper() == 1:
                is_valid = 1
                print(" ")
                print("1) MINOR HEALTH POTION, 10 gold")
                print("2) MINOR MANA POTION, 10 gold")
                print(" ")
                shop_consumables = input()

                if shop_consumables.upper() == 1:
                    if player.gold >= minor_health_potion.cost:
                        print(" ")
                        player.gold = player.gold - minor_health_potion.cost
                        player.inventory.append(minor_health_potion)
                        print("You now have, " + player.inventory[0])

                if shop_consumables.upper() == 2:
                    if player.gold >= minor_mana_potion:
                        print(" ")
                        player.gold = player.gold - minor_mana_potion.cost
                        player.inventory.append(minor_mana_potion)
                        print("You now have, " + player.inventory[1])

            if shop.upper() == 2:
                is_valid = 1
                shop_materials = input('')

            if shop.upper() == 'NO':
                is_valid = 1

    if would_you_like_to_shop.upper() == 'NO':
        print(" ")
        print("Okay, if you change your mind, I'll be here!")
        return


def springfield_smith(player):

    print("Howdy Mate! My name is Berry, I run this shop. I have weapons, shields, and armor.")
    is_valid = 0
    while is_valid == 0:
        print(" ")
        print("1) WEAPONS")
        print("2) SHIELDS")
        print("3) ARMOR")
        print(" ")
        shop = input()
        if shop == 1:
            is_valid = 1
            print(" ")
            print("1) MELEE")
            print("2) RANGED")
            print(" ")
            shop_weapons = input("")
            if shop_weapons == '1':
                print(" ")
                print("1) ROUGH IRON SWORD, averages 10 slash damage, 20 gold.")
                print("2) RUSTY SPIKED CLUB, averages of 8 blunt damage. 18 gold")
                print(" ")
                shop_melee = input()
                if shop_melee == 1:
                    if player.gold >= rough_iron_sword.cost:
                        print(" ")
                        player.gold = player.gold - rough_iron_sword.cost
                        player.weapons.append(rough_iron_sword)

                if shop_melee == 2:
                    if player.gold >= rusty_spiked_club.cost:
                        print(" ")
                        player.gold = player.gold - rusty_spiked_club.cost
                        player.weapons.append(rusty_spiked_club)

            if shop_weapons == '2':
                print(" ")
                print("1) HUNTING BOW, averages 12 distraction damage, 25 gold")
                print("2) RUSTY FLINT LOCK PISTOLS, average 15 explosive damage, 30 gold")
                print(" ")
                shop_ranged = input()
                if shop_ranged == 1:
                    if player.gold >= hunting_bow.cost:
                        print(" ")
                        player.gold = player.gold - hunting_bow.cost
                        player.weapons.append(hunting_bow)

                if shop_ranged == 2:
                    if player.gold >= rusty_flint_lock_pistol.cost:
                        print(" ")
                        player.gold = player.gold - rusty_flint_lock_pistol.cost
                        player.weapons.append(rusty_flint_lock_pistol)

        if shop.upper() == 'SHIELDS':
            is_valid = 1

        if shop.upper() == 'ARMOR':
            is_valid = 1

