import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_input = input("What's your choice? 0 for rock, 1 for paper, 2 for scissors?\n")
if user_input == "0":
    print(rock)
elif user_input == "1":
    print(paper)
elif user_input == "2":
    print(scissors)

print("computer choice:\n")
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if computer_choice == int(user_input):
    print("It's a draw!")
else:
    if computer_choice == 0 and int(user_input) == 1:
        print("You win!")
    if computer_choice == 0 and int(user_input) == 2:
        print("You lose!")
    if computer_choice == 1 and int(user_input) == 2:
        print("You win!")
    if computer_choice == 1 and int(user_input) == 0:
        print("You lose!")
    if computer_choice == 2 and int(user_input) == 0:
        print("You win!")
    if computer_choice == 2 and int(user_input) == 1:
        print("You lose!")
