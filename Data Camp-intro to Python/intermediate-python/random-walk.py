	# • After setting seed
	# 1. Initialize empty list (outcomes)
	# 2. Create for loop that runs 10x
	# 	○ Use range function that generates list of iterable #s
	# 3. Inside for loop, generate random integer (coin) that either outputs 0 or 1
	# 4. If value is 0, then it appends string "head" to the list
	# 	○ If value is 1, then it appends string "tails" to list
	# 		§ Uses append method for both
	# 5. Print out the list

import numpy as np 
np.random.seed(123) # set seed
outcomes = [] # initialize empty list
for x in range(10): #create loop that runs 10x & use range function to generate list of iterable #s
    coin = np.random.randint(0, 2) #generate rand int that either is 0/1
    #create if/else statement that appends string based on coin result
    if coin == 0: 
        outcomes.append("heads") #appends "heads" to list
    else:
        outcomes.append("tails") #appends "strings" to list
print(outcomes)

#['heads', 'tails', 'heads', 'heads', 'heads', 'heads', 'heads', 'tails', 'tails', 'heads']

#NOT A RANDOM WALK B/C LIST ITEMS AREN'T BASED ON THE PREVIOUS ITEMS


# Heads/Tails - RANDOM WALK

# 	1. Create list that already has value 0
# 	2. Create for loop that runs 10x w/ range function
# 	3. Generate random integer (coin)
# 	4. Instead of if/else, create statement that if it's a 0 (heads) - then # of tails stays the same
# 		a. But if it's a 1 (tails) then # tails increments by 1
# 		b. Just add the variable coin (for tails) & append the values to the tails list
# 	5. Print

# 	• List prints out 11 elements, the last element tells you how many times tails was thrown 


np.random.seed(123)
tails = [0] #Create list (tails) w/ value 0 - so 0 tails thrown
for x in range(10): #Create for loop that runs 10x w/ range function
    coin = np.random.randint(0,2) #Generate random integer 0/1
    tails.append(tails[x] + coin) #create statement that if it's a 0 (heads) - then # of tails stays the same. But if it's a 1 (tails) then # tails increments by 1
print(tails)
#[0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3]  #last item (11th) = # of times tails thrown



##EXERCISE 1 - NEXT STEP
# NumPy is imported, seed is set

# Initialize random_walk
random_walk=[0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# [0, 3, 4, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, -1, 0, 5, 4, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 7, 8, 9, 10, 11, 10, 14, 15, 14, 15, 14, 15, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 32, 33, 37, 38, 37, 38, 39, 38, 39, 40, 42, 43, 44, 43, 42, 43, 44, 43, 42, 43, 44, 46, 45, 44, 45, 44, 45, 46, 47, 49, 48, 49, 50, 51, 52, 53, 52, 51, 52, 51, 52, 53, 52, 55, 56, 57, 58, 57, 58, 59]  






## EXERCISE 2 - HOW LOW CAN YOU GO?
#A typical way to solve problems like this is by using max(). If you pass max() two arguments, the biggest one gets returned. For example, to make sure that a variable x never goes below 10 when you decrease it, you can use:

#y = max(10, y - 1)

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1) #used max to ensure step is never < 0
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)
#[0, 4, 3, 2, 4, 3, 4, 6, 7, 8, 13, 12, 13, 14, 15, 16, 17, 16, 21, 22, 23, 24, 23, 22, 21, 20, 19, 20, 21, 22, 28, 27, 26, 25, 26, 27, 28, 27, 28, 29, 28, 33, 34, 33, 32, 31, 30, 31, 30, 29, 31, 32, 35, 36, 38, 39, 40, 41, 40, 39, 40, 41, 42, 43, 42, 43, 44, 45, 48, 49, 50, 49, 50, 49, 50, 51, 52, 56, 55, 54, 55, 56, 57, 56, 57, 56, 57, 59, 64, 63, 64, 65, 66, 67, 68, 69, 68, 69, 70, 71, 73]






##EXERCISE 3 - VISUALIZE WALK
# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()