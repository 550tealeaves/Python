# 	• 3 most common are
# 		○ And
# 		○ Or
# 		○ Not


# And
# 	• Takes 2 booleans and returns True if they are both True
# 	• True + True = True
# 	• T + F = False
# 	• F and F = False
# 	• T and F = False
# 	• Can also use comparison results
# 		○ x=5
# 		○ y=3
# 		○ X = Y  - False
# 		○ X > 6 = False
# 		○ X <= 15 - True

# Or
# 	• Only 1 of booleans needs to be True

# Not
# 	• Negates boolean value used
# 	• Not False = True
# 	• Not True = False

# NumPy arrays
# 	• Truth value of an array w/ >1 element is ambiguous
# 	• You must use the NumPy equivalent of boolean operators
# 		○ Logical_and()
# 		○ Logical_or()
# 		○ Logical_not()

# 	• To determine which BMIs are between 21 and 22
# 		○ Np.logical_and(bmi > 21, bmi < 22)
# 		○ And operation is performed element wise
# 			§ Compares the elements and says which is True/False
# 	• To see the values of BMIs that are b/w 21 and 22
# 		○ Use square brackets
# 		○ Bmi[np.logical_and(bmi > 21, bmi < 22)]


## EXAMPLE - BMI
True and True #True
False and True #False
True and False #False  
False and False #False

True or True #True
False or True #True
True or False #True
False or False #False
y = 5 
y < 7 or y > 13 # True

not True #False
not False #True

import numpy as np

bmi = np.array([22.5, 19.6, 21.2, 35.1, 20.7, 21.8])

#What BMIs are b/w 21 and 22
np.logical_and(bmi > 21, bmi < 22)

bmi[np.logical_and(bmi > 21, bmi < 22)]





## EXERCISE 1 - AND, OR, NOT
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen*2 < your_kitchen*3)



## EXERCISE 2 - NOT
x = 8
y = 9
not(not(x < 3) and not(y > 14 or y > 10)) # False




## EXERCISE - BOOLEAN OPERATORS
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11 ))