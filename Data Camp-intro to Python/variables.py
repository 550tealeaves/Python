monthly_savings = 10
num_months = 12
intro = "Hello! How are you?"

# Calculate year_savings using monthly_savings and num_months
year_savings = monthly_savings*num_months

# Print the type of year_savings
print(type(year_savings))
print(year_savings)

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro) #Hello! How are you?Hello! How are you?


# Definition of savings and total_savings
savings = 100
total_savings = 150


# Fix the printout

print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)
print(pi_float)

#Can use multiplication in strings to repeat certain worlds
"I said " + ("Could you come here, please? " * 3) + "Melissa"


# ******LISTS ******
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list called areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)



# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas) #['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0, 'bedroom', 10.75, 'bathroom', 9.5]


#More examples of lists
my_list = [1, 3, 4, 2]
print(my_list) #[1, 3, 4, 2]

my_list = [[1, 2, 3], [4, 5, 7]]
print(my_list) #[[1, 2, 3], [4, 5, 7]]

my_list = [1 + 2, "a" * 5, 3]
print(my_list) #[3, 'aaaaa', 3]


# LIST OF LISTS
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed], 
         ["bathroom", bath]]

# Print out house
print(house) # [['hallway', 11.25], ['kitchen', 18.0], ['living room', 20.0], ['bedroom', 10.75], ['bathroom', 9.5]]

# Print out the type of house
print(type(house)) #list


# ****SUBSETTING LISTS****

# Use index to access items in list
# 1st item always has index 0
# Can count backwards and use negative values to access end items
# 1st item backwards has index -1
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam[6] #dad
fam[-2] #dad

# List slicing
# Lets you select multiple items in list & create a new list
fam[3:5] # [1.68, 'mom'] only returns the 4th/5th items, does not return 6th item

#[start: end] start = inclusive, end = exclusive

fam[1:4] # [1.73, "emma", 1.68] 2nd, 3rd, 4th items

# can omit the index before or after the colon
# if no start index, then starts at index=0
fam[:4] #['liz', 1.73, "emma", 1.68]

#if no end index, will include all elements INCLUDING  the last value
fam[5:] #[1.71, 'dad', 1.89]


#EXERCISES
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1]) #11.25

# Print out last element from areas
print(areas[-1]) #9.50

# Print out the area of the living room
print(areas[-5]) #20.0


#Subset & calculate
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3] #adding the areas of kitchen & bedroom



# Print the variable eat_sleep_area
print(eat_sleep_area) #28.75


# Slicing and dicing
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[-4:] #have no ending index - so starts at 4th item from end and includes all items after to the end
upstairs_alt = areas[6:10] # includes 6th, 7th, 8th, 9th items but NOT the 10th

# Print out downstairs and upstairs
print(downstairs) # ['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0]
print(upstairs) #['bedroom', 10.75, 'bathroom', 9.5]
print(upstairs_alt) # ['bedroom', 10.75, 'bathroom', 9.5]


#Omitting the beginning or ending indices 
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[-3:]

print(downstairs) #['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0]
print(upstairs) #[10.75, 'bathroom', 9.5]


# REPLACE LIST ELEMENTS
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

# Print new areas list
print(areas) #['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5]



# EXTEND A LIST
# Use the + operator to add more elements to a list
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

print(areas_1) #['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5, 'poolhouse', 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

print(areas_2) #['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5, 'poolhouse', 24.5, 'garage', 15.45]



# DELETE LIST ELEMENTS
# Once you remove an element from a list, the indexes of the elements that come after the deleted element all change! So you remove 1st element, indices change, then you remove 2nd element, and indices change again.
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Same line
#command1; command2

# Separate lines
#command1
#command2

#del(areas[10]); del(areas[11]) # removes the 10th/11th indices - poolhouse, 24.5

del(areas[-4:-2])
print(areas) #['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5, 24.5, 15.45]



# INNER WORKINGS OF LISTS
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy - use list(array_name) to prevent changes to the original areas array w/o this then printing areas would have the same changes as areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0


# Print areas
print(areas) #[11.25, 18.0, 20.0, 10.75, 9.5]
print(areas_copy) #[5.0, 18.0, 20.0, 10.75, 9.5]

