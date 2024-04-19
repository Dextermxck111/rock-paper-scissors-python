from art import rock, paper, scissors
import random

user_pick = int(input("What will you choose? Type 0 for rock, 1 for paper, and 2 for scissors. "))

choices = [rock, paper, scissors]

computer_pick = random.choice(choices)

if user_pick == 0:
    user_pick = rock
elif user_pick == 1:
    user_pick = paper
elif user_pick == 2:
    user_pick = scissors

if user_pick == computer_pick:
    print(user_pick)
    print("\n")
    print(computer_pick)
    print("Draw, you chose the same thing as the computer.")
elif user_pick is rock and computer_pick is paper:
    print(user_pick)
    print("\n")
    print(computer_pick)
    print("You lose, paper beats rock.")
elif user_pick is paper and computer_pick is rock:
    print(user_pick)
    print("\n")
    print(computer_pick)
    print("You win, paper beats rock.")
elif user_pick is paper and computer_pick is scissors:
    print(user_pick)
    print("\n")
    print(computer_pick)
    print("You lose, scissors beats paper.")
elif user_pick is scissors and computer_pick is paper:
    print(user_pick)
    print("\n")
    print(computer_pick)
    print("You win, scissors beats paper.")
elif user_pick is scissors and computer_pick is rock:
    print(user_pick)
    print("\n")
    print(computer_pick)
    print("You lose, rock beats scissors.")
elif user_pick is rock and computer_pick is scissors:
    print(user_pick)
    print("\n")
    print(computer_pick)
    print("You win, rock beats scissors.")