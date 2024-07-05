# 	• Pivot tables = another way to calculate grouped summary statistics

# 	• Use .pivot_table() method to create pivot table
# 		○ Values argument = col you want to summarize
# 		○ Index argument = col you want to group by
# 		○ Default = mean value for each group
# To use a different argument, use the aggfunc argument

# 	• Margins=True
# 		○ Last row/col of pivot table has the totals 
# 		○ Has the means of all values in cols/rows
# 			§ Excludes missing values
# 		○ See summary stat for mult levels of dataset



# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)


#       weekly_sales
# type              
# A        23674.667
# B        25696.678




# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)


#              mean       median
#      weekly_sales weekly_sales
# type                          
# A       23674.667     11943.92
# B       25696.678     13336.08



# Try using the pivot_table method to group by 'type' and 'is_holiday'
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

# Print the result to check
print(mean_sales_by_type_holiday)

# is_holiday      False     True
# type                          
# A           23768.584  590.045
# B           25751.981  810.705




# Try using pivot_table to group by department and type, and fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0))

# type                 A           B
# department                        
# 1            30961.725   44050.627
# 2            67600.159  112958.527
# 3            17160.003   30580.655
# 4            44285.399   51219.654
# 5            34821.011   63236.875
# ...                ...         ...
# 95          123933.787   77082.102
# 96           21367.043    9528.538
# 97           28471.267    5828.873
# 98           12875.423     217.428
# 99             379.124       0.000

# [80 rows x 2 columns]




# Use pivot_table to calculate the mean weekly_sales by department and type
# Fill missing values with 0 and include row and column sums
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))

# type                A           B        All
# department                                  
# 1           30961.725   44050.627  32052.467
# 2           67600.159  112958.527  71380.023
# 3           17160.003   30580.655  18278.391
# 4           44285.399   51219.654  44863.254
# 5           34821.011   63236.875  37189.000
# ...               ...         ...        ...
# 96          21367.043    9528.538  20337.608
# 97          28471.267    5828.873  26584.401
# 98          12875.423     217.428  11820.590
# 99            379.124       0.000    379.124
# All         23674.667   25696.678  23843.950

# [81 rows x 3 columns]






##### WORKING W/ PIVOT TABLES IN DATAFRAMES ######

# 	• Create pivot table with .pivot_table() - which takes 3 arguments
# 		1. Col name (as string) 
# 			i. Has values to aggregate
# 		2. Index - cols to group by & display in rows 
# 		3. Columns - cols to group by & display in cols

# 	• Example below shows all the heights in cm for the diff breeds based on color
# 	• A pivot table is a dataframe with a sorted index
# 		○ Can use the previously learned techniques on slicing/subsetting dataframs
# 		○ Loc & slicing = great for subsetting pivot tables 

# Calculating summary stats on dataframe
# 	• Axis argument
# 		○ Default value is "index"
# 			§ Means to calculate statistics across the rows
# 			§ Below example - calculates the mean for each color = across the breeds
# 	• To calculate summary stats for each row, (across cols),
# 		○ Axis = "columns"
# 			§ Ex: mean height calculated for each breed = across the colors 
# 	• Normally wouldn't use the axis argument b/c dataframes contain diff data types
# 	• BUT pivot tables contain the same data type = can set axis

import pandas as pd

dogs = pd.read_csv("Data Camp-intro to Python/data-manipulation-pandas/dogs.csv", index_col=0)

dogs.head()

dogs_height_by_breed_vs_color = dogs.pivot_table("height_cm", index="breed", columns="color")
print(dogs_height_by_breed_vs_color)
#shows all heights in cm for diff breeds based on color

# color        Black  Brown  Gray   Tan  White
# breed
# Chihuahua      NaN    NaN   NaN  18.0    NaN
# Chow Chow      NaN   46.0   NaN   NaN    NaN
# Labrador      59.0   56.0   NaN   NaN    NaN
# Poodle        43.0    NaN   NaN   NaN    NaN
# Schnauzer      NaN    NaN  49.0   NaN    NaN
# St. Bernard    NaN    NaN   NaN   NaN   77.0


