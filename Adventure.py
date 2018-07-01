
from random import *
from ClassFile import Player
from ClassFile import Weapon
from ClassFile import Shield
from ClassFile import HealthPotion
from ClassFile import Monster
from MonsterEncounterFunction import monster_encounter
from Shops_an_Stuff import springfield_shop


def springfield_intro(player):

    print("Thank you, " + player.name + " you saved our town from sure destruction!")
    print("PLease take this as your reward, " + player.gold + 5)
    print("This is the town of Springfield, and I am the Mayor. My name is Mark West.")
    print("We have many shops, smiths, and even hospitals.")

    is_valid = 0
    while is_valid == 0:
        explore = input("Would you like to visit any of the shops? [SHOP/SMITH/HOSPITALS] or [NO} ")
        if explore.upper() == 'SHOP':
            is_valid = 1
            springfield_shop(player)
            is_valid = 0

        if explore.upper() == 'SMITH':
            is_valid = 1
            springfield_smith(player)
            is_valid = 0

        if explore.upper() == 'HOSPITALS':
            is_valid = 1
            hospital(player)
            is_valid = 0

        if explore.upper() == 'NO':
            is_valid = 1
            print('Okay, Okay')


