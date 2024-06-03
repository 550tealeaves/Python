# ***METHODS***
#Methods are functions that belong to objects (str, lists, float, boolean, integers) & there are specific methods for specific objects
# Ex: capitalize(), replace(), bit_length(), conjugate(), index(), count() etc   
# Must use . notation to call method
# methods can be chained together using dot notation

# LIST METHODS
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam.index("mom") # 4  - returns index position of "mom"
fam.count(1.73) # counts # of times 1.73 is in list - 1

# STRING METHODS
sister = 'liz'
sister.capitalize() #'Liz' - capitalizes the string
sister.replace("z", "sa") #lisa - will replace the letter z with sa
brother = 'dave'
brother.replace('e', 'ey').capitalize() #Davey - first replaces e with ey & then capitalizes string

# Some methods can change the objects they are called on
fam.append("me") # add element to list
fam #['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89, 'me']
fam.append(1.79) # adding element to list as new height
fam #['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89, 'me', 1.79]


# ***EXERCISES***
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place - use .count()
print(place.count("o")) # 3





# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0)) #2

# Print out how often 9.50 appears in areas
print(areas.count(9.50)) #1




# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5) #adds 24.5 to the list
areas.append(15.45) #adds 15.45 to list, placing it after the 24.5

# Print out areas
print(areas) #[11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.45]

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas) #[15.45, 24.5, 9.5, 10.75, 20.0, 18.0, 11.25]