dogs_height_by_breed_vs_color.loc["Chow Chow": "Poodle"]

# color      Black  Brown  Gray  Tan  White
# breed
# Chow Chow    NaN   46.0   NaN  NaN    NaN
# Labrador    59.0   56.0   NaN  NaN    NaN
# Poodle      43.0    NaN   NaN  NaN    NaN


#CALCULATE SUMMARY STATS
dogs_height_by_breed_vs_color.mean(axis="index") #calculate mean across the rows 
#mean height calculated for each color dog across the breeds

# color
# Black    51.0
# Brown    51.0
# Gray     49.0
# Tan      18.0
# White    77.0
# dtype: float64


dogs_height_by_breed_vs_color.mean(axis="columns") #calculate mean across columsn
#mean height calculated for each breed across colors

# breed
# Chihuahua      18.0
# Chow Chow      46.0
# Labrador       57.5
# Poodle         43.0
# Schnauzer      49.0
# St. Bernard    77.0
# dtype: float64




## EXAMPLE 1

# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index=["country", "city"], columns="year")

# See the result
print(temp_by_country_city_vs_year)

# year                              2000    2001    2002    2003    2004  ...    2009    2010    2011    2012    2013
# country       city                                                      ...                                        
# Afghanistan   Kabul             15.823  15.848  15.715  15.133  16.128  ...  15.093  15.676  15.812  14.510  16.206
# Angola        Luanda            24.410  24.427  24.791  24.867  24.216  ...  24.325  24.440  24.151  24.240  24.554
# Australia     Melbourne         14.320  14.180  14.076  13.986  13.742  ...  14.647  14.232  14.191  14.269  14.742
#               Sydney            17.567  17.854  17.734  17.592  17.870  ...  18.176  17.999  17.713  17.474  18.090
# Bangladesh    Dhaka             25.905  25.931  26.095  25.927  26.136  ...  26.536  26.648  25.803  26.284  26.587
# ...                                ...     ...     ...     ...     ...  ...     ...     ...     ...     ...     ...
# United States Chicago           11.090  11.703  11.532  10.482  10.943  ...  10.298  11.816  11.214  12.821  11.587
#               Los Angeles       16.643  16.466  16.430  16.945  16.553  ...  16.677  15.887  15.875  17.090  18.121
#               New York           9.969  10.931  11.252   9.836  10.389  ...  10.142  11.358  11.272  11.971  12.164
# Vietnam       Ho Chi Minh City  27.589  27.832  28.065  27.828  27.687  ...  27.853  28.282  27.675  28.249  28.455
# Zimbabwe      Harare            20.284  20.861  21.079  20.889  20.308  ...  20.524  21.166  20.782  20.523  19.756

# [100 rows x 14 columns]



##EXERCISE 2

import pandas as pd
temperatures = pd.read_pickle("/usr/local/share/datasets/temperatures_no_unc.pkl")

temperatures["year"] = temperatures["date"].dt.year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index = ["country", "city"], columns = "year")

# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi")]

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi"), "2005":"2010"]


# year                    2005    2006    2007    2008    2009    2010
# country  city                                                       
# Egypt    Cairo        22.006  22.050  22.361  22.644  22.625  23.718
#          Gizeh        22.006  22.050  22.361  22.644  22.625  23.718
# Ethiopia Addis Abeba  18.313  18.427  18.143  18.165  18.765  18.298
# France   Paris        11.553  11.788  11.751  11.278  11.464  10.410
# Germany  Berlin        9.919  10.545  10.883  10.658  10.062   8.607
# India    Ahmadabad    26.828  27.283  27.511  27.049  28.096  28.018
#          Bangalore    25.477  25.418  25.464  25.353  25.726  25.705
#          Bombay       27.036  27.382  27.635  27.178  27.845  27.765
#          Calcutta     26.729  26.986  26.585  26.522  27.153  27.289
#          Delhi        25.716  26.366  26.146  25.675  26.554  26.520


##EXERCISE 3
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])

# year
# 2013    20.312
# dtype: float64
# country  city  
# China    Harbin    4.877
# dtype: float64