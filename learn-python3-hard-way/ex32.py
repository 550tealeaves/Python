# EX 32 - Loops and List
# Use for loop to build and print different lists
# Use lists to store the results
# list = container of things,separated by comma, organized in order
## **Common to find functions w/ if-statements that have lists w/ lists (nested) - have to break it down to understand it

hairs = ['brown', 'blond', 'red']
eyes = ['hazel', 'blue', 'green']
weights = [1, 2, 3, 4]

# Lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This 1st type of for-loop goes through a list
for number in the_count: #the_count = list
  print(f"This is the count {number}")

# This is the count 1
# This is the count 2
# This is the count 3
# This is the count 4
# This is the count 5

for fruit in fruits: #fruits = list
  print(f"A fruit of type: {fruit}")

# A fruit of type: apples
# A fruit of type: oranges
# A fruit of type: pears
# A fruit of type: apricots


# **MIXED LISTS**
# Use empty brackets {} b/c you don't know what's in it
for i in change: #change = list
  print(f"I got {i}")

# I got 1
# I got pennies
# I got 2
# I got dimes
# I got 3
# I got quarters

# BUILD LISTS - start w/ empty one []
elements = []

# Then use range function to do 0 to 5 counts
for i in range(0, 6):
  print(f"Adding {i} to the list.")
  # append = function that adds item to list
  elements.append(i)

# Adding 0 to the list.
# Adding 1 to the list.
# Adding 2 to the list.
# Adding 3 to the list.
# Adding 4 to the list.
# Adding 5 to the list.

# Print out new list
for i in elements:
  print(f"Element was: {i}")

# Element was: 0
# Element was: 1
# Element was: 2
# Element was: 3
# Element was: 4
# Element was: 5