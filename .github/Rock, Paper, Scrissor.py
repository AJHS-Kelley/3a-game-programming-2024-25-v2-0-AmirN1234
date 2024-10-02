# Rock, Paper, and Scissors by Amir Norflett, v0.1 

# MODULE IMPORTS 
import random 

# DATA STRUCTURES -- PLAYER 
playerScore = 0 
playerName = "Test Player"
playerChoice = None

# DATA STRCUTURES -- CPU
cpuScore = 0 
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Amir Norflett.\n")
print(f"Hello {playerName}!.\n")
isCorrect = input ("Is that Correct?  Type yes or no and press enter.\n")

# .lower() can turn all input into lowercase
# .upper() can turn all input into UPPERcase

if isCorrect == "yes":
    print(f"Ok {playerName}, let's play Rock, Paper, Scissor!.\n")    
else: 
    Amir = input("AmirNorflett.\n")

# THE RULES using MULTI-LINE STRINGS 
print(f"")
Welcome, {playerName} to the Rock, Paper, Scissors Robot!
It




















# MAIN GAME LOOP 
while playerScore < 5 and cpuScore < 5: 
    print(f""{Amir} you have {playerScore} points.nThe cpu has {cpuScore}) 
    playerChoice = input("Please enter rock, paper, or scrissors amd press enter.\n")
if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissor":
   playerChoice = input("Please enter rock, paper, or scissors and press enter .\n").lower()  
   if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
       print()


else: 
    print(f"You have chosen {playerChoice}.\n")

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


elif playerChoice == "Scissors" and cpuChoice == "Scissors":
    # DRAW
    print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
    print("It's a draw!\n")
elif playerChoice == "paper" and cpuChoice == "rock":
    # PLAYER WINS

















print(f"Your Final Score: {playerScore}\nCPU Final Score: {cpuScore}\n")
if playerScore > cpuScore: 
    print(f"Congratulations {playerName}, a winner is you!\n")
elif cpuScore > playerScore:
    print(f"The CPU wins. You are a disappointment to all.\n")
else:
    print("Unable to determine a winner.\nPlease restart.\n")
    exit()