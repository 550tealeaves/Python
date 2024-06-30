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
import numpy as np 
for val in np.nditer(meas):
    print(val)




##PART 2
import pandas as pd 
brics = pd.read_csv("Data Camp-intro to Python/intermediate-python/brics.csv", index_col=0)
for value in brics:
    print(value)


# 	• This produces the col names, not the values
# 	• Pandas requires that you explicitly state that you want to iterate over the rows
# 		○ Use iterrows method
# 			§ Generates 2 pieces of data as a panda series
# 				□ Row label
                # Data in row



brics = pd.read_csv("Data Camp-intro to Python/intermediate-python/brics.csv", index_col=0)
for lab, row in brics.iterrows():
    print(lab)
    print(row)


	# • 1st iteration
	# 	○ Label = BR
	# 	○ Row = the panda series 
	# • Since row variable on each iteration is a series, you can access more info by using subsetting techniques 


import pandas as pd 
brics = pd.read_csv("Data Camp-intro to Python/intermediate-python/brics.csv", index_col=0)
for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])

##prints out the row label (country initials) & country capital






##	• Goal: Want to add a new col to the dataframe, called name length (# characters in countries' name)
		# ○ Create series via iteration
		# 	§ Need both row label & data
		# 	§ Select each country col from row & pass it to len function (determines # characters of string)
		# 	§ Pass the # of characters to a new column, named "name_length"
		# 		□ Used .loc

## ADDING COLUMNS - CREATE NEW COL, CALLED NAME_LENGTH, THAT HAS # OF CHARACTERS OF COUNTRY NAME
import pandas as pd 
brics = pd.read_csv("Data Camp-intro to Python/intermediate-python/brics.csv", index_col=0)
for lab, row in brics.iterrows():
    #creating series for each iteration
    brics.loc[lab, "name_length"] = len(row["country"])
    print(brics)

	# • Problem is that it creates a series object on each iteration = inefficient


#BETTER WAY IS TO USE APPLY
	# 	○ DOESN'T NEED A FOR LOOP
	# • Select the country col from the brics dataframe  & then apply the len functions to that col
	# 	○ Apply pulls len function w/ each country name as input
	# 	○ Creates new array that can be stored as new col 

import pandas as pd 
brics = pd.read_csv("Data Camp-intro to Python/intermediate-python/brics.csv", index_col=0)
brics["name_length"] = brics["country"].apply(len)
print(brics)





## EXERCISE 1 - LOOP OVER DATAFRAME
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)



## EXERCISE 2 - LOOP OVER DF CONTINUED
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))
#US: 809
# AUS: 731
# JPN: 588
# IN: 18
# RU: 200
# MOR: 70
# EG: 45



## EXERCISE 3 - ADD COLUMN - FOR LOOP 
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = (row["country"].upper())


# Print cars
print(cars)

# #     cars_per_cap        country  drives_right        COUNTRY
# US            809  United States          True  UNITED STATES
# AUS           731      Australia         False      AUSTRALIA
# JPN           588          Japan         False          JAPAN
# IN             18          India         False          INDIA
# RU            200         Russia          True         RUSSIA
# MOR            70        Morocco          True        MOROCCO
# EG             45          Egypt          True          EGYPT




## EXERCISE 4 - ADD COLUMN - APPLY() - SAME RESULTS AS EXERCISE 3
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)


# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)
# #     cars_per_cap        country  drives_right        COUNTRY
# US            809  United States          True  UNITED STATES
# AUS           731      Australia         False      AUSTRALIA
# JPN           588          Japan         False          JAPAN
# IN             18          India         False          INDIA
# RU            200         Russia          True         RUSSIA
# MOR            70        Morocco          True        MOROCCO
# EG             45          Egypt          True          EGYPT