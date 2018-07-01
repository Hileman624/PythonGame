
import random
from ClassFile import Player
from ClassFile import Weapon
from ClassFile import Ammo
from ClassFile import Shield
from ClassFile import Armor
from ClassFile import HealthPotion
from ClassFile import ManaPotion
from ClassFile import Materials
from ClassFile import Monster
from MonsterEncounterFunction import monster_encounter

# Defined Consumables
minor_health_potion = HealthPotion(name='MINOR HEALTH POTION', restore_health=12, cost=10)
minor_mana_potion = ManaPotion(name='MINOR MANA POTION', restore_mana=5, cost=10)

# AMMO
wooden_arrow_with_flint_tip = Ammo(name='WOODEN ARROW (FLINT TIP)', min_damage=1, max_damage=3, damage_type='None', cost=6)

# Defined Melee Weapons
rough_iron_sword = Weapon(name='ROUGH IRON SWORD', min_damage=8, max_damage=12, damage_type='Slash', cost=20)
rusty_spiked_club = Weapon(name='RUSTY SPIKED CLUB', min_damage=6, max_damage=10, damage_type='Blunt', cost=18)

# Defined Ranged Weapons
hunting_bow = Weapon(name='HUNTING BOW', min_damage=8, max_damage=16, damage_type=' ', cost=25)

# Defined Shields
iron_shield = Shield(name='IRON SHIELD', min_block=20, max_block=30, cost=35)

# Defined Materials
feather = Materials(name='FEATHER', cost=1)
wooden_arrow_shaft = Materials(name='WOODEN ARROW SHAFT', cost=2)
flint_arrow_head = Materials(name='FLINT ARROW HEAD', cost=2)

# Defined Armor
leather_helm = Armor(name='LEATHER HELM', damage_reduction=2, cost=35)
leather_chest = Armor(name='LEATHER CHEST', damage_reduction=3, cost=40)
leather_gloves = Armor(name='LEATHER GLOVES', damage_reduction=1, cost=30)
leather_pants = Armor(name='LEATHER PANTS', damage_reduction=3, cost=40)
leather_boots = Armor(name='LEATHER BOOTS', damage_reduction=1, cost=30)


def springfield_shop(player):
    print("Welcome," + player.name)
    would_you_like_to_shop = input("Would you like to browse my wares? [YES/NO]")
    print(" ")
    if would_you_like_to_shop == 'YES':
        is_valid = 0
        while is_valid == 0:
            print(" ")
            print("We have consumables and materials.")
            print("1) CONSUMABLES")
            print("2) MATERIALS")
            print(" ")
            shop = input()
            if shop == 1:
                is_valid = 1
                print(" ")
                print("1) MINOR HEALTH POTION, 10 gold")
                print("2) MINOR MANA POTION, 10 gold")
                print(" ")
                shop_consumables = input()

                if shop_consumables == 1:
                    if player.gold >= minor_health_potion.cost:
                        print(" ")
                        player.gold = player.gold - minor_health_potion.cost
                        player.inventory.append(minor_health_potion)
                        print("You now have, " + player.inventory[0])

                if shop_consumables == 2:
                    if player.gold >= minor_mana_potion:
                        print(" ")
                        player.gold = player.gold - minor_mana_potion.cost
                        player.inventory.append(minor_mana_potion)
                        print("You now have, " + player.inventory[1])

            if shop == 2:
                is_valid = 1
                print(" ")
                print("1) FEATHERS")
                print("2) WOODEN ARROW SHAFT")
                print("3) FLINT ARROW HEAD")
                print(" ")
                shop_materials = input()
                if shop_materials == 1:
                    if player.gold >= feather.cost:
                        print(" ")
                        player.gold = player.gold - feather.cost
                        player.crafting_inventory.append(feather)

                if shop_materials == 2:
                    if player.gold >= wooden_arrow_shaft.cost:
                        print(" ")
                        player.gold = player.gold - wooden_arrow_shaft.cost
                        player.crafting_inventory.append(wooden_arrow_shaft)

                if shop_materials == 3:
                    if player.gold >= flint_arrow_head.cost:
                        print(" ")
                        player.gold = player.gold - flint_arrow_head.cost
                        player.crafting_inventory.append(flint_arrow_head)

            if shop == 'NO':
                is_valid = 1

    if would_you_like_to_shop.upper() == 'NO':
        print(" ")
        print("Okay, if you change your mind, I'll be here!")
        return


