# You're going to be learning about PRINTING, COMMENTING, STRING MANIPULATION, VARIABLES

def intro():
    print('Day 1 : You\'re going to be learning about PRINTING, COMMENTING, STRING MANIPULATION, VARIABLES')
    print('Type "1" for Exercise 1 - Debugging Practice')
    print('Type "2" for Exercise 2 - Input Function')
    print('Type "3" for Exercise 3 - Variables')
    print('Type "4" for Day 1 Project: Band Name Generator')

def exe1():
    '''
    Exercise 1 - Debugging Practice
    '''
    #Fix the code below 👇

    print("Day 1 - String Manipulation")
    print('String Concatenation is done with the "+" sign.')
    print('e.g. print("Hello " + "world")')
    print("New lines can be created with a backslash and n.")

def exe2():
    '''
    Exercise 2 - Input Function
    '''
    #Write your code below this line 👇
    print(len(input('What is your name? ')))

def exe3():
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

def day1():
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

def program():
    if choice == 1:
        exe1()
    elif choice == 2:
        exe2()
    elif choice == 3:
        exe3()
    elif choice == 4:
        day1()
    else:
        print('You not type the selected choice, please "RUN" again.')

####################################

####################################
intro()
# choice = int(input('What is your choice ? \n'))
# program()

should_end = False
while not should_end:
  choice = int(input('What is your choice ? ("1", "2", "3", "4")\n'))
  program()

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")