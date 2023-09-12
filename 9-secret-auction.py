# You're going to be learning about Dictionaries, Nesting & Secret Aution Program
from turtle import clear

def exe0():
    '''
    Exercise 0 - Introduction Dictionary
    '''
    programming_dictionary = {
        'Bug' : 'An error in a program that prevents the program from running as expected.',
        'Function' : 'A piece of code that you can easily call over and over again.',
    }

    # Retrieving items from dictionary.
    # print(programming_dictionary['Function'])

    # adding new items to dictionary.
    programming_dictionary['Loop'] = 'The action of doing something over and over again.'
    print(programming_dictionary)

    # Create an empty dictionary
    empty_dictionary = {}
    print(empty_dictionary)

    # Wipe an existing empty_dictionary
    # programming_dictionary = {}
    # print(programming_dictionary)

    # Edit an item in a dictionary
    programming_dictionary['Bug'] = 'A moth in your computer.'
    print(programming_dictionary)
    print('\n')

    # Loop through a dictionary
    for thing in programming_dictionary:
        print(thing)

    for key in programming_dictionary:
        print(key)
        print(programming_dictionary[key])

def exe1():
    '''
    Exercise 1 - Grading Program
    '''
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }
    # 🚨 Don't change the code above 👆

    # TODO-1: Create an empty dictionary called student_grades.
    student_grades = {}

    # TODO-2: Write your code below to add the grades to student_grades.👇
    for student in student_scores:
        score = student_scores[student]
        if score > 90:
            student_grades[student] = 'Outstanding'
        elif score > 80:
            student_grades[student] = 'Exceeds Expectations'
        elif score > 70:
            student_grades[student] = 'Acceptable'
        else:
            student_grades[student] = 'Fail'

    # 🚨 Don't change the code below 👇
    print(student_grades)

# Below is about Nesting  ( Please Read this )#
'''
#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
'''

def exe2():
    '''
    Exercise 2 : Dictionary in List
    '''
    travel_log = [
        {
            "country": "France",
            "visits": 12,
            "cities": ["Paris", "Lille", "Dijon"]
        },
        {
            "country": "Germany",
            "visits": 5,
            "cities": ["Berlin", "Hamburg", "Stuttgart"]
        },
    ]

    # DO NOT change the code above 👆

    # TODO: Write the function that will allow new countries
    # to be added to the travel_log.
    def add_new_country(name, visit_count, cities_visited):
        new_country = {}
        new_country["country"] = name
        new_country["visits"] = visit_count
        new_country["cities"] = cities_visited
        travel_log.append(new_country)

    # Do not change the code below 👇
    add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
    print(travel_log)

def secret_auction():
    '''
    Final Project day 9 : Secret Auction
    '''

    # from replit import clear
    from art import logo_secret_auction
    print(logo_secret_auction)

    bids = {}
    bidding_finished = False

    def find_highest_bidder(bidding_record):
        highest_bid = 0
        winner = ""
        # bidding_record = {"Angela": 123, "James": 321}
        for bidder in bidding_record:
            bid_amount = bidding_record[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")

    while not bidding_finished:
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        bids[name] = price
        should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
        if should_continue == "no":
            bidding_finished = True
            find_highest_bidder(bids)
        # elif should_continue == "yes":
        #     clear()

        # FAQ: My console doesn't clear()
        # This will happen if you’re using an IDE other than replit.
        # I’ll cover how to use PyCharm in Day 15. That said, you can write your own clear() function or configure your IDE like so:


secret_auction()