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
# print(f'final_amount = \'\{:.2f\}\'.format(bill_per_person)')
print(f'final_amount = round(bill_per_person, 2) = {final_amount}')


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")