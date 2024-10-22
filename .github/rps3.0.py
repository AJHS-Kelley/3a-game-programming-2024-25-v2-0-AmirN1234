# Rock, Paper, and Scissors by Amir Norflett, v3.3a

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
def playerName() -> str: # Function Signature -- name of function, (arugments if any)
    """Gets the name from the player and returns it."""
    # The line abve is a DOCSTRING, it gives a brief example of what the function does. 































def playerChoice() -> str:
    """Allows the player to choose rock, paper, scissors."""
    playerChoice = input("Please enter rock, paper, scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissor":
        playerChoice = input ("Please enter rock, paper, scissors and press enter.\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissor":
            print("You are not following directions. Please try again.\n")
            exit()
        print(f"You have chosen {playerchoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n") 
    return playerChoice

def cpuChoice() -> str:
    """Allows the CPU to choose rock, paper, scissors."""
    cpuChoice = random.randint(0,2) # randomly select 0, 1, or 2. 
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = "scissors"
    elif cpuChoice == 2:
        cpuChoice = "paper"        
    else:
        print("Unable to determine CPU choice.\nPlease restart.\n")
        exit()
    return cpuChoice

def pickwinner(playerChoice: str, cpuChice: str) -> str:
    """Determines the winner using player and cpu choices."""
    if playerChoice == "rock" and cpuChoice == "paper":
        # CPU WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        return "CPU Wins"
    elif playerChoice == "rock" and cpuChoice == "scissors":
        # PLAYER WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1 
        return "Player Wins"
    elif playerChoice == "rock" and cpuChoice == "rock":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        return "Draw"
    elif playerChoice == "scissors" and cpuChoice == "rock":
        # CPU WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1 
        return "CPU Wins"
    elif playerChoice == "scissors" and cpuChoice == "paper":
        # PLAYER WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1 
        return "Player Wins"
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        # DRAW 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "rock":
        # PLAYER WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
        return "Player Wins"
    elif playerChoice == "paper" and cpuChoice == "paper":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "scissors":
        # CPU WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1 
        return "CPU Wins"
    else:
        # CPU WINS 
        exit()

def score(winner: str) -> int:
    """This function uses the winner to update the score for CPU, Num. DRAWS, and player score."""





        
   return score 