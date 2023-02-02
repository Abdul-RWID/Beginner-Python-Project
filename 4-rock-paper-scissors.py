# You're going to be learning about Randomisation and Python Lists

'''
Exercise 1 - Heads or Tails
'''
import random

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
elif random_side == 0:
  print("Tails")

####################################
print('\n')
'''
Exercise 2 - Banker Roulette
'''
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

#Write your code below this line 👇

#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)    #-1 because list start at 0
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

####################################
print('\n')
'''
Exercise 3 - Treasure Map
'''
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
pos_column = int(position[0])
pos_row = int(position[1])

selected_row = map[pos_row - 1]
selected_row[pos_column - 1] = 'X'
# DISEDERHANAKAN >> map[pos_row - 1][pos_column - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

####################################
print('\n')
'''
Day 4 Project: Rock Paper Scissors
'''
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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice < 0 or user_choice > 2:
  print('You typed an invalid number, you lose!')

else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  if user_choice == 0:
    if computer_choice == 0:
      print('You draw')
    elif computer_choice == 1:
      print('You lose')
    elif computer_choice == 2:
      print('You win')

  if user_choice == 1:
    if computer_choice == 0:
      print('You win')
    elif computer_choice == 1:
      print('You draw')
    elif computer_choice == 2:
      print('You lose')

  if user_choice == 2:
    if computer_choice == 0:
      print('You lose')
    elif computer_choice == 1:
      print('You win')
    elif computer_choice == 2:
      print('You lose')

  #alternatif solution
  '''
  if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")
  '''