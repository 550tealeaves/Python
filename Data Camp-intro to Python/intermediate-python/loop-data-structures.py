#Dictionary - requires a METHOD to iterate
world = {
    "afghanistan": 30.55,
    "albania": 2.77,
    "algeria": 39.21
}

#Use .items() method to iterate over dictionaries
for key, value in world.items():
    print(key + "--" + str(value))


##NumPy Array - require a FUNCTION to iterate
import numpy as np 
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight/np_height **2  

for val in bmi:
    print(val) #prints each ind value


##2D NumPy Array
#2D array is built up from 1D arrays
import numpy as np 
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight]) #combines 2 areas into new variable
for val in meas: #for loop prints out the entire array on iteration - not what we want
    print(val)


#np.nditer function will print out each individual element in the arrays
#the input is the array you are iterating over (meas)
for val in np.nditer(meas):
    print(val)