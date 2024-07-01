# 	• Does one color of dog weigh more than another?
# 	• Female dogs taller than males?

# Steps
# 	• Subset dogs into groups based on color
# 	• Take mean of each
# 		○ Be careful b/c duplicated code can introduce error
# 	• Use groupby() method
# 		1. Group by color variable
# 		2. Select weight column
# 		3. Calculate the mean
# 			i. This provides mean weight for each dog color 

# Multiple grouped summaries 
# 	• Use agg method to get multiple stats
# 		○ Pass list of functions into .agg() after grouping by color
# 		○ Results show min, max, & sum of diff colored dogs' weights

# Groupby multiple columns 
# 	• Ex
# 		1. Group by color & breed
# 		2. Select weight col
# 		3. Calculate the mean 
# Result gives the mean of each breed of each color
# 	• Can group by & aggregate by multiple cols


##EXERCISE 1 - % SALES AT EACH STORE TYPE
# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type) #[0.9097747 0.0902253 0.       ]


#EX 2 - GROUPBY CALC
# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)

# type
# A    0.91
# B    0.09
# Name: weekly_sales, dtype: float64



# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)

# type  is_holiday
# A     False         2.337e+08
#       True          2.360e+04
# B     False         2.318e+07
#       True          1.621e+03
# Name: weekly_sales, dtype: float64


##EX 3 - MULT GROUPED SUMMARIES
import pandas as pd
sales = pd.read_pickle("/usr/local/share/datasets/sales_subset.pkl.bz2")
# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)


#         amin       amax       mean    median
# type                                        
# A    -1098.0  293966.05  23674.667  11943.92
# B     -798.0  232558.51  25696.678  13336.08
#      unemployment                      fuel_price_usd_per_l                     
#              amin   amax   mean median                 amin   amax   mean median
# type                                                                            
# A           3.879  8.992  7.973  8.067                0.664  1.107  0.745  0.735
# B           7.170  9.765  9.279  9.199                0.760  1.108  0.806  0.803