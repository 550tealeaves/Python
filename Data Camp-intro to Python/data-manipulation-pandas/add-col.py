#	• Adding new col = feature engineering
	# • Left side of eq has new col w/in []
	# • Right side of the equal sign contains the necessary formula to creating the new col 
	# 	○ Formula can contain 1+ col 

import pandas as pd

dogs = pd.read_csv("Data Camp-intro to Python/data-manipulation-pandas/dogs.csv", index_col=0)

dogs.head()
dogs.describe()
dogs.info() 


##ADD NEW COL AKA FEATURE ENGINEERING
#LEFT SIDE OF "=" HAS NEW COL WRAPPED IN []
#RIGHT SIDE OF "=" HAS RELEVANT FORMULA TO CREATE NEW COL
#FORM CAN CONTAIN 1+ COL

#CREATE COL HEIGHT_M THAT HAS THE HEIGHTS CONVERTED TO METERS
dogs["height_m"] = dogs["height_cm"] /100
print(dogs)

#      name        breed  color  ...  weight_kg  date_of_birth height_m
# 0    Bella     Labrador  Brown  ...         24       7/1/2013     0.56     
# 1  Charlie       Poodle  Black  ...         24      9/16/2016     0.43     
# 2     Lucy    Chow Chow  Brown  ...         24      8/25/2014     0.46     
# 3   Cooper    Schnauzer   Gray  ...         17     12/11/2011     0.49     
# 4      Max     Labrador  Black  ...         29      1/20/2017     0.59     
# 5   Stella    Chihuahua    Tan  ...          2      4/20/2015     0.18     
# 6   Bernie  St. Bernard  White  ...         74      2/27/2018     0.77 



#CREATE COL FOR DOG BMI
dogs["bmi"] = dogs["weight_kg"] / dogs["height_m"] **2
print(dogs)

#       name        breed  color  ...  date_of_birth  height_m         bmi
# 0    Bella     Labrador  Brown  ...       7/1/2013      0.56   76.530612   
# 1  Charlie       Poodle  Black  ...      9/16/2016      0.43  129.799892   
# 2     Lucy    Chow Chow  Brown  ...      8/25/2014      0.46  113.421550   
# 3   Cooper    Schnauzer   Gray  ...     12/11/2011      0.49   70.803832   
# 4      Max     Labrador  Black  ...      1/20/2017      0.59   83.309394   
# 5   Stella    Chihuahua    Tan  ...      4/20/2015      0.18   61.728395   
# 6   Bernie  St. Bernard  White  ...      2/27/2018      0.77  124.810255



#MULTIPLE MANIPULATIONS
bmi_lt_100 = dogs[dogs["bmi"] < 100] #select those w/ bmi < 100
bmi_lt_100_height = bmi_lt_100.sort_values("height_cm", ascending=False) #sort the heights in descending order
bmi_lt_100_height[["name", "height_cm", "bmi"]] #select only these 3 cols to show

#SHOWS THE NAME/HEIGHT_CM & BMI COLS FOR DOGS W/ BMI < 100 & HEIGHTS SORTED IN DESCENDING ORDER
#      name  height_cm        bmi
# 4     Max         59  83.309394
# 0   Bella         56  76.530612
# 3  Cooper         49  70.803832
# 5  Stella         18  61.728395




##EXERCISE 1 - ADDING NEW COLS
# Add total col as sum of individuals and family_members
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

homelessness['p_individuals'] = homelessness['individuals'] / homelessness['total']

# See the result
print(homelessness)

