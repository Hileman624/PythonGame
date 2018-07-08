import time
import random

class MultiplayerGame:
    def __init__(self):
        self.started = False
        self.player1 = None
        self.player2 = None
        self.turn = 0
        self.lastMessage = ""

    def player_action(self, player, monster, action):
        player_attack_sword = random.randint(player.weapons[0].min_damage, player.weapons[0].max_damage)
        player_attack_bow = random.randint(player.weapons[1].min_damage, player.weapons[1].max_damage)
        result = ""
        if action == "1":
            monster.health = monster.health - player_attack_sword
            result = player.name + " damaged " + monster.name + " for " + str(player_attack_sword) + ". "
            if monster.health < 0:
                monster.health = 0
                result += monster.name + " has 0 health remaining."
            else:
                result += (monster.name + " has " + str(monster.health) + " health remaining.")

        if action == "2":
            monster.health = monster.health - player_attack_bow
            result = player.name + " damaged " + monster.name + " for " + str(player_attack_bow) + ". "
            if monster.health < 0:
                monster.health = 0
                result += monster.name + " has 0 health remaining."
            else:
                result += monster.name + " has " + str(monster.health) + " health remaining."

        if action == "3":
            player.raiseShield = 1
            result = player.name + " raised shield."

        if action == "4":
            player.health = player.health + player.inventory[0].restore_health
            result = player.name + " healed for " + str(player.inventory[0].restore_health) + ". " + str(player.health) + " health remaining."
        self.lastMessage = result
        return result
