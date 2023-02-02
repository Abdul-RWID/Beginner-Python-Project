# You're going to be learning about PRINTING, COMMENTING, STRING MANIPULATION, VARIABLES

'''
Exercise 1 - Debugging Practice
'''
#Fix the code below 👇

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

####################################
print('\n')
'''
Exercise 2 - Input Function
'''
#Write your code below this line 👇
print(len(input('What is your name? ')))

####################################
print('\n')
'''
Exercise 3 - Variables
'''
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
c = a
a = b
b = c

#Write your code above this line 👆


# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

####################################
print('\n')
'''
Day 1 Project: Band Name Generator
'''
#Go to: https://replit.com/@appbrewery/band-name-generator-start?v=1
#1. Create a greeting for your program.
name = input('What is your name ? ')
print('Hello ' + name)
print('Welcome to the Band Name Generator.')

#2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew up in ?\n")

#3. Ask the user for the name of a pet.
pet = input("What's your pet's name ?\n")

#4. Combine the name of their city and pet and show them their band name.
print('Your band name could be ' + city + ' ' + pet)

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end