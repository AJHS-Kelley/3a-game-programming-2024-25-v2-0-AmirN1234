# Rock, Paper, and Scissors by Amir Norflett, v0.1 

# MODULE IMPORTS 
import random, time

# DATA STRUCTURES -- PLAYER 
playerScore = 0 
playerChoice = None
numDraws = 0

# DATA STRCUTURES -- CPU
cpuScore = 0 
cpuChoice = None

# MAIN GAME LOOP 
loopCount = 0 
loopsReq = input("How many loops do you want?\nEnter an integer, no commas, and press enter.\n")
# req is the universal abbreviation in computer programming for REQUEST. reqs = REQUEST
rpsTimeStart = time.time() # returns the number of seconds since Jan. 01, 1970 @ 12:00AM
while loopCount < loopsReq: 


# let cpu select choice at random
 cpuChoice = random.randint(0, 2) # randomly select 0, 1, 2.   
if cpuChoice == 0:
    cpuChoice = "rock"
elif cpuChoice == 1:
    cpuChoice = "scissors"
elif cpuChoice == 2:
   cpuChoice = "paper"
else:
    print ("Unable to determine CPU choice.\nPlease restart.\n")
    exit()
# print(f"CPU choice: {cpuchoice}")

# let cpu select choice at random
playerChoice = random.randint(0, 2) # randomly select 0, 1, 2.   
if playerChoice == 0:
    playerChoice = "rock"
elif playerChoice == 1:
    playerChoice = "scissors"
elif playerChoice == 2:
   playerChoice = "paper"
else:
    print ("Unable to determine CPU choice.\nPlease restart.\n")
    exit()
# compare player choice to cpu choice 
if playerChoice == "rock" and cpuChoice == "paper":
    print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
    print("The CPU wins a point.\n")
    pass 
    # CPU WINS
elif playerChoice == "rock" and cpuChoice == "scissors":
    print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
    print("You win a point.\n")
    playerScore +=1
    pass 
    # DRAW
elif playerChoice == "rock" and cpuChoice == "rock":
    print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
    print("The CPU wins a point.\n")
    pass
   # DRAW
elif # PLAYER CHOOSE SCISSORS, CPU CHOOSE ROCK:
    pass
    # CPU WINS 






































rpsTimeStop = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"Number of Loops: {loopCount}\n")
print(f"Execution Time {rpsTime: .2F} seconds.\n") # :.2F formats to 2 decimal places.