#                 region                 state  individuals  family_members  state_pop     total  p_individuals
# 0   East South Central               Alabama       2570.0           864.0    4887681    3434.0          0.748
# 1              Pacific                Alaska       1434.0           582.0     735139    2016.0          0.711
# 2             Mountain               Arizona       7259.0          2606.0    7158024    9865.0          0.736
# 3   West South Central              Arkansas       2280.0           432.0    3009733    2712.0          0.841
# 4              Pacific            California     109008.0         20964.0   39461588  129972.0          0.839
# 5             Mountain              Colorado       7607.0          3250.0    5691287   10857.0          0.701
# 6          New England           Connecticut       2280.0          1696.0    3571520    3976.0          0.573
# 7       South Atlantic              Delaware        708.0           374.0     965479    1082.0          0.654
# 8       South Atlantic  District of Columbia       3770.0          3134.0     701547    6904.0          0.546
# 9       South Atlantic               Florida      21443.0          9587.0   21244317   31030.0          0.691
# 10      South Atlantic               Georgia       6943.0          2556.0   10511131    9499.0          0.731
# 11             Pacific                Hawaii       4131.0          2399.0    1420593    6530.0          0.633
# 12            Mountain                 Idaho       1297.0           715.0    1750536    2012.0          0.645
# 13  East North Central              Illinois       6752.0          3891.0   12723071   10643.0          0.634
# 14  East North Central               Indiana       3776.0          1482.0    6695497    5258.0          0.718
# 15  West North Central                  Iowa       1711.0          1038.0    3148618    2749.0          0.622
# 16  West North Central                Kansas       1443.0           773.0    2911359    2216.0          0.651
# 17  East South Central              Kentucky       2735.0           953.0    4461153    3688.0          0.742
# 18  West South Central             Louisiana       2540.0           519.0    4659690    3059.0          0.830
# 19         New England                 Maine       1450.0          1066.0    1339057    2516.0          0.576
# 20      South Atlantic              Maryland       4914.0          2230.0    6035802    7144.0          0.688
# 21         New England         Massachusetts       6811.0         13257.0    6882635   20068.0          0.339
# 22  East North Central              Michigan       5209.0          3142.0    9984072    8351.0          0.624
# 23  West North Central             Minnesota       3993.0          3250.0    5606249    7243.0          0.551
# 24  East South Central           Mississippi       1024.0           328.0    2981020    1352.0          0.757
# 25  West North Central              Missouri       3776.0          2107.0    6121623    5883.0          0.642
# 26            Mountain               Montana        983.0           422.0    1060665    1405.0          0.700
# 27  West North Central              Nebraska       1745.0           676.0    1925614    2421.0          0.721
# 28            Mountain                Nevada       7058.0           486.0    3027341    7544.0          0.936
# 29         New England         New Hampshire        835.0           615.0    1353465    1450.0          0.576
# 30        Mid-Atlantic            New Jersey       6048.0          3350.0    8886025    9398.0          0.644
# 31            Mountain            New Mexico       1949.0           602.0    2092741    2551.0          0.764
# 32        Mid-Atlantic              New York      39827.0         52070.0   19530351   91897.0          0.433
# 33      South Atlantic        North Carolina       6451.0          2817.0   10381615    9268.0          0.696
# 34  West North Central          North Dakota        467.0            75.0     758080     542.0          0.862
# 35  East North Central                  Ohio       6929.0          3320.0   11676341   10249.0          0.676
# 36  West South Central              Oklahoma       2823.0          1048.0    3940235    3871.0          0.729
# 37             Pacific                Oregon      11139.0          3337.0    4181886   14476.0          0.769
# 38        Mid-Atlantic          Pennsylvania       8163.0          5349.0   12800922   13512.0          0.604
# 39         New England          Rhode Island        747.0           354.0    1058287    1101.0          0.678
# 40      South Atlantic        South Carolina       3082.0           851.0    5084156    3933.0          0.784
# 41  West North Central          South Dakota        836.0           323.0     878698    1159.0          0.721
# 42  East South Central             Tennessee       6139.0          1744.0    6771631    7883.0          0.779
# 43  West South Central                 Texas      19199.0          6111.0   28628666   25310.0          0.759
# 44            Mountain                  Utah       1904.0           972.0    3153550    2876.0          0.662
# 45         New England               Vermont        780.0           511.0     624358    1291.0          0.604
# 46      South Atlantic              Virginia       3928.0          2047.0    8501286    5975.0          0.657
# 47             Pacific            Washington      16424.0          5880.0    7523869   22304.0          0.736
# 48      South Atlantic         West Virginia       1021.0           222.0    1804291    1243.0          0.821
# 49  East North Central             Wisconsin       2740.0          2167.0    5807406    4907.0          0.558
# 50            Mountain               Wyoming        434.0           205.0     577601     639.0          0.679





##EXERCISE 2 - COMBO
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)


#                    state  indiv_per_10k
# 8   District of Columbia         53.738
# 11                Hawaii         29.079
# 4             California         27.624
# 37                Oregon         26.636
# 28                Nevada         23.314
# 47            Washington         21.829
# 32              New York         20.392