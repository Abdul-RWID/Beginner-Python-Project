# You're going to be learning about CONDITIONAL STATEMENTS (if else, else if), LOGICAL OPERATORS
# CODE BLOCKS, SCOPE

'''
Exercise 1 - Odd or Even
'''
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
  print("This is an even number.")
#Otherwise (number cannot be divided by 2 with 0 remainder).
else:
  print("This is an odd number.")

####################################

'''
Exercise 2 - BMI 2.0
'''
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

####################################

'''
Exercise 3 - Leap Year
'''
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Refer to the flow chart here: https://bit.ly/36BjS2D

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

####################################

'''
Exercise 4 - Pizza Order Practice
'''
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bill = 0

if size == "S":
  bill += 15
  print(f'Small pizza price is ${bill}.')
elif size == "M":
  bill += 20
  print(f'Medium pizza price is ${bill}.')
else:
  bill += 25
  print(f'Large pizza price is ${bill}.')
bill_pizza = bill

if add_pepperoni == "Y":
  if size == "S":
    bill_pepperoni = 2
    bill += 2
    print('Adding pepperoni price is $2.')
  else:
    bill_pepperoni = 3
    bill += 3
    print('Adding pepperoni price is $3.')
else:
  bill_pepperoni = 0

if extra_cheese == "Y":
  bill_cheese = 1
  bill += 1
  print('Extra cheese price is $1.')
else:
  bill_cheese = 0

print(f"Your final bill is: ${bill}.")
print(f'Final bill is: ${bill_pizza} + ${bill_pepperoni} + ${bill_cheese} = ${bill}')

####################################

####################################

'''
Exercise 5 - Love Calculator
'''
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

####################################

'''
Day 3 Project: Treasure Island
'''
# ASCII Art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake.\nThere is an island in the middle of the lake.\n'
                  'Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed.\nThere is a house with 3 doors.\n"
                    "One red, one yellow and one blue.\nWhich colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")

####################################

'''
Day 3 Project: Treasure Island (by MINE)
'''
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

stage_1 = (input('Where are you going ("left" or "right")? ')).lower()
if stage_1 == 'right':
  print('You falling into a hole, GAME OVER !!!')
elif stage_1 == 'left':
  print('you arrive at the beach.\n')

  print('Select "wait" if you want to board the ship.')
  print('Select "swim" if you want to swim to the nearest island.')
  stage_2 = (input('What do you want to do ("wait" or "swim") ? ')).lower()
  if stage_2 == 'swim':
    print('You attacking by trout, GAME OVER !!!')
  elif stage_2 == 'wait':
    print('The ship has arrived at the nearest island.')
    print('There are 3 entrances on the island.')
    print('There are blue, red and yellow doors.\n')

    stage_3 = (input('Which door do you choose (blue, red, yellow) ? ')).lower()
    if stage_3 == 'blue':
      print('You eaten by beast, GAME OVER !!!')
    elif stage_3 == 'red':
      print('You burned by fire, GAME OVER !!!')
    elif stage_3 == 'yellow':
      print('You got the treasure, YOU WIN !!!')
    else:
      print('You did not choose any of the options')

  else:
    print('you did not choose any of the options')

else:
  print('You did not choose any of the options, GAME OVER !!!')