import random

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
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_images = [rock, paper, scissor]
user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choise >= 3 or user_choise < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choise])
    computer_choise = random.randint(0, 2)
    print(f"Computer Choose:")
    print(game_images[computer_choise])


    if user_choise == 0 and computer_choise == 2:
        print("You Win!")
    elif user_choise == 2 and computer_choise == 0:
        print("You Lose!")
    elif computer_choise > user_choise:
        print("You Lose!")
    elif computer_choise == user_choise:
        print("It's a draw!")