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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Make a rock, paper, scissors game.

# Start the game by asking the player:

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:

# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.

#Write your code below this line 👇
# check that user entered a valid entry
acceptableEntry = 0
# "choiceOptions" is the potential options
choiceOptions = [0, 1, 2]
# "choice" is the user's choice
while acceptableEntry < 1:
    try:
        choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    except ValueError:
        print("Not a valid entry, please try again.")
        continue
    if choice in choiceOptions:
        acceptableEntry = 1
    else:
        print("Not a valid entry, please try again.")

# "compChoice" is the random computer choice
compChoice = choiceOptions[random.randint(0, len(choiceOptions) - 1)]
# "choices" are the potential choices
choices = [rock, paper, scissors]
# "winLose" is whether the user wins or loses, starts as a loss (0)
winLose = 0

if choice == 0:
    if compChoice == 2:
        winLose = 1
if choice == 1:
    if compChoice == 0:
        winLose = 1
if choice == 2:
    if compChoice == 1:
        winLose = 1
if choice == compChoice:
    print("Your choice:" + choices[choice] + "Computer choice:" + choices[compChoice])
    print("Draw.")
else:

    print(choices[choice] if winLose else choices[compChoice])

    print("Beats ")

    print(choices[choice] if not winLose else choices[compChoice])

    print("You win!" if winLose else "You Lose!")