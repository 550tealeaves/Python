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