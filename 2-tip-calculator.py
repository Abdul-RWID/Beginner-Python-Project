# You're going to be learning about DATA TYPES, NUMBERS, TYPE CONVERSION, F-STRINGS

'''
Exercise 1 - Data Types
'''

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Check the data type of two_digit_number
# print(type(two_digit_number))

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits together
result = first_digit + second_digit

print(two_digit_number[0] + ' + ' + two_digit_number[1] + ' = ' + str(result))
print(str(first_digit) + ' + ' + str(second_digit) + ' = ' + str(result))
print('{0} + {1} = {2}'.format(str(first_digit), str(second_digit), str(result)))
print(f'{str(first_digit)} + {str(second_digit)} = {str(result)}')
print(result)
print(type(result))

####################################

'''
Exercise 2 - BMI Calculator
'''
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
print(int(bmi))
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)
print(int(bmi))
# or direct with value
bmi =int(weight) / float(height) ** 2

bmi_as_int = int(bmi)

print('{0} / {1} ** 2 = {2}'.format(str(weight), str(height), str(bmi_as_int)))
print(bmi_as_int)

####################################

'''
Exercise 3 - Life in Weeks
'''
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
die = input('What is your approximate age die ? ')
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# if you die at 90 years old
years = int(die) - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

message = f"You have {days} days, {weeks} weeks, {months} months, and {years} years left."
print(message)

####################################

'''
Day 2 Project: Tip Calculator
'''
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
print(f'\ntip_as_percent = tip / 100 = {tip_as_percent}')
total_tip_amount = bill * tip_as_percent
print(f'total_tip_amount = bill * tip_as_percent = {total_tip_amount}')
total_bill = bill + total_tip_amount
print(f'total_bill = bill + total_tip_amount = {total_bill}')

bill_per_person = total_bill / people
print(f'\nbill_per_person = total_bill / people = {bill_per_person}')
final_amount = round(bill_per_person, 2)
print(f'final_amount = round(bill_per_person, 2) = {final_amount}')
final_amount = '{:.2f}'.format(bill_per_person)
# print(f"final_amount = '\{:.2f\}'.format(bill_per_person)")
print(f'final_amount = round(bill_per_person, 2) = {final_amount}')


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")

