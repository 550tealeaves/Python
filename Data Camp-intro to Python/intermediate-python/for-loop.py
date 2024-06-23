# 	• For var in seq:
# 		Expression
		
# 	• For each var in seq, execute expression

# Fam = [1.73, 1.68, 1.71, 1.89]

# Goal 
# 	• Print out each item in the list separately


# 	• For height in fam: 
# 		Print(height)
		

# 	• On every iteration, print out value of height

# 	• No access to indexes


# Goal 
# 	• Print out both the height value AND the index
# 	• Use enumerate
# 		○ Produces 2 values on iteration
# 		○ In the example, index contains the index & height contains the float 

# Loop over string
# 	• For loop can iterate over every character in a string
# 	• For c in "family" :
# 		Print(c.capitalize())
# 	• 6 different print outs , 1 for each character, in the string "family" occurs 


fam = [1.73, 1.68, 1.71, 1.89]
for height in fam :
    print(height) #will print each item on its own line

help(enumerate)

for index, height in enumerate(fam) :
    print("index" + " " + str(index) + ": " + str(height))


for c in "family":
    print(c.capitalize()) #prints each letter capitalized on own line




##EXERCISE 1 - LOOP OVER A LIST
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for values in areas:
    print(values)




##EXERCISE 2- INDEXES & VALUES
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print("room " + "" + str(index) + ": " + str(a))


##EXERCISE 3 - INDEXES & VALUES PART 2
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop - change the starting index by doing math on variable
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area)) 



##EXERCISE 4 - LOOP OVER LISTS OF LISTS
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for room in house:
    print("the " + room[0] + " is " + str(room[1]) + " sqm") #the kitchen is 18.0 sqm
    #the living room is 20.0 sqm


