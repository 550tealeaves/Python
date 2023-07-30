#Grouping data in lists
#Important to be able to group data - don't want to create a new variable for every new piece of data
#Collect related data inside a list using []
todo = ['Read', 'Workout', 'Code'] #read, workout, code = elements
print(todo) # prints above list 

#Elements = values or data inside list 

#If you put a string b/w brackets = make list w/ 1 value
todo = ['Coding']
print(todo) # prints ['Coding']

#Use commas to separate 2+ values (elements) in list - commas are OUTSIDE of the quotes
todo = ['Read', 'Workout']
print(todo)

# Lists can hold infinite # of values of ANY DATA TYPE - just separate w/ comma
users = [] # empty list
print(users) # prints only [] b/c empty list


active_users = ['Finn']
print('Active:') #prints "Active:"
print(active_users) #prints ["Finn"]

characters = ['mario', 'luigi', 'peaches', 'bowser']
print(characters)


reviewed_movies = ['Withnail and I', 'Mad Max']
print(reviewed_movies)

#CHANGING DATA W/IN LISTS

# Every element i list has numbered position called an index
# Indices always start at 0 
temperatures = [17, 20, 26, 24]
print(temperatures[1]) #will print the 2nd element in list = 20
print(temperatures[2]) #will print 3rd element in list = 26

# To change the 3rd value in list, 1st access it and then assign it to a new value
temperatures = [17, 20, 26, 24]
temperatures[2] = 25 # changes 3rd value from 26 to 25
print(temperatures) #3rd value will be 26 instead of 26
temperatures[3] = 20 #reassign 4th value from 24 to 20
print(temperatures) #4th value will be 20 instead of 24


cars = ['Fiat', 'Tesla', 'Saab']
print(cars[2]) #prints 'Saab'
cars[1] = 'Cadillac'  #changes 'Tesla' to 'Cadillac
print(cars)

items = ['milk', 'tomato', 'apple']
print(items) # 'milk', 'tomato', "apple"
print (items[1]) # 'tomato'
items[1] = 'cheese'
print(items) # "milk", "cheese", "apple"