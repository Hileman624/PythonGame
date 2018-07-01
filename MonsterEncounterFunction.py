
import random
from ClassFile import Player
from ClassFile import Weapon
from ClassFile import Shield
from ClassFile import HealthPotion
from ClassFile import Monster


def monster_encounter(player, monster):
    encounter = input("You encounter a " + monster.name + " [FLEE/FIGHT] ")
    if encounter.upper() == 'FLEE':
        print("Cowards!")
        return
    if encounter.upper() == 'FIGHT':
        random_num = random.randint(1, 2)
        while player.health > 0 and monster.health > 0:
            if random_num == 1:
                # PLAYER ATTACKS FIRST
                player_attack_sword = random.randint(player.weapons[0].min_damage, player.weapons[0].max_damage)
                player_attack_bow = random.randint(player.weapons[1].min_damage, player.weapons[1].max_damage)
                player_shield_shield = random.randint(player.shields[0].min_block, player.shields[0].max_block)
                monster_attack = random.randint(monster.min_damage, monster.max_damage)

                action = input("Would you like to attack " + monster.name + " with " + player.weapons[0].name + " or " + player.weapons[1].name + ", or would you like to use " + player.shields[0].name + " or an item? ")
                if action.upper() == player.weapons[0].name.upper():
                    monster.health = monster.health - player_attack_sword
                    print("You damaged the " + monster.name + " for " + str(player_attack_sword) + ". " + monster.name + " has " + str(monster.health))
                    player.health = player.health - monster_attack
                    print("You have", player.health, "health remaining")

                if action.upper() == player.weapons[1].name.upper():
                    monster.health = monster.health - player_attack_bow
                    print("You damaged the " + monster.name + " for " + str(player_attack_bow) + ". " + monster.name + " has " + str(monster.health))
                    player.health = player.health - monster_attack
                    print("You have", player.health, "health remaining")

                if action.upper() == player.shields[0].name.upper():
                    player.health = player.health + (monster_attack - player_shield_shield)
                    print("You block the " + monster.name + "attack")

                if action.upper() == 'ITEM':
                    item = input('Would you like to use a ' + player.inventory[0].name + '? ')
                    if item.upper() == player.inventory[0].name.upper():
                        player.health = player.health + player.inventory[0].restore_health
                        print("You healed for " + str(player.inventory[0].restore_health) + ". Now you have " + str(player.health) + " remaining")
                    else:
                        return

            if random_num == 2:
                # MONSTER ATTACKS FIRST
                player_attack_sword = random.randint(player.weapons[0].min_damage, player.weapons[0].max_damage)
                player_attack_bow = random.randint(player.weapons[1].min_damage, player.weapons[1].max_damage)
                player_shield_shield = random.randint(player.shields[0].min_block, player.shields[0].max_block)
                monster_attack = random.randint(monster.min_damage, monster.max_damage)

                player.health = player.health - monster_attack
                print("The " + monster.name + " attacked you for " + str(monster_attack))
                print("You have", player.health, "health remaining")
                action = input("Would you like to attack " + monster.name + " with " + player.weapons[0].name + " or " + player.weapons[1].name + ", or would you like to use " + player.shields[0].name + " or an item? ")
                if action.upper() == player.weapons[0].name.upper():
                    monster.health = monster.health - player_attack_sword
                    print("You damaged the " + monster.name + " for " + str(player_attack_sword) + ". " + monster.name + " has " + str(monster.health))

                if action.upper() == player.weapons[1].name.upper():
                    monster.health = monster.health - player_attack_bow
                    print("You damaged the " + monster.name + " for " + str(player_attack_bow) + ". " + monster.name + " has " + str(monster.health))

                if action.upper() == player.shields[0].name.upper():
                    monster_attack = monster_attack - player_shield_shield
                    if monster_attack < 0:
                        monster_attack = 0
                    player.health = player.health - monster_attack
                    print("You block the " + monster.name + "attack")

                if action.upper() == 'ITEM':
                    item = input('Would you like to use a ' + player.inventory[0].name + '? ')
                    if item.upper() == player.inventory[0].name.upper():
                            player.health = player.health + player.inventory[0].restore_health
                            print("You healed for " + str(player.inventory[0].restore_health) + ". Now you have " + str(player.health) + " remaining")
                    else:
                        return

        if player.health < 1:
            print("You Are Dead, RIP", player.name)
        if monster.health < 1:
            print("You killed the", monster.name)
            player.add_xp(monster.xp)
            print("You gained " + str(monster.xp) + " xp.")
