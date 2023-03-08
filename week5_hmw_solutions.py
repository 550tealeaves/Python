# For Q1 - Q5, use the "#" key to annotate the code and explain what *each line* of code is accomplishing
# For Q6 - Q8, you must find and use the "#" key to explain the error.
# Be as specific as possible. 
# Each line of code is worth .5 points for a total of 10 points. 

# Q1. List:
cities=['New York', 'Paris', 'Mexico City', 'Kuala Lumpur', 'Barcelona'] 
# In this command, we are creating a list with 5 items and setting it equal to the variable "cities"

# Q2. For loop: 
for city in cities: #this is the start of a for loop. We are saying, for every item "city" in the "cities" list
    print('My favorite city is ' + city) 
    # we are using the print function to ask Python to display the sentence "My favorite city is" 
    # along with the input variable


# Q3. Playing with lists:
cities.append('Nairobi') #we are using the append function to add a new city "Nairobi" to our cities list
cities.sort() #we are using the sort function to sort our cities list in alphabetical order
print(cities) #we are using the print function to display our new cities list

# Q4.Conditional script: 
location = input("Which city do you want to learn about today?") 
# we are using the input function to ask the user to input a city and setting the result equal to 
# a new variable "location" 
if location == "New York": #we are setting up a conditional that says if "location" is equivalent to "New York"
    print("Empire State Building, Central Park, Brooklyn Bridge") 
    #then display the following output: "Empire State Building, Central Park, Brooklyn Bridge"
elif location == "Paris": 
    #we are adding another conditional that says if "location" is not equivalent to "New York" but 
    # is equivalent to Paris
    print("Tour Eiffel, Arc de Triomphe, Jardin des Tuileries")
    #then display the following output: "Tour Eiffel, Arc de Triomphe, Jardin des Tuileries"
else: #we are ending our conditional by saying "for anything other than Paris and New York"
    print("I don't know what location you're talking about! I'm just a little program...")
    #then display the following output: "I don't know what location you're talking about! 
    # I'm just a little program...""

# Q5. Functions
def this_function(x): #we are defining a new function named "this_function" that takes an input "x"
    print("this_function takes as its input: "+x) #we use the print function to display the results of our function
    # with input "x"



# Q6. Find and explain the error:
list = [1, five, 12, '13'] #five is not defined. It should be a string in quotation marks ("five" or 'five')

# Q7. Find and explain the error:
x = 'hello'
y = x + 1 #we can't concatenate data types, e.g., string and integers

# Q8. Find and explain the error:
for city in cities #this for loop code is missing ":" at the end of the line, which is required for initiating the loop
print('My favorite city is ' + 'city') #this print function needs to be indented

# Q9. Find and explain the error:
x == 1 # "==" checks whether the two given operands are equal or not. Since we haven't defined x=1 as a variable, this statement
# can't run
