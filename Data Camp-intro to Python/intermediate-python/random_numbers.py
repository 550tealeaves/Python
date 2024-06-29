	# • Goal is to win this dice game
	# • Have to simulate the process many times
	# 	○ Hacker statistics

	# • Steps
	# 	○ Need random generators to simulate dice
	# 		§ Use the random package inside numpy
	# 		§ .rand() function - generates random # from 0-1
	# 			□ How? .rand() calls # from a seed that Python used
	# 			□ Seed can be manually set
	# 				® Np.random.seed(123) #starts from seed 123
	# 				® Np.random.rand()

#basic .rand()
import numpy as np
np.random.rand() #generates random # b/w 0 & 1


#Setting the "c" for random # generation
#will get the same #s each time if you set the seed
np.random.seed(123)
np.random.rand()


#COIN TOSS - SIMULATE PROBABILITY
np.random.seed(123)
coin = np.random.randint(0,2) #randomly generate 0 OR 1
print(coin)


#Add if/else statement so something else results from # generated
np.random.seed(123)
coin = np.random.randint(0,2) #randomly generate 0 OR 1
print(coin)
if coin == 0:
    print("heads")
else:
    print("tails")




##EXERCISE 1 - RANDOM FLOAT
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())


##EXERCISE 2 - ROLL DICE
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
dice1 = np.random.randint(1, 7) #prints any integer from 1-7
print(dice1)

# Use randint() again to simulate a second throw
dice2 = np.random.randint(1, 7)
print(dice2)


## EXERCISE 3 - NEXT MOVES
import numpy as np
np.random.seed(123)
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)  # Make sure the range is 1 to 6 inclusive

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :  # Complete the elif statement
    step = step + 1
else :  # Complete the else statement
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)