import pandas as pd

dogs = pd.read_csv("Data Camp-intro to Python/data-manipulation-pandas/dogs.csv", index_col=0)

dogs.head()
dogs.describe()
dogs.info() 

dogs.sort_values("weight_kg") #sorts weights ascending

#       name        breed  color  height_cm  weight_kg date_of_birth
# 5   Stella    Chihuahua    Tan         18          2     4/20/2015
# 3   Cooper    Schnauzer   Gray         49         17    12/11/2011
# 0    Bella     Labrador  Brown         56         24      7/1/2013
# 1  Charlie       Poodle  Black         43         24     9/16/2016
# 2     Lucy    Chow Chow  Brown         46         24     8/25/2014
# 4      Max     Labrador  Black         59         29     1/20/2017
# 6   Bernie  St. Bernard  White         77         74     2/27/2018

dogs.sort_values("weight_kg", ascending=False) #sorts weights descending

#      name        breed  color  height_cm  weight_kg date_of_birth
# 6   Bernie  St. Bernard  White         77         74     2/27/2018
# 4      Max     Labrador  Black         59         29     1/20/2017
# 0    Bella     Labrador  Brown         56         24      7/1/2013
# 1  Charlie       Poodle  Black         43         24     9/16/2016
# 2     Lucy    Chow Chow  Brown         46         24     8/25/2014
# 3   Cooper    Schnauzer   Gray         49         17    12/11/2011
# 5   Stella    Chihuahua    Tan         18          2     4/20/2015


#SORT BY MULTIPLE VARIABLES - wrap in ([])
dogs.sort_values(["weight_kg", "height_cm"])

#       name        breed  color  height_cm  weight_kg date_of_birth
# 5   Stella    Chihuahua    Tan         18          2     4/20/2015
# 3   Cooper    Schnauzer   Gray         49         17    12/11/2011
# 1  Charlie       Poodle  Black         43         24     9/16/2016
# 2     Lucy    Chow Chow  Brown         46         24     8/25/2014
# 0    Bella     Labrador  Brown         56         24      7/1/2013
# 4      Max     Labrador  Black         59         29     1/20/2017
# 6   Bernie  St. Bernard  White         77         74     2/27/2018



#SORT BY MULTIPLE VARIABLES & CHANGE DIRECTION
dogs.sort_values(["weight_kg", "color"], ascending=[True, False])

#       name        breed  color  height_cm  weight_kg date_of_birth
# 5   Stella    Chihuahua    Tan         18          2     4/20/2015
# 3   Cooper    Schnauzer   Gray         49         17    12/11/2011
# 0    Bella     Labrador  Brown         56         24      7/1/2013
# 2     Lucy    Chow Chow  Brown         46         24     8/25/2014
# 1  Charlie       Poodle  Black         43         24     9/16/2016
# 4      Max     Labrador  Black         59         29     1/20/2017
# 6   Bernie  St. Bernard  White         77         74     2/27/2018


#SUBSETTING COLUMNS
#will return as a panda series
dogs["name"]

# 0      Bella
# 1    Charlie
# 2       Lucy
# 3     Cooper
# 4        Max
# 5     Stella
# 6     Bernie
# Name: name, dtype: object


#SUBSETTING MULTIPLE COLUMNS
dogs[["breed", "height_cm"]]

#          breed  height_cm
# 0     Labrador         56
# 1       Poodle         43
# 2    Chow Chow         46
# 3    Schnauzer         49
# 4     Labrador         59
# 5    Chihuahua         18
# 6  St. Bernard         77


#SUBSETTING ROWS
dogs[dogs["height_cm"]>50]

#      name        breed  color  height_cm  weight_kg date_of_birth
# 0   Bella     Labrador  Brown         56         24      7/1/2013
# 4     Max     Labrador  Black         59         29     1/20/2017
# 6  Bernie  St. Bernard  White         77         74     2/27/2018


#SUBSETTING BASED ON TEXT DATA
dogs[dogs["breed"] == "Labrador"]

#     name     breed  color  height_cm  weight_kg date_of_birth
# 0  Bella  Labrador  Brown         56         24      7/1/2013
# 4    Max  Labrador  Black         59         29     1/20/2017


dogs[dogs["date_of_birth"]< "2015-01-01"] #when writing dates list it as Y-M-D

#     name        breed  color  height_cm  weight_kg date_of_birth
# 3  Cooper    Schnauzer   Gray         49         17    12/11/2011
# 4     Max     Labrador  Black         59         29     1/20/2017
# 6  Bernie  St. Bernard  White         77         74     2/27/2018




#SUBSET ROWS TO MEET MULTIPLE CONDITIONS
is_lab = dogs["breed"] == "Labrador" #seelct rows w/ breed Labrador
is_brown = dogs["color"] == "Brown" #select rows w/ color Brown
dogs[is_lab & is_brown] #select row w/ both breed Labrador & color Brown

#     name     breed  color  height_cm  weight_kg date_of_birth
# 0  Bella  Labrador  Brown         56         24      7/1/2013


##ALTERNATIVE WYA TO TYPE THE ROWS/MULT CONDITIONS
dogs[(dogs["breed"] == "Labrador") & (dogs["color"] == "Brown")]

#     name     breed  color  height_cm  weight_kg date_of_birth
# 0  Bella  Labrador  Brown         56         24      7/1/2013




