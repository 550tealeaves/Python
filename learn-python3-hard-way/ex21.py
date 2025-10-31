## FUNCTIONS RETURN SOMETHING
# return sets variables to be a value from the function

# Function called w/ 2 arguemnts: a&b

#Addititive function
def add(a, b):
  print(f"Adding {a} + {b}")
  return a + b

#Subtractive function
def subtract(a, b):
  print(f"Subtracting {a} - {b}")
  return a - b

#Multiplicative function
def multiply(a, b):
  print(f"Multiplying {a} * {b}")
  return a * b

#Dividing function
def divide(a, b):
  print(f"Dividing {a} / {b}")
  return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f'Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}')

# Extra credit puzzle
print("And now a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")