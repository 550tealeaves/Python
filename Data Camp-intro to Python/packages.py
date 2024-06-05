# ***PACKAGES***
# Why do we use packages?
# 	• If you had to enter every function/method, then 
# 		○ Would be very large, messy code
# 		○ Lots of unused code
# 		○ Maintenance problems
# 	• Packages = directory of Python scripts
# 		○ Each script = module
# 			§ Modules specify functions, methods, and Python types
# 		○ Thousands available
# 			§ NumPy
# 				□ Arrays
# 			§ Matplotlib
# 				□ Viz
# 			§ Scikit-learn
# 				□ Machine learning
# 		○ Must be installed first
# 		○ Then put code in script telling Python that you want to use packages


# Install package
# 	• Go to http://pip.readthedocs.org/en/stable/installing
# 	• Download get-pip.py
# 	• In terminal, type python3 get-pip.py
# 		○ Can now install packages
# 			§ Pip3 install numpy
# 				□ Installs NumPy package

# Import package
# 	• Must import the package or a specific module
# 		○ Import numpy
# 			§ Imports entire NumPy package
# 				□ Handles lists as arrays
# 			§ Have to call the package when doing calculations
# 				□ Numpy.array([1,2,3])
# 			§ Can import the package as variable so you don't have to write numpy each time
# 				□ Import numpy as np
# 					® Np.array([1,2,3])
# 			§ Can also rephase the import statement so you don't need a prefix before array
# 				□ From numpy import array
# 					® Array([1,2,3})
# 						◊ Doesn't need numpy prefix
# 						◊ CON - only imports a certain portion of the package


# EXERCISES
# Import the math package - need it to calculate pi
import math 

# Definition of radius
r = 0.43

# Calculate C - use math.pi
C = 2*math.pi*r

# Calculate A
A = math.pi*r**2

# Build printout
print("Circumference: " + str(C)) # Circumference: 2.701769682087222
print("Area: " + str(A)) # Area: 0.5808804816487527



#SELECTIVE IMPORT
# Import radians function of math package
from math import radians

# Definition of radius
r = 192500

# Travel distance of Moon over 12 degrees. Store in dist.
# B/c selective import, don't need the prefix - didn't need math.radians
dist = r * radians(12)

# Print out dist
print(dist) # 40317.10572106901


# Different ways to import packages
# Wants to import the inv() function from the linalg subset of package, scipy & store it as my_inv
from scipy.linalg import inv as my_inv



# ****NUMPY******
# 	• Numeric Python
# 	• Alternative to Python List: NumPy Array
# 	• Does calculations over entire arrays
# 	• Quick/easy install
# 		○ Must use pip3 install numpy in the terminal
# 			§ Numpy doesn't work for me in VS Code
# 	• Knows how to work with arrays like they were single values
# 	• Assumptions
# 		○ Assumes Numpy arrays have only 1 type
# 			§ So if you mix data types, it will convert them into a single type


# 	• W/o numpy array, adding lists just results in concatenation of the values (just put them next to each other)
# 	• Using numpy_array - then it will add the values of each list


# Numpy Subsetting
# 	• Can use array of booleans to get index values
# 	• Ex: want to see what values are greater than/ less than a specific value
# 		○ Bmi > 23
# 			§ Array([False, False, False, True, False])
# 				□ Uses an Array of booleans 
# 	• Now use the boolean to perform subsetting
# 		○ Bmi[bmi>23]
# 			§ Array ([24.7473475])



# Import the numpy package as np - this doesn't work on VS code
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball)) #class 'numpy.ndarray'




# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in) # [74 74 72 ... 75 75 73]

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m) # [1.8796 1.8796 1.8288 ... 1.905  1.905  1.8542]






# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592


# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m**2

# Print out bmi
print(bmi) # [23.11037639 27.60406069 28.48080465 ... 25.62295933 23.74810865
# 25.72686361]





# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light) #[False False False ... False False False]

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light]) #[20.54255679 20.54255679 20.69282047 20.69282047 20.34343189 20.34343189, 20.69282047 20.15883472 19.4984471  20.69282047 20.9205219 ]


#np.array must have one data type - it will convert mixed types to a single type
np.array([True, 1, 2]) + np.array([3, 4, False]) # array([4, 5, 2])

np.array([4, 3, 0]) + np.array([0, 2, 2]) # this has the same output as the above line





# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50]) #200

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111]) #[73 74 72 73 69 72 73 75 75 73 72]



# 2D NumPy arrays
	# • Numpy.ndarray
	# 	○ Numpy. = type that was defined in the numpy package
	# 	○ Ndarray = n-dimensional array
	# 		§ Np_height & np_weight = 1D arrays
	# 		§ Can create multidimensional arrays
	# • Can create 2D NumPy arrays from list of lists
	# • All elements must be the same data type or else, it will force conversion into a homogeneous type
    #Subsetting
    # regular list of lists
    # x = [["a", "b"], ["c", "d"]]
    # [x[0][0], x[1][0]]

    # numpy
    # import numpy as np
    # np_x = np.array(x)
    # np_x[:, 0]

import numpy as np
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, 68.7]]) #can create 2D numpy arrays from list of lists

np_2d #array([[ 1.73,  1.68,  1.71,  1.89,  1.79],
    #    [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])

# this shows that array has 2 rows w/ 5 col
#shape = attribute of 2d array that provides info on what data structure looks like
np_2d.shape # (2, 5) - 2x5 table (2 rows, 5 cols)

#treat the lists like they are elements in another list - 1st list has index=0, 2nd has index=1
np_2d[0] #array([1.73, 1.68, 1.71, 1.89, 1.79])





# Import numpy
import numpy as np

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball)) #class 'numpy.ndarray'

# Print out the shape of np_baseball
print(np_baseball.shape) # (4,2) 4 rows, 2 col





# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape) #(1015, 2) - 1015 rows, 2 col



