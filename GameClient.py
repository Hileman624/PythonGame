import requests
import time
import sys

playerName = input("What is your name?")
print("Hello " + playerName)

serverAddress = input("Please enter server address: ")
try:
    serverInfo = requests.get(serverAddress+"/").text
except:
    print("Failed to connect. Goodbye.")
    sys.exit()

print("")
print("Would you like to create or join a multiplayer game?")
print("1) Create a game")
print("2) Join a game")
createOrJoin = input(": ")

# create or join multiplayer game
if createOrJoin == "1":
    print("OK, creating game...")
    response = requests.get(serverAddress+"/game-create")
    print(response.text)
    print("Joining game...")
    response = requests.get(serverAddress+"/game-join?name="+playerName)
    print(response.text)
else:
    print("OK, joining game...")
    response = requests.get(serverAddress+"/game-join?name="+playerName)
    print(response.text)

# wait for others to join
gameStatus = requests.get(serverAddress+"/game-status").text
while "Waiting for game to start." not in gameStatus:
    print(gameStatus)
    gameStatus = requests.get(serverAddress+"/game-status").text
    time.sleep(5)
print(gameStatus)

# start the game
gameStatus = requests.get(serverAddress+"/game-start").text
print(gameStatus)

matchStatus = requests.get(serverAddress+"/match-status").text
while "The match has ended." not in matchStatus:
    isMyTurn = requests.get(serverAddress+"/check-turn?name="+playerName).text
    if isMyTurn == "no":
        print("waiting for turn")
    else:
        # show the other player's last action
        lastActionMsg = requests.get(serverAddress+"/get-previous-player-action").text
        print("")
        print(lastActionMsg)
        time.sleep(1)
        # do my turn here
        print("")
        print("Would you like to ")
        time.sleep(.5)
        print("1) attack with DULL SWORD")
        time.sleep(.5)
        print("2) attack with RUGGED BOW")
        time.sleep(.5)
        print("3) block with WOODEN SHIELD")
        time.sleep(.5)
        print("4) use a HEALTH POTION")
        print("")
        action = input(": ")
        actionMsg = requests.get(serverAddress+"/do-action?name="+playerName+"&action="+action).text
        print(actionMsg)

    time.sleep(10)
    matchStatus = requests.get(serverAddress+"/match-status").text

matchStatus = requests.get(serverAddress+"/match-status").text
print(matchStatus)