import random
import time
from ClassFile import Player
from ClassFile import Weapon
from ClassFile import Shield
from ClassFile import HealthPotion
from ClassFile import Monster

def monster_turn(player, monster):
    monster_attack = random.randint(monster.min_damage, monster.max_damage)
    player_shield_shield = random.randint(player.shields[0].min_block, player.shields[0].max_block)
    player.health = player.health - monster_attack
    print("The " + monster.name + " attacked you for " + str(monster_attack))
    print("You have", player.health, "health remaining")

def player_turn(player, monster):
    player_attack_sword = random.randint(player.weapons[0].min_damage, player.weapons[0].max_damage)
    player_attack_bow = random.randint(player.weapons[1].min_damage, player.weapons[1].max_damage)
    print("")
    print("")
    print("")
    print("Would you like to ")
    print("1) attack with " + player.weapons[0].name)
    print("2) attack with " + player.weapons[1].name)
    print("3) block with " + player.shields[0].name)
    print("4) use an item")
    print("")
    action = input()
    print("")
    if action == "1":
        monster.health = monster.health - player_attack_sword
        print("You damaged the " + monster.name + " for " + str(player_attack_sword) + ". " + monster.name + " has " + str(monster.health))

    if action == "2":
        monster.health = monster.health - player_attack_bow
        print("You damaged the " + monster.name + " for " + str(player_attack_bow) + ". " + monster.name + " has " + str(monster.health))

    if action == "3":
        player.raiseShield = 1
        print("You ready your shield.")

    if action == "4":
        item = input('Would you like to use a ' + player.inventory[0].name + '? ')
        if item.upper() == player.inventory[0].name.upper():
            player.health = player.health + player.inventory[0].restore_health
            print("You healed for " + str(player.inventory[0].restore_health) + ". Now you have " + str(player.health) + " remaining")
        else:
            player_turn(player, monster)

def monster_encounter(player, monster):
    print("You encounter a " + monster.name + ". Do you ")
    print("1) Flee")
    print("2) Fight")
    print("")
    encounter = input()
    print("")
    if encounter == '1':
        print("Cowards!")
    if encounter == '2':
        random_num = random.randint(1, 2)
        while player.health > 0 and monster.health > 0:
            if random_num == 1:
                # PLAYER ATTACKS FIRST
                player_turn(player, monster)
                monster_turn(player, monster)

            if random_num == 2:
                # MONSTER ATTACKS FIRST
                monster_turn(player, monster)
                player_turn(player, monster)

        if player.health < 1:
            print("You Are Dead, RIP", player.name)
        if monster.health < 1:
            print("You killed the", monster.name)
            player.add_xp(monster.xp)
            print("You gained " + str(monster.xp) + " xp.")
