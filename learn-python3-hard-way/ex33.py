# EX 33 - WHILE LOOP
# While loop keeps executing code block as long as Boolean is True
# Ending line with : means Python starts new code block
# While loop jumps to the top and repeats and runs until expression is False

# PROBLEM - sometimes won't stop and will crash system
## How to avoid issue
# (1) Use it rarely
# (2) Make sure Boolean will become False
# (3) If unsure, print out test variable at top/bottom of while loop to know what it's doing

i = 0
numbers = [] #empty list

while i < 6:
  print(f"At the top i is {i}") # new code block after ":"
  numbers.append(i) # numbers add to list 0 -5 (stops before 6)

  i = i + 1
  print("Numbers now: ", numbers) #numbers 0-5 b/c appended to <6
  print(f" At the bottom i is {i}") # i is 1-6 (b/c i+1)

print("The numbers: ")

for num in numbers:
  print(num) #Just prints the numbers 0-5 b/c numbers runs up to <6