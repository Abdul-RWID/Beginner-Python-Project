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

'''
Exercise 3 - Treasure Map
'''


