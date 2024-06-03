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