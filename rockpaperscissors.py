import random
from enum import Enum
 
class Type(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3

def play_game():
    print("Type nbr to choose an option: \n 1 : Rock \n 2 : Paper \n 3 : Scissor")
    print("")
       
    userInput = input("\nChoose option: ")
    computerPlayer = random.randrange(1,4)
    
    #system.os("cls")
    print("Player: ", Type(int(userInput)).name)
    print("Computer: ", Type(computerPlayer).name)
    
    if int(userInput) == int(computerPlayer):
        print("\nResult: It's a draw")
    elif (int(userInput) == 1 and int(computerPlayer) == 3):
        print("\nPLAYER WINS!!")
    elif (int(userInput) == 2 and int(computerPlayer) == 1):
        print("\nPLAYER WINS!!")
    elif (int(userInput) == 3 and int(computerPlayer) == 2):
        print("\nPLAYER WINS!!")
    else:
        print("\nCOMPUTER WINS!!")
        
while True:
    answer = input("\nDo you want to play a game of rock, paper and scissors? (y or n): ")
    if answer == 'y':
        play_game()
    elif answer == 'n':
        break
    else:
        print("Try again")
