# 	# • Pandas built on matplotlib & numpy
# 	# • Provides multidim array objects

# 	# • Methods are written w/ ()
# 	# 	○ Describe
# 	# 	○ Info
# 	# 	○ head
# 	# • Attributes are not
# 	# 	○ Values
# 	# 	○ shape

# 	# • Diff ways to store datain pandas
# 	# 	○ Rectangular data aka tabular data = most common
# 	# 		§ Each observation (dog) is a row
# 	# 		§ Each variable (dog property) is a column
# 	# 		§ Pandas represents rect data as a DataFrame
# 	# 		§ Every value w/in col has same datatype
# 	# 			□ But diff col have diff data types


# EXPLORING THE DATAFRAME

# 	• .head() method
# 		○ Shows 1st 5 rows

# 	• .info() method
# 		○ Displays names of col, data types, & if they have missing values

# 	• .shape attribute
# 		○ Attribute contains the # of rows & cols
# 			§ (#rows, #cols)

# 	• .describe() method
# 		○ Summary stats for numerical cols

# DataFrames have 3 main attributes

# 	1. Values attribute
# 		○ Contains data values in 2D numpy array
# 	2. Columns attribute
# 		a. Provides labels for col

# 	3. Index attribute
# 		a. Provides labels for rows


##EXERCISE 1 - HEAD
import pandas as pd
print(homelessness.head())

#                region       state  individuals  family_members  state_pop
# 0  East South Central     Alabama       2570.0           864.0    4887681
# 1             Pacific      Alaska       1434.0           582.0     735139
# 2            Mountain     Arizona       7259.0          2606.0    7158024
# 3  West South Central    Arkansas       2280.0           432.0    3009733
# 4             Pacific  California     109008.0         20964.0   39461588



##EXERCISE 2 - INFO
# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape) #(51, 5) - 51 rows, 5 cols

# Print a description of homelessness
print(homelessness.describe())

# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 51 entries, 0 to 50
# Data columns (total 5 columns):
#  #   Column          Non-Null Count  Dtype  
# ---  ------          --------------  -----  
#  0   region          51 non-null     object 
#  1   state           51 non-null     object 
#  2   individuals     51 non-null     float64
#  3   family_members  51 non-null     float64
#  4   state_pop       51 non-null     int64  
# dtypes: float64(2), int64(1), object(2)
# memory usage: 2.4+ KB
# None


# print(homelessness.describe())
#        individuals  family_members  state_pop
# count       51.000          51.000  5.100e+01
# mean      7225.784        3504.882  6.406e+06
# std      15991.025        7805.412  7.327e+06
# min        434.000          75.000  5.776e+05
# 25%       1446.500         592.000  1.777e+06
# 50%       3082.000        1482.000  4.461e+06
# 75%       6781.500        3196.000  7.341e+06
# max     109008.000       52070.000  3.946e+07




##EXERCISE 3 - PARTS OF DATAFRAME
# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print (homelessness.values)

# Print the column index of homelessness
print (homelessness.columns)

# Print the row index of homelessness
print (homelessness.index)

# [['East South Central' 'Alabama' 2570.0 864.0 4887681]
#  ['Pacific' 'Alaska' 1434.0 582.0 735139]
#  ['Mountain' 'Arizona' 7259.0 2606.0 7158024]
#  ['West South Central' 'Arkansas' 2280.0 432.0 3009733]
#  ['Pacific' 'California' 109008.0 20964.0 39461588]
#  ['Mountain' 'Colorado' 7607.0 3250.0 5691287]
#  ['New England' 'Connecticut' 2280.0 1696.0 3571520]
#  ['South Atlantic' 'Delaware' 708.0 374.0 965479]
#  ['South Atlantic' 'District of Columbia' 3770.0 3134.0 701547]
#  ['South Atlantic' 'Florida' 21443.0 9587.0 21244317]
#  ['South Atlantic' 'Georgia' 6943.0 2556.0 10511131]
#  ['Pacific' 'Hawaii' 4131.0 2399.0 1420593]
#  ['Mountain' 'Idaho' 1297.0 715.0 1750536]
#  ['East North Central' 'Illinois' 6752.0 3891.0 12723071]
#  ['East North Central' 'Indiana' 3776.0 1482.0 6695497]
#  ['West North Central' 'Iowa' 1711.0 1038.0 3148618]
#  ['West North Central' 'Kansas' 1443.0 773.0 2911359]
#  ['East South Central' 'Kentucky' 2735.0 953.0 4461153]
#  ['West South Central' 'Louisiana' 2540.0 519.0 4659690]
#  ['New England' 'Maine' 1450.0 1066.0 1339057]
#  ['South Atlantic' 'Maryland' 4914.0 2230.0 6035802]
#  ['New England' 'Massachusetts' 6811.0 13257.0 6882635]
#  ['East North Central' 'Michigan' 5209.0 3142.0 9984072]
#  ['West North Central' 'Minnesota' 3993.0 3250.0 5606249]
#  ['East South Central' 'Mississippi' 1024.0 328.0 2981020]
#  ['West North Central' 'Missouri' 3776.0 2107.0 6121623]
#  ['Mountain' 'Montana' 983.0 422.0 1060665]
#  ['West North Central' 'Nebraska' 1745.0 676.0 1925614]
#  ['Mountain' 'Nevada' 7058.0 486.0 3027341]
#  ['New England' 'New Hampshire' 835.0 615.0 1353465]
#  ['Mid-Atlantic' 'New Jersey' 6048.0 3350.0 8886025]
#  ['Mountain' 'New Mexico' 1949.0 602.0 2092741]
#  ['Mid-Atlantic' 'New York' 39827.0 52070.0 19530351]
#  ['South Atlantic' 'North Carolina' 6451.0 2817.0 10381615]
#  ['West North Central' 'North Dakota' 467.0 75.0 758080]
#  ['East North Central' 'Ohio' 6929.0 3320.0 11676341]
#  ['West South Central' 'Oklahoma' 2823.0 1048.0 3940235]
#  ['Pacific' 'Oregon' 11139.0 3337.0 4181886]
#  ['Mid-Atlantic' 'Pennsylvania' 8163.0 5349.0 12800922]
#  ['New England' 'Rhode Island' 747.0 354.0 1058287]
#  ['South Atlantic' 'South Carolina' 3082.0 851.0 5084156]
#  ['West North Central' 'South Dakota' 836.0 323.0 878698]
#  ['East South Central' 'Tennessee' 6139.0 1744.0 6771631]
#  ['West South Central' 'Texas' 19199.0 6111.0 28628666]
#  ['Mountain' 'Utah' 1904.0 972.0 3153550]
#  ['New England' 'Vermont' 780.0 511.0 624358]
#  ['South Atlantic' 'Virginia' 3928.0 2047.0 8501286]
#  ['Pacific' 'Washington' 16424.0 5880.0 7523869]
#  ['South Atlantic' 'West Virginia' 1021.0 222.0 1804291]
#  ['East North Central' 'Wisconsin' 2740.0 2167.0 5807406]
#  ['Mountain' 'Wyoming' 434.0 205.0 577601]]
# Index(['region', 'state', 'individuals', 'family_members', 'state_pop'], dtype='object')
# Int64Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
#             49, 50],
#            dtype='int64')



