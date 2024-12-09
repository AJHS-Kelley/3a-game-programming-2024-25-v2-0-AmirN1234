# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# You are behind and I am concerned you will not finish by the due date. 
# There has been almost no new code added to the project. 
# 2024-12-09 -- You have added some code, but the project is not finished.  You have until 2024-12-16 @ 3:00PM to resubmit. 

# MODULE IMPORTS
import random
import time
import datetime 

# SAVING DATA TO A FILE 
# STEP 1 -- Create the file name to use.
logFileName = "dragonRealmLog" + str(time.time()) + "txt."
# Example:  dragonRealmLog1132AM.txt

# STEP 2 -- Create / Open the file to save the data
saveData = open(logFileName, "x")
# FILE MODES 
# "x" CREATES FILE, IF FILE EXISTS, EXIT WITH ERROR MESSAGE 
# "w" CREATES FILE, IF THE FILE EXISTS, ERASE AND OVERWRITE FILE CONTENTS 
# "a" CREATES FILE, IF THE FILE EXISTS, APPEND DATA TO THE FILE 


saveData.write("GAME STARTED" + " " + str(datetime.datetime.now())+ "\n")


def displayIntro():

    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')
        print("Game Over")


playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()


# using Booleans for Items 
hasSword = False
damage = random.randint(1,6)
pickUpItem = input()




