# 	• Most data will be in tabular structure
# 	• Every row is observation or measurement (temp)
# 		○ For each observation, there are diff variables
# 			§ Date/time
# 			§ Location
# 	• Need a rectangular data structure
# 		○ 2D NumPy array is not great at handling mixed data types
# 		○ Pandas package - data manipulation tool built on NumPy package that can handle mixed data types
# 			§ Store the tabular data in an object called the dataframe
# 			§ Each row has unique row label 
# 	• How to build a Dataframe from Dictionary?
# 		○ Create key value pairs and store in dictionary
# 			§ Keys = column labels
# Values = data (col by col)
# Make sure to note the index if the data has a first column


## EXERCISE 1 - DICTIONARY TO DATAFRAME
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd 

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    "country":names,
    "drives_right": dr,
    "cars_per_cap": cpc
}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)



## EXERCISE 2
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars


# Print cars again
print(cars)





#EXERCISE 2
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(row_labels)
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']


# Specify row labels of cars
car.index = row_labels

# Print cars again
print(cars)





import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)


# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']


# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)




## EXERCISE 3 - CSV TO DATAFRAME
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)



##EXERCISE 4 - CSV TO DATAFRAME PART 2
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)


# Print out cars
print(cars)