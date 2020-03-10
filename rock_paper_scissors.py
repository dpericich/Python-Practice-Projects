## Rock, Paper, Scissor Game
# Create a game for a single player to play against the computer
# My personal take on the game (horribly coded, but it works)
from random import randint

computer = randint(0,2)
# 0 will be Rock, 1 will be Paper and 2 will be scissors

welcome = "Welcome to Rock Paper Scissors!\nPlease type in \"Rock\", \"Paper\", or \"Scissors.\": "

human = input(welcome)

print(human.lower())
if(human == "rock"):
    human = 0
elif(human == "paper"):
    human = 1
elif(human == "scissors"):
    human = 2
else:
    print("That is not an option")

if(computer == 0):
    print("rock")
elif(computer == 1):
    print("paper")
elif(computer == 2):
    print("scissors")

if(human == 0 and computer == 0):
    print("Tie")
elif(human == 0 and computer == 1):
    print("The computer wins...")
elif(human == 0 and computer == 2):
    print("You win!")
elif(human == 1 and computer == 0):
    print("You win!")
elif(human == 1 and computer == 1):
    print("Tie")
elif(human == 1 and computer == 2):
    print("The computer wins..")
elif(human == 2 and computer == 0):
    print("The computer wins...")
elif(human == 2 and computer == 1):
    print("You win!")
elif(human == 2 and computer == 2):
    print("Tie")