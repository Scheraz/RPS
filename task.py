import random
from random import randint

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
computer_choice = random.randint(0, 2)
#rock = 0, paper = 1, scissors = 2
#0 + 2 = win
#2 + 1 = win
#1 + 0 = win

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_signs = [rock, paper, scissors]

print(game_signs[user_choice])
print(f"Computer Chose:")
print(game_signs[computer_choice])

# Invalid Scenario

if user_choice >= 3 or user_choice < 0:
    print("You put an invalid number. Choose again.")

#Draw scenario

elif user_choice == computer_choice:
    print("It's a draw. Choose again!")

#Win scenario:

elif user_choice > computer_choice:
    print("You win!")
elif user_choice == 0 and computer_choice == 2:
    print ("You win!")

#Lose Scenario

elif computer_choice > user_choice:
    print("You lost")
elif computer_choice == 0 and user_choice == 2:
    print("You lost!")







