## Guess the number project
from random import randint

computer = randint(0,20)

# Create all response strings
welcome = "Welcome to Guess the number!\nIf you pick the right number, you win!!"
msg1 = "Enter a number between 0 and 20: "
win = "You won! The number is "
high = "Your guess was too high..."
low = "Your guess was too low..."

print(welcome)
guesses = []
count = 0
while(count < 5):
    guess = input(msg1)
    guess = int(guess)
    if(guess == computer):
        print(win + str(guess) + "!")
        break
    elif(guess > computer):
        print(high)
    else:
        print(low)
    guesses.append(guess)
    print(guesses)
    count +=count