	# • Summary stats tell you about dataset
	# 	○ Mean
	# 		§ Center of data
	# 		§ Select column in brackets and apply.mean()
	# 	○ Can get summary stats for date col 

	# • .agg() method 
	# 	○ Computes custom summary stats
	# 		§ Ex: compute 30th percentile of a col
	# 			□ Def pct30(column):
	# 				Return column.quantile(0.3)
	# 		§ Then you can pass this new function into the .aggregate method
	# 			□ Dogs["weight_kg"].agg(pct30) = 22.599
	# 	○ Can use on multiple columns
	# 		§ Ex: find 30th percentile for weight & height columns
	# 	○ Can calculate multiple summary stats at once
	# 		§ Can pass a list of functions into .agg()
	# 		§ Ex: calculate the 30th & 40th percentiles
	# 			□ Define both functions and pass them into .agg()
	# 			□ .agg([pct30, pct40])
	# • Can also calculate cumulative sum w/ .cumsum()

import pandas as pd

dogs = pd.read_csv("Data Camp-intro to Python/data-manipulation-pandas/dogs.csv", index_col=0)

dogs.head()
dogs.describe()
dogs.info()

# BASIC SUMMARY STATS
dogs["height_cm"].mean() #49.714285714285715
dogs["height_cm"].mode()
dogs["height_cm"].median() #49.0
dogs["height_cm"].min() #18
dogs["height_cm"].max() #77
dogs["height_cm"].var() #322.5714285714286
dogs["height_cm"].std() #17.960273621841864
dogs["height_cm"].sum() #348
dogs["height_cm"].quantile() #49.0


# CAN SUMMARIZE DATES - my dates probably not formatted properly - should be Y-M-D
dogs["date_of_birth"].min() #1/20/17
dogs["date_of_birth"].max() #9/16/16


# AGGREGATE METHOD - MAKES CUSTOM SUMMARY STATS
def pct30(column):
    return column.quantile(0.3)

dogs["weight_kg"].agg(pct30) #22.599999999999998

# .AGG() CAN SUMMARIZE MULTIPLE COLUMNS
dogs[["weight_kg", "height_cm"]].agg(pct30)

# weight_kg    22.6
# height_cm    45.4
# dtype: float64

def pct40(column):
    return column.quantile(0.4)

def pct60(column):
    return column.quantile(0.6)

dogs["weight_kg"].agg([pct30, pct40, pct60])

# pct30    22.6
# pct40    24.0
# pct60    24.0
# Name: weight_kg, dtype: float64



# CUMULATIVE STATS - RETURNS COL OF #s INSTEAD OF SINGLE VALUE
dogs["weight_kg"]

# 0    24
# 1    24
# 2    24
# 3    17
# 4    29
# 5     2
# 6    74
# Name: weight_kg, dtype: int64

dogs["weight_kg"].cumsum()

# 0     24
# 1     48
# 2     72
# 3     89
# 4    118
# 5    120
# 6    194
# Name: weight_kg, dtype: int64

dogs["weight_kg"].cummax()

# 0    24
# 1    24
# 2    24
# 3    24
# 4    29
# 5    29
# 6    74
# Name: weight_kg, dtype: int64


dogs["weight_kg"].cummin()

# 0    24
# 1    24
# 2    24
# 3    17
# 4    17
# 5     2
# 6     2
# Name: weight_kg, dtype: int64


dogs["weight_kg"].cumprod()

# 0            24
# 1           576
# 2         13824
# 3        235008
# 4       6815232
# 5      13630464
# 6    1008654336
# Name: weight_kg, dtype: int64



sales = pd.read_csv("Data Camp-intro to Python/data-manipulation-pandas/sales.csv", index_col=0)

#EXERCISE 1 - MEAN/MEDIAN
# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())


#OUTPUT IS FROM EXERCISE CODE
#   store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
# 0      1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
# 1      1    A           1 2010-03-05      21827.90       False          8.056                 0.693         8.106
# 2      1    A           1 2010-04-02      57258.43       False         16.817                 0.718         7.808
# 3      1    A           1 2010-05-07      17413.94       False         22.528                 0.749         7.808
# 4      1    A           1 2010-06-04      17558.09       False         27.050                 0.715         7.808
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10774 entries, 0 to 10773
# Data columns (total 9 columns):
#  #   Column                Non-Null Count  Dtype         
# ---  ------                --------------  -----         
#  0   store                 10774 non-null  int64         
#  1   type                  10774 non-null  object        
#  2   department            10774 non-null  int32         
#  3   date                  10774 non-null  datetime64[ns]
#  4   weekly_sales          10774 non-null  float64       
#  5   is_holiday            10774 non-null  bool          
#  6   temperature_c         10774 non-null  float64       
#  7   fuel_price_usd_per_l  10774 non-null  float64       
#  8   unemployment          10774 non-null  float64       
# dtypes: bool(1), datetime64[ns](1), float64(4), int32(1), int64(1), object(1)
# memory usage: 641.9+ KB
# None
# store                      15.442
# department                 45.218
# weekly_sales            23843.950
# is_holiday                  0.004
# temperature_c              15.732
# fuel_price_usd_per_l        0.750
# unemployment                8.082
# dtype: float64
# store                      13.000
# department                 40.000
# weekly_sales            12049.065
# is_holiday                  0.000
# temperature_c              16.967
# fuel_price_usd_per_l        0.743
# unemployment                8.099

# 23843.95014850566
# 12049.064999999999



#EXERCISE 2 - SUMMARIZE DATES
# Print the maximum of the date column
print(sales["date"].max()) #2012-10-26 00:00:00

# Print the minimum of the date column
print(sales["date"].min()) #2010-02-05 00:00:00



#EXERCISE 3 - AGGREGATE SUMMARIES
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales["temperature_c"].agg(iqr)) #16.583333333333336



# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr)) 

# temperature_c           16.583
# fuel_price_usd_per_l     0.073
# unemployment             0.565
# dtype: float64



# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

# #        temperature_c  fuel_price_usd_per_l  unemployment
# iqr            16.583                 0.073         0.565
# median         16.967                 0.743         8.099



# EXERCISE 4 - CUMULATIVE STATS
# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date", ascending=True)

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

    #      date  weekly_sales  cum_weekly_sales  cum_max_sales
    # 0  2010-02-05      24924.50          24924.50       24924.50
    # 1  2010-03-05      21827.90          46752.40       24924.50
    # 2  2010-04-02      57258.43         104010.83       57258.43
    # 3  2010-05-07      17413.94         121424.77       57258.43
    # 4  2010-06-04      17558.09         138982.86       57258.43
    # 5  2010-07-02      16333.14         155316.00       57258.43
    # 6  2010-08-06      17508.41         172824.41       57258.43
    # 7  2010-09-03      16241.78         189066.19       57258.43
    # 8  2010-10-01      20094.19         209160.38       57258.43
    # 9  2010-11-05      34238.88         243399.26       57258.43
    # 10 2010-12-03      22517.56         265916.82       57258.43
    # 11 2011-01-07      15984.24         281901.06       57258.43