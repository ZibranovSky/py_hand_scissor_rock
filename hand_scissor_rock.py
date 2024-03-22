#hand scissor rock

import random as rand
import time

print("Simple hand scissor and rock game \n")
word = ["scissor","hand","rock"]

player_choice = input("Enter your choice (hand/scissor/rock) : ")

computer_choice = rand.choice(word)

print("wait while your enemy choice its decision....")

time.sleep(2)

print("your enemy release {} ".format(computer_choice))

if player_choice == "hand" and computer_choice == "hand":
    print("Draw")
elif player_choice == "hand" and computer_choice == "scissor":
    print("You lose to your enemy")
elif player_choice == "hand" and computer_choice == "rock":
    print("You win!!")
elif player_choice == "scissor" and computer_choice == "hand":
    print("You win!!")
elif player_choice == "scissor" and computer_choice == "scissor":
    print("Draw")
elif player_choice == "scissor" and computer_choice == "rock":
    print("You lose to your enemy")
elif player_choice == "rock" and computer_choice == "hand":
    print("You lose to your enemy")
elif player_choice == "rock" and computer_choice == "scissor":
    print("You win!!")
elif player_choice == "rock" and computer_choice == "rock":
    print("Draw")
else:
    print("wrong input!")


close = input("program end (enter) ")