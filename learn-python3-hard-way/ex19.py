## FUNCTIONS AND VARIABLES ##
# Variables in function are not connected to the variables in the script

# Define the function (cheese_and_crackers) and its 2 arguments - cheese_count & boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f'You have {cheese_count} cheeses!')
  print(f'You have {boxes_of_crackers} boxes of crackers!')
  print("Man, that's enough for a party!")
  print("Get a blanket.\n") # will print this on a new line

# 4 ways to pass values into function cheese_and_crackers

# (1) pass in numbers
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30) # pass 20,30 into the place of cheese_count & boxes_of_crackers

# (2) pass in variables
print("OR, we may utilize the variables from the script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # pass these 2 variables (10 & 50) as arguments into cheese_and_crackers function

# (3) pass in math equation
print("we can even do math inside too:")
cheese_and_crackers(10 - 27, 5 + 6) # can pass the arguments as 2 separate math equation

# (4) pass in combo of math and variables
print('Additionally, we can combine the two, variables and math:')
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)