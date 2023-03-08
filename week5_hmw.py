# For Q1 - Q5, use the "#" key to annotate the code and explain what *each line* of code is accomplishing
# For Q6 - Q8, you must find and use the "#" key to explain the error.
# Be as specific as possible. 
# Each line of code is worth .5 points for a total of 10 points. 

# Q1. List:
# creates a list w/ 5 strings each identifying a city and storing 
cities=['New York', 'Paris', 'Mexico City', 'Kuala Lumpur', 'Barcelona'] 



# Q2. For loop: 
# for item in lists - this will iterate across entire city list 
for city in cities: 
    print('My favorite city is ' + city) 
    

# Q3. Playing with lists:
# .append & .sort are methods
cities.append('Nairobi') 
cities.sort() 
print(cities) 

# Q4.Conditional script: 
# == is equivalency - if location is "New York", then print
# = assigns a value 
location = input("Which city do you want to learn about today?") 

if location == "New York": 
    print("Empire State Building, Central Park, Brooklyn Bridge") 
elif location == "Paris":  # elif = else if = if location is NOT NY, but is Paris, then print 
    print("Tour Eiffel, Arc de Triomphe, Jardin des Tuileries")
else:  # if it is neither NY or Paris, then print
    print("I don't know what location you're talking about! I'm just a little program...")
    

# Q5. Functions
# the name of the function is this_function - takes as its input x
def this_function(x): 
    print("this_function takes as its input: "+x)  
x = "python"
this_function(x)


# Q6. Find and explain the error:
list = [1, five, 12, '13'] 

# Q7. Find and explain the error:
x = 'hello'
y = x + 1 

# Q8. Find and explain the error:
for city in cities 
print('My favorite city is ' + 'city') 

# Q9. Find and explain the error:
x == 1