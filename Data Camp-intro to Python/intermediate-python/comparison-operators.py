	# • Comparison operators 
	# 	○ Tell how values relate
	# 	○ Result in boolean
	# • Always make sure to make comparisons of objects of the same type
    # · Can compare an array with a numeric value or string and see Python will compare that numeric value against each element in the array and return a boolean if the types are the same


## EXERCISE 1
# Comparison of booleans
True == False

# Comparison of integers
-5*15 != 75

# Comparison of strings
"pyscript" == "PyScript"

# Compare a boolean with an integer
True == 1





## EXERCISE 2
# Comparison of integers
x = -3 * 6
x >= -10


# Comparison of strings
y = "test"

"test" <= y

# Comparison of booleans
True > False




## EXERCISE 3 - COMPARE ARRAYS
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)


