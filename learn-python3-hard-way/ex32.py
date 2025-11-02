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

for fruit in fruits: #fruits = list
  print(f"A fruit of type: {fruit}")

# **MIXED LISTS**
# Use empty brackets {} b/c you don't know what's in it
for i in change: #change = list
  print(f"I got {i}")

# BUILD LISTS - start w/ empty one []
elements = []

# Then use range function to do 0 to 5 counts
for i in range(0, 6):
  print(f"Adding {i} to the list.")
  # append = function that adds item to list
  elements.append(i)

# Print out new list
for i in elements:
  print(f"Element was: {i}")
