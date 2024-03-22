#hand scissor rock

import random as rand
import time

print("Simple hand scissor and rock game \n")
word = ["scissor","hand","rock"]


repeat = "y"

while repeat != "n":
    
    player_choice = input("Enter your choice (hand/scissor/rock) : \n")


    print("\n")

    computer_choice = rand.choice(word)

    print("wait while your enemy choice....")

    time.sleep(2)

    print("your enemy release {} ".format(computer_choice))

    if player_choice == "hand" and computer_choice == "hand":
        print("Draw")
        print("\n")
        repeat = input("repeat program ? (y/n) ")
    elif player_choice == "hand" and computer_choice == "scissor":
        print("You lose to your enemy")
        print("\n")
        repeat = input("repeat program ? (y/n) ")
    elif player_choice == "hand" and computer_choice == "rock":
        print("You win!!")
        print("\n")
        repeat = input("repeat program ? (y/n) ")
    elif player_choice == "scissor" and computer_choice == "hand":
        print("You win!!")
        print("\n")
        repeat = input("repeat program ? (y/n) ")
    elif player_choice == "scissor" and computer_choice == "scissor":
        print("Draw")
        print("\n")
        repeat = input("repeat program ? (y/n) ")
    elif player_choice == "scissor" and computer_choice == "rock":
        print("You lose to your enemy")
        print("\n")
        repeat = input("repeat program ? (y/n) ")
    elif player_choice == "rock" and computer_choice == "hand":
        print("You lose to your enemy")
        print("\n")
        repeat = input("repeat program ? (y/n) ")
    elif player_choice == "rock" and computer_choice == "scissor":
        print("You win!!")
        print("\n")
        repeat = input("repeat program ? (y/n) ")
    elif player_choice == "rock" and computer_choice == "rock":
        print("Draw")
        print("\n")
        repeat = input("repeat program ? (y/n) ")
    else:
        print("wrong input!")
        print("\n")
        repeat = input("repeat program ? (y/n) ")

    if repeat == "y":
        continue
    else:
        break

close = input("program end (enter) ")