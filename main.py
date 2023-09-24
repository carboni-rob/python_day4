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

#Write your code below this line 👇
import random

result_map = [["Draw", "You win", "You lose"],
              ["You lose", "Draw", "You win"],
              ["You win", "You lose", "Draw"]]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_choice >= 3 or your_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("Your choice:")
    print(rock if your_choice == 0 else paper if your_choice == 1 else scissors)
    computer_choice = random.randint(0, 2)
    print("Computer choice:")
    print(rock if computer_choice == 0 else paper if computer_choice == 1 else scissors)
    print(result_map[computer_choice][your_choice])