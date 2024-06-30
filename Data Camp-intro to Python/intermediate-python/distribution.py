	# • What is the probability that you will reach 60 steps high?
	# • If you simulate walk 1000s of times, you'll end w/ different steps
	# • Once you know dist, can calculate # of chances

	# 1. Set random seed
	# 2. Create empty list (final_tails)
	# 	a. List will contain the # of tails you tally after playing the game
	# 3. Create for loop that runs 100x w/ range function
	# 4. Create list tails and set it to 0
	# 5. Create another for loop that runs 10x w/ range function
	# 6. Generate random integer (0/1)
	# 7. Append the tally of heads/tails to tails list
	# 8. Append # from step 6 to the final_tails list
	# 	a. Indentation specifies that step 7 is part of the top level for loop
	# 9. Print
	# 	a. Each # = # of tails that were thrown in game of 10 tosses
	# 10. Make sure matplotlib is imported since we want a histogram
	# 11. Plot histogram w/ 10 bins

import numpy as np 
import matplotlib.pyplot as plt
np.random.seed(123) #set seed
final_tails = [] #create empty list
for x in range(10000): #create top level loop that runs 10K times
    tails = [0] #create list tails and set to 0
    for x in range(10): #create lower level loop that runs 10x
        coin = np.random.randint(0, 2) #generate rand # 0/1
        tails.append(tails[x] + coin) #append tally of heads/tails to tails list
    final_tails.append(tails[-1]) #append tails list to final_tails list
print(final_tails)
plt.hist(final_tails, bins=10, color="forestgreen")
plt.show()





##EXERCISE 1 - SIMIULATE MULTIPLE WALKS
# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(5) :

    # Code from before
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

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)

#[[0, 1, 2, 1, 2, 3, 2, 3, 2, 3, 7, 9, 8, 7, 6, 7, 8, 9, 10, 9, 10, 11, 17, 18, 19, 20, 21, 22, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 30, 29, 30, 31, 30, 31, 30, 33, 32, 33, 34, 33, 34, 33, 37, 36, 37, 38, 39, 38, 37, 38, 37, 36, 35, 34, 33, 34, 35, 36, 37, 38, 37, 38, 39, 38, 39, 40, 41, 40, 39, 45, 44, 43, 47, 48, 49, 48, 53, 54, 53, 52, 53, 54, 55, 54, 53, 55, 56, 55, 54, 53], [0, 1, 7, 6, 5, 4, 3, 4, 3, 4, 9, 8, 9, 10, 13, 12, 13, 14, 15, 16, 17, 16, 15, 16, 15, 14, 15, 16, 15, 18, 19, 18, 17, 18, 19, 20, 21, 20, 23, 22, 21, 22, 23, 24, 25, 26, 27, 28, 27, 28, 27, 26, 27, 28, 27, 28, 31, 32, 37, 38, 37, 38, 37, 38, 37, 38, 37, 39, 40, 43, 44, 45, 44, 43, 42, 41, 40, 41, 40, 44, 43, 42, 43, 42, 43, 48, 49, 48, 51, 50, 54, 55, 57, 56, 57, 62, 67, 68, 69, 70, 71], [0, 1, 7, 11, 17, 18, 19, 24, 23, 22, 27, 26, 27, 28, 29, 30, 31, 30, 29, 35, 34, 33, 34, 33, 34, 33, 34, 33, 39, 38, 39, 40, 41, 42, 43, 46, 47, 46, 45, 46, 47, 46, 45, 49, 50, 51, 52, 51, 52, 53, 52, 53, 52, 53, 52, 51, 50, 51, 52, 53, 54, 53, 52, 51, 55, 56, 61, 62, 63, 64, 65, 69, 72, 73, 72, 73, 72, 71, 76, 77, 78, 79, 80, 84, 85, 86, 87, 86, 87, 88, 89, 90, 89, 90, 91, 92, 96, 95, 101, 100, 101], [0, 1, 2, 1, 3, 2, 1, 5, 4, 3, 4, 5, 4, 5, 6, 7, 8, 9, 10, 11, 10, 11, 13, 18, 19, 18, 19, 18, 19, 18, 19, 18, 19, 20, 19, 20, 21, 25, 24, 29, 28, 27, 28, 29, 30, 29, 30, 29, 28, 32, 31, 30, 31, 32, 38, 39, 38, 39, 40, 41, 42, 43, 42, 41, 40, 45, 46, 45, 46, 47, 48, 49, 50, 49, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 57, 62, 61, 62, 63, 66, 65, 68, 67, 73, 72, 71, 70, 71, 72, 73], [0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 0, 0, 0, 1, 5, 9, 8, 9, 8, 11, 12, 13, 12, 11, 10, 9, 10, 11, 12, 13, 14, 18, 19, 20, 23, 22, 21, 25, 26, 25, 24, 23, 24, 25, 26, 25, 26, 27, 32, 33, 37, 43, 42, 43, 42, 41, 42, 41, 42, 43, 48, 49, 52, 53, 52, 53, 54, 55, 54, 53, 56, 57, 58, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 65, 66, 65, 66, 67, 68, 69, 70, 69, 68, 69, 70, 76, 75, 74, 78, 79, 80]]





## EXERCISE 2 - VISUALIZE ALL WALKS
# Use np.array() to convert all_walks to a NumPy array, np_aw.
# Try to use plt.plot() on np_aw. Also include plt.show(). Does it work out of the box?
# Transpose np_aw by calling np.transpose() on np_aw. Call the result np_aw_t. Now every row in np_all_walks represents the position after 1 throw for the five random walks.
# Use plt.plot() to plot np_aw_t; also include a plt.show(). Does it look better this time?
# initialize and populate all_walks

import numpy as np 
import matplotlib.pyplot as plt
np.random.seed(123)


all_walks = []
for i in range(5) :
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
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()



##EXERCISE 3 - IMPLEMENT CLUMSINESS
#Have 0.5% chance of falling down. That calls for another random number generation. Basically, you can generate a random float between 0 and 1. If this value is less than or equal to 0.005, you should reset step to 0.

import numpy as np 
import matplotlib.pyplot as plt
np.random.seed(123)

# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Simulate random walk 20 times
all_walks = []
for i in range(20) :
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

        # Implement clumsiness - 0.005% chance of failure
        if np.random.rand() <= 0.005:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()


##EXERCISE 4 - PLOT DISTRIBUTION
import numpy as np 
import matplotlib.pyplot as plt
np.random.seed(123)


# Simulate random walk 500 times
all_walks = []
for i in range(500) :
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
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()


##EXERCISE 5 - CALCULATE ODDS
#The histogram of the previous exercise was created from a NumPy array ends, that contains 500 integers. Each integer represents the end point of a random walk. To calculate the chance that this end point is greater than or equal to 60, you can count the number of integers in ends that are greater than or equal to 60 and divide that number by 500, the total number of simulations.
np.mean(ends >= 60) #78.4