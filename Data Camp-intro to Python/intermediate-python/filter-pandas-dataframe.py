# Goal
# 	• Select countries w/ areas > 8 million km2
# 	• 3 steps
# 		○ Select area column
# 			§ Want to get a panda Series, not a DataFrame - use any of the below 3 ways
# 			§ Brics["area"]
# 			§ Brics.loc[: "area"]
# 			§ Brics.iloc[:, 2]
# 		○ Do comparison on area column
# 			§ Brics["area"] > 8
# 				□ The items in the column are evaluated w/ boolean
# 			§ Can store this comparison as a variable
# 				□ Is_huge = brics["area"] > 8
# 		○ Use result to select countries
# 			§ Aka use it to subset the pandas dataframe
# 			§ Put the comparison inside square brackets
# 				□ Brics[is_huge]


# 	• Could do it all in 1 line
# 		○ Brics[brics["area"] > 8 ]



# 	• Since Pandas is built on NumPy, you can do element boolean operation on NumPy arrays


# 	• Goal
# 		○ Select observations w/ area b/w 8-10 million km2
# 	• Steps
# 		○ Import numpy as np
# 		○ Use np.logical_and() OR np.logical_or() to create a pandas series
# 			§ Np.logical_and(brics["area"] > 8, brics["area"] < 10)
# 		○ Then wrap code in square brackets to subset the brics dataset
# 			§ Brics[np.logical_and(brics["area"] > 8, brics["area" < 10)]




##EXERCISE 1 - DRIVING RIGHT
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel = cars[dr]



##EXERCISE 2 - ONE LINE OF CODE
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
# dr = cars['drives_right']
# sel = cars[dr]

sel = cars[cars['drives_right']]

# Print sel
print(sel)



##EXERCISE 3 - CARS PER CAPITA
#Which countries have a high cars per capita figure?
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
many_cars = cars["cars_per_cap"] > 500

cars_maniac = cars[many_cars]


# Print car_maniac
print(cars_maniac)



##EXERCISE 4 - CARS PER CAPITA
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between] 



# Print medium
print(medium) #'medium'





