'''
    Name: Snowball-Mania
    Author: Jared Dooyema
    Date: 
    Class: AP Computer Science Principles
    Python: 
'''

import random
import time
from colorama import init, Fore, Back, Style

init()
print("Hello " + Fore.LIGHTYELLOW_EX + "World!")# + Style.RESET_ALL)


def printIntro():
    '''
    ' Param: none
    ' 
    ' Print a welcome message to the user
    ' 
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("❄️  Welcome to Snowball Mania!❄️")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def getNames():
    '''
    ' Param: none
    ' 
    ' Create a list to hold player names.
    ' Ask the user for their name.  Store it in a variable and add it to the player list.
    ' Print instructions for the user to add more players and to type "DONE" when finished.
    ' Read in the first additional player name.
    ' While the user hasn't typed "DONE", add the new name to the player list and prompt for the next name
    ' After the user is finished entering names, print a "Time to play!" message
    '
    ' Return: the list of player names
    ' 
    '''
    playerList = []
    myName = input("What is your name? ")
    playerList.append(myName)
    print("Add other players one at a time by typing their names and hitting ENTER. Type DONE when finished")
    nextName = input()
    while (nextName != "DONE"):
        playerList.append(nextName)
        nextName = input()
    print("Great! - time to play!!")
    return playerList        

def getThrower(players):
    '''
    ' Param: players (list of player names)
    '
    ' Return a randomly chosen player name to be the next thrower.
    '
    ' Return: player name
    '''
    thrower = random.choice(players)
    return thrower

    
def getVictim(players, t):
    '''
    ' Param: players (list of player names), t (the thrower for this round)
    ' 
    ' Select a random player to be the next victim.  
    ' While the victim is the same player as the thrower, randomly select a new victim from the list.
    ' Return the victim's name.
    '
    ' Return: victim's name
    '''
    victim = random.choice(players)
    while (t == victim):
        victim = random.choice(players)
    return victim


def getHitResult():
    '''
    ' Param: none
    ' 
    ' Generate a random number between 1 and 10
    ' If the number is greater than 4 (60% chance), return True
    ' Else, return False
    '
    ' Return: Boolean representing whether or not the snowball hit
    '''
    hitNum = random.randint(1, 10)
    if (hitNum > 4):
        return True
    else:
        return False
    

def playSnowballFight(players):
    '''
    ' Param: players (a list of players still in the game)
    '
    ' While there are still multiple players in the game...
    '   - Get the next thrower
    '   - Get the next victim
    '   - Get the next hit result
    '   - If a hit occurred, flip a coin to see if it is a knockout or not.
    '     - If knockout, print a knockout message and remove the victim from the list
    '     - Else, print a hit message but do not remove victim
    '   - Else, print a miss message
    '   - time.sleep(3) - delay execution for three seconds
    ' 
    ' Return: none
    '''
    while (len(players) > 1):
        thrower = getThrower(players)
        victim = getVictim(players, thrower)
        hitResult = getHitResult()
        survives1 = (thrower + " throws at "  +victim + Fore.YELLOW + " and hits, but " + victim + Fore.RED+ " survives!" + Style.RESET_ALL)
        survives2 = (thrower + " attempts to hit "  +victim + Fore.YELLOW + " and succeeds victoriously, however " + victim + Fore.RED+ " remains undeterred!" + Style.RESET_ALL)
        surviveMessages = [survives1, survives2]
        hits1 = (thrower + " throws and absolutely destroys " + Fore.GREEN + victim  + " - " + victim + Fore.CYAN+ " is out of the game!!!" + Style.RESET_ALL)
        hits2 = (thrower + " nails " + Fore.GREEN + victim  + " - " + victim + Fore.CYAN+ " is Donzos!!!" + Style.RESET_ALL)
        hitMessages = [hits1, hits2]
        miss1 =(thrower + " throws at " + victim + Fore.MAGENTA+ " but has really bad aim and misses." + Style.RESET_ALL)
        miss2 =(thrower + " trips on a hidden rock, while throwing at " + victim + Fore.MAGENTA+ " and hits nothing but a poor, innocent snowman bystander." + Style.RESET_ALL)
        missMessages = [miss1,miss2]
        if (hitResult == True):
            koResult = random.randint(1, 2)     # 1 = not KO, 2 = KO
            if (koResult == 1):
                print(random.choice(surviveMessages))
            else:
                print(random.choice(hitMessages))
                players.remove(victim)
        else:
            print(random.choice(missMessages))
        time.sleep(3)
    
def printOutro(winner):
    '''
    ' Param: name of the winner
    ' 
    ' Print a congratulatory message naming the winner
    '
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("All hail " + winner + ", the Ultimate Student/Snowball Wizard!")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def runProgram():
    '''
    ' Param: none
    ' 
    ' Call the method that will print the intro messages
    ' Call the method that will return a list of player names.  Save the list in a variable.
    ' Call the method that will simulate the snowball fight
    ' Call the method that will print the outro messagees
    '
    ' Return: none
    '''
    printIntro()
    #testPlayers = ["Jack", "Sam", "Eliana", "Aanya", "Izaiah", "Audrey", "Elam", "John", "Jared", "Aron", "Sebastien", "Tyler", "Collin", "Taylor", "Will", "Nolan", "Llyden", "Xavier", "Landon", "Mr. Holthouse", "Mr. Yeh"]
    testPlayers = getNames()
    playSnowballFight(testPlayers)
    printOutro(testPlayers[0])

runProgram()



# testThrower = getThrower(testPlayers)
# testVictim = getVictim(testPlayers, testThrower)
# testHit = getHitResult()

# # successful hit
# if (testHit == True):
#     print(testThrower + " throws at " + testVictim + " - HIT")
# # miss
# else:
#     print(testThrower + " throws at " + testVictim + " - MISS")

