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
