from ClassFile import Quest
from ClassFile import Player
from ClassFile import Weapon
from ClassFile import Shield
from ClassFile import HealthPotion
from ClassFile import ManaPotion
from ClassFile import Monster
from MonsterEncounterFunction import monster_encounter
from Adventure import springfield_intro

# Defined Quest
save_springfield = Quest(name='Save Springfield', objective="Kill 5 Boars", gold=5, xp=10)

# Defined Player
player = Player(name='PlaceHolder', max_health=50, max_mana=0)

# Defined Weapons
dull_sword = Weapon(name='DULL SWORD', min_damage=5, max_damage=10, damage_type='Slash')
rugged_bow = Weapon(name='RUGGED BOW', min_damage=6, max_damage=8, damage_type='Distraction')

player.weapons.append(dull_sword)
player.weapons.append(rugged_bow)

# Defined Shields
wooden_shield = Shield(name='WOODEN SHIELD', min_block=10, max_block=20)

player.shields.append(wooden_shield)

# Defined Health Potion
minor_health_potion = HealthPotion(name='MINOR HEALTH POTION', restore_health=12, cost=10)

player.inventory.append(minor_health_potion)

# Defined Mana Potion
minor_mana_potion = ManaPotion(name='MINOR MANA POTION', restore_mana=5, cost=10)

# Defined Creatures
boar = Monster(name='Boar', max_health=12, min_damage=3, max_damage=6, weakness='Fire', xp=2)
wolf = Monster(name='Wolf', max_health=25, min_damage=5, max_damage=8, weakness='Fire', xp=5)
dragon = Monster(name='Dragon', max_health=1200, min_damage=25, max_damage=50, weakness='Frost', xp=5000)

print("Hello Traveler")
u_name = input("What is your name? ")
player.name = u_name
print("Nice to meet you", player.name, "you have", player.health, "health ")
monster_encounter(player, boar)
#springfield_intro(player)