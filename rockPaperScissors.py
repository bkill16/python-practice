import random

user_input = " "
user_choice = " "
comp_choice = 0

print("\nWelcome to Rock, Paper, Scissors!")

while user_input != "4":

    print("\n1. Rock\n2. Paper\n3. Scissors\n4. Quit")
    user_input = input("Enter choice: ")

    if user_input == "4":
        print("\nGoodbye\n")
        break

    if user_input == "1":
        user_choice = "Rock"
    elif user_input == "2":
        user_choice = "Paper"
    elif user_input == "3":
        user_choice = "Scissors"
    else:
        print("Error getting user choice")

    comp_input = random.randint(1, 3)

    if comp_input == 1:
        comp_choice = "Rock"
    elif comp_input == 2:
        comp_choice = "Paper"
    elif comp_input == 3:
        comp_choice = "Scissors"
    else:
        print("Error getting computer choice")

    print(f"You chose {user_choice}")
    print(f"Computer chose {comp_choice}")

    if user_choice == comp_choice:
        print("Tie. Nobody wins :(")
    elif user_choice == "Paper" and comp_choice == "Rock":
        print("You win! Good job!")
    elif user_choice == "Rock" and comp_choice == "Paper":
        print("Computer wins! You suck!")
    elif user_choice == "Rock" and comp_choice == "Scissors":
        print("You win! Good job!")
    elif user_choice == "Scissors" and comp_choice == "Rock":
        print("Computer wins! You suck!")
    elif user_choice == "Scissors" and comp_choice == "Paper":
        print("You win! Good job!")
    elif user_choice == "Paper" and comp_choice == "Scissors":
        print("Computer wins! You suck!")
    else:
        print("Error determining winner")