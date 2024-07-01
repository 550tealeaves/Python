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