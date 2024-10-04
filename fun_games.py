import random

options = ["rock","paper","scissors"]

user_input =  input("choose rock, paper or scissors:")

computer_choice = random.choice(options)


print("user choose",user_input)
print("computer choose",computer_choice)

if user_input == computer_choice:
    print("tie")
elif user_input == "rock" and computer_choice == "scissors":
    print("user win")

elif user_input == "rock" and computer_choice == "paper":
    print("computer win")

elif user_input == "scissors" and computer_choice == "paper":
    print("user win")

else:
    print("computer wins")