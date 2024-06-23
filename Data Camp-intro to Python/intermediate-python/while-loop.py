	# • If condition is true, python executes the code only 1 time
	# • While loop 
	# 	○ Executes code inside if condition is true
	# 	○ Will continue to execute the code repeatedly 
	# • Similar syntax as if statement
	# • When to use it
	# 	○ Numerically calculating model
	# 	○ Repeating action until condition is met
	# • If there is a condition that evaluates to False, then the while loop stops running


	# • When the while loop keeps running, it disconnects the session
	# • Interrupt the loop with Ctrl + C


error = 50.0
while error > 1:
    error = error / 4
    print(error) #0.78125


#This while loop will keep going and disconnect the session
error = 50.0
while error > 1:
    (error)



##EXERCISE 1 - WARM UP - HOW MANY PRINTOUTS
x = 1
while x < 4 :
    print(x)
    x = x + 1 #3




##EXERCISE 2 - BASIC WHILE LOOP
# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)



#EXERCISE 3 - ADD CONDITIONALS
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1,
    else : 
      offset = offset + 1    
    print(offset)