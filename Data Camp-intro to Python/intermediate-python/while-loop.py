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