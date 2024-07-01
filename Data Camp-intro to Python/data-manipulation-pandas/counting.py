# Unique values
# 	• Drop duplicate names
# 		○ .drop_duplicates() method
# 			§ Takes an argument "subset" which is the col that you want to find unique values
# 		○ Below example drops all duplicates from the name column (remove duplicate dog names)
# 			§ Extracts a dog w/ each name 1x
#             Can pass list of col names to extract unique values from
# Counting
# 	• .value_counts() method
# 	• Can also use sort argument to sort descending/ascending
# 	• Normalize argument - used to convert totals into proportions


##EXERCISE 1 - DROP DUPLICATES
import pandas as pd
sales = pd.read_pickle("/usr/local/share/datasets/sales_subset.pkl.bz2")
# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset="date")

# Print date col of holiday_dates
print(holiday_dates["date"])

#       store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
# 0         1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
# 901       2    A           1 2010-02-05      35034.06       False          4.550                 0.679         8.324
# 1798      4    A           1 2010-02-05      38724.42       False          6.533                 0.686         8.623
# 2699      6    A           1 2010-02-05      25619.00       False          4.683                 0.679         7.259
# 3593     10    B           1 2010-02-05      40212.84       False         12.411                 0.782         9.765
#     store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
# 0       1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
# 12      1    A           2 2010-02-05      50605.27       False          5.728                 0.679         8.106
# 24      1    A           3 2010-02-05      13740.12       False          5.728                 0.679         8.106
# 36      1    A           4 2010-02-05      39954.04       False          5.728                 0.679         8.106
# 48      1    A           5 2010-02-05      32229.38       False          5.728                 0.679         8.106
# 498    2010-09-10
# 691    2011-11-25
# 2315   2010-02-12
# 6735   2012-09-07
# 6810   2010-12-31
# 6815   2012-02-10
# 6820   2011-09-09
# Name: date, dtype: datetime64[ns]



#EXERCISE 2 - COUNTING CAT VARS
# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

# print(dept_props_sorted)
# A    11
# B     1
# Name: type, dtype: int64
# A    0.917
# B    0.083
# Name: type, dtype: float64
# 1     12
# 55    12
# 72    12
# 71    12
# 67    12
#       ..
# 37    10
# 48     8
# 50     6
# 39     4
# 43     2
# Name: department, Length: 80, dtype: int64
# 1     0.013
# 55    0.013
# 72    0.013
# 71    0.013
# 67    0.013
#       ...  
# 37    0.011
# 48    0.009
# 50    0.006
# 39    0.004
# 43    0.002
# Name: department, Length: 80, dtype: float64