#FILTER ON MULTIPLE VALUES OF CATEGORICAL VARIABLE
# USE .isin() METHOD - WHICH ACCEPTS A LIST OF VALUES TO FILTER FOR
is_black_or_brown = dogs["color"].isin(["Black", "Brown"]) #select rows w/ color Brown or Black
dogs[is_black_or_brown]

#       name      breed  color  height_cm  weight_kg date_of_birth
# 0    Bella   Labrador  Brown         56         24      7/1/2013
# 1  Charlie     Poodle  Black         43         24     9/16/2016
# 2     Lucy  Chow Chow  Brown         46         24     8/25/2014
# 4      Max   Labrador  Black         59         29     1/20/2017




##EXERCISE 3 - SORTING ROWS
# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())

# #               region         state  individuals  family_members  state_pop
# 50            Mountain       Wyoming        434.0           205.0     577601
# 34  West North Central  North Dakota        467.0            75.0     758080
# 7       South Atlantic      Delaware        708.0           374.0     965479
# 39         New England  Rhode Island        747.0           354.0    1058287
# 45         New England       Vermont        780.0           511.0     624358




##EXERCISE 4
# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region', 'family_members'], ascending=[True, False])

# Print the top few rows
# print(homelessness_reg_fam.head())
#                region      state  individuals  family_members  state_pop
# 13  East North Central   Illinois       6752.0          3891.0   12723071
# 35  East North Central       Ohio       6929.0          3320.0   11676341
# 22  East North Central   Michigan       5209.0          3142.0    9984072
# 49  East North Central  Wisconsin       2740.0          2167.0    5807406
# 14  East North Central    Indiana       3776.0          1482.0    6695497


##EXERCISE 5 - SUBSETTING COLUMNS
# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())

# 0      2570.0
# 1      1434.0
# 2      7259.0
# 3      2280.0
# 4    109008.0
# Name: individuals, dtype: float64



# Make sure to select the "state" and "family_members" columns from the homelessness DataFrame
state_fam = homelessness[["state", "family_members"]]

# Print the head of the result to check your selection
print(state_fam.head())

#         state  family_members
# 0     Alabama           864.0
# 1      Alaska           582.0
# 2     Arizona          2606.0
# 3    Arkansas           432.0
# 4  California         20964.0



# Make sure to select the 'individuals' and 'state' columns from the homelessness DataFrame
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result to check your selection
print(ind_state.head())



## SUBSETTING ROWS
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]

# See the result
print(ind_gt_10k)

    #              region       state  individuals  family_members  state_pop
    # 4              Pacific  California     109008.0         20964.0   39461588
    # 9       South Atlantic     Florida      21443.0          9587.0   21244317
    # 32        Mid-Atlantic    New York      39827.0         52070.0   19530351
    # 37             Pacific      Oregon      11139.0          3337.0    4181886
    # 43  West South Central       Texas      19199.0          6111.0   28628666
    # 47             Pacific  Washington      16424.0          5880.0    7523869
    


# Make sure to filter the DataFrame using the correct column name and value
mountain_reg = homelessness[homelessness["region"] == "Mountain"]

# Print the result to see if it worked
print(mountain_reg)

#       region       state  individuals  family_members  state_pop
# 2   Mountain     Arizona       7259.0          2606.0    7158024
# 5   Mountain    Colorado       7607.0          3250.0    5691287
# 12  Mountain       Idaho       1297.0           715.0    1750536
# 26  Mountain     Montana        983.0           422.0    1060665
# 28  Mountain      Nevada       7058.0           486.0    3027341
# 31  Mountain  New Mexico       1949.0           602.0    2092741
# 44  Mountain        Utah       1904.0           972.0    3153550
# 50  Mountain     Wyoming        434.0           205.0     577601


# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)

#     region   state  individuals  family_members  state_pop
# 1  Pacific  Alaska       1434.0           582.0     735139


# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness["region"] == "South Atlantic") | (homelessness["region"] == "Mid-Atlantic")]

# See the result
print(south_mid_atlantic)

#             region                 state  individuals  family_members  state_pop
# 7   South Atlantic              Delaware        708.0           374.0     965479
# 8   South Atlantic  District of Columbia       3770.0          3134.0     701547
# 9   South Atlantic               Florida      21443.0          9587.0   21244317
# 10  South Atlantic               Georgia       6943.0          2556.0   10511131
# 20  South Atlantic              Maryland       4914.0          2230.0    6035802
# 30    Mid-Atlantic            New Jersey       6048.0          3350.0    8886025
# 32    Mid-Atlantic              New York      39827.0         52070.0   19530351
# 33  South Atlantic        North Carolina       6451.0          2817.0   10381615
# 38    Mid-Atlantic          Pennsylvania       8163.0          5349.0   12800922
# 40  South Atlantic        South Carolina       3082.0           851.0    5084156
# 46  South Atlantic              Virginia       3928.0          2047.0    8501286
# 48  South Atlantic         West Virginia       1021.0           222.0    1804291




# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)

#       region       state  individuals  family_members  state_pop
# 2   Mountain     Arizona       7259.0          2606.0    7158024
# 4    Pacific  California     109008.0         20964.0   39461588
# 28  Mountain      Nevada       7058.0           486.0    3027341
# 44  Mountain        Utah       1904.0           972.0    3153550