def springfield_smith(player):

    print("Howdy Mate! My name is Berry, I run this shop. I have weapons, ammo, shields, and armor.")
    is_valid = 0
    while is_valid == 0:
        print(" ")
        print("1) WEAPONS")
        print("2) AMMO")
        print("3) SHIELDS")
        print("4) ARMOR")
        print(" ")
        smith = input()
        if smith == 1:
            is_valid = 1
            print(" ")
            print("1) MELEE")
            print("2) RANGED")
            print(" ")
            smith_weapons = input()
            if smith_weapons == 1:
                print(" ")
                print("1) ROUGH IRON SWORD, averages 10 slash damage, 20 gold.")
                print("2) RUSTY SPIKED CLUB, averages of 8 blunt damage. 18 gold")
                print(" ")
                smith_melee = input()
                if smith_melee == 1:
                    if player.gold >= rough_iron_sword.cost:
                        print(" ")
                        player.gold = player.gold - rough_iron_sword.cost
                        player.weapons.append(rough_iron_sword)

                if smith_melee == 2:
                    if player.gold >= rusty_spiked_club.cost:
                        print(" ")
                        player.gold = player.gold - rusty_spiked_club.cost
                        player.weapons.append(rusty_spiked_club)

            if smith_weapons == 2:
                print(" ")
                print("1) HUNTING BOW, averages 12 distraction damage, 25 gold")
                print(" ")
                shop_ranged = input()
                if shop_ranged == 1:
                    if player.gold >= hunting_bow.cost:
                        print(" ")
                        player.gold = player.gold - hunting_bow.cost
                        player.weapons.append(hunting_bow)

        if smith == 2:
            print(" ")
            print("1) WOODEN ARROW WITH FLINT TIP, 2 damage, 6 gold ")
            print(" ")
            smith_ammo = input()
            if smith_ammo == 1:
                if player.gold >= wooden_arrow_with_flint_tip.cost:
                    print(" ")
                    player.gold = player.gold - wooden_arrow_with_flint_tip.cost
                    player.ammo.append(wooden_arrow_with_flint_tip)

        if smith == 3:
            is_valid = 1
            print(' ')
            print('1) IRON SHIELD, average block of 25, 30 gold')
            print(" ")
            shop_shields = input()
            if shop_shields == 1:
                if player.gold >= iron_shield.cost:
                    print(" ")
                    player.gold = player.gold - iron_shield.cost
                    player.shields.append(iron_shield)

        if smith == 4:
            is_valid = 1
            print(' ')
            print("1) LEATHER HELM, 2 damage reduction, 35 gold ")
            print("2) LEATHER CHEST, 3 damage reduction, 40 gold ")
            print("3) LEATHER GLOVES, 1 damage reduction, 30 gold ")
            print("4) LEATHER PANTS, 3 damage reduction, 40 gold ")
            print("5) LEATHER BOOTS, 1 damage reduction, 30 gold ")
            smith_armor = input()
            if smith_armor == 1:
                if player.gold >= leather_helm.cost:
                    player.gold = player.gold - leather_helm.cost
                    player.inventory.append(leather_helm)

            if smith_armor == 2:
                if player.gold >= leather_chest.cost:
                    player.gold = player.gold - leather_chest.cost
                    player.inventory.append(leather_chest)

            if smith_armor == 3:
                if player.gold >= leather_gloves.cost:
                    player.gold = player.gold - leather_gloves.cost
                    player.inventory.append(leather_gloves)

            if smith_armor == 4:
                if player.gold >= leather_pants.cost:
                    player.gold = player.gold - leather_pants.cost
                    player.inventory.append(leather_pants)

            if smith_armor == 5:
                if player.gold >= leather_boots.cost:
                    player.gold = player.gold - leather_boots.cost
                    player.inventory.append(leather_boots)





