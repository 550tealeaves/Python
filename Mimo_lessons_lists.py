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

# UPDATING LISTS
# To add value to list, code the list_name.append('new-value')
scores = [24, 23]
scores.append(25) # adds 25 to list
print(scores) # new list puts 25 at the last index position

users = ["john", "hannah", "marco"]
users.append("julian")
print(users) # print "john", "hannah", "marco", "julian"

# To add new value to a SPECIFIC INDEX, use insert()
# index() has 2 parameters: 1st = index, 2nd = value
shopping = ["kiwis", "peas"]
shopping.insert(0, "lemon") # will add "lemon" at 0 index position (1st)
print(shopping) # prints "lemon", "kiwis", "peas"

shopping = ['kiwis', 'peas']
shopping.insert(0, 'lemon')  # will add "lemon" at 0 index position (1st)
shopping.insert(1, 'chocolate') # adds 'chocolate' at 1 index position (2nd) 
print(shopping) # 'lemon', 'chocolate', 'kiwis', "peas"

# Can only add 1 element at a time for .append() and .insert()
initials = ["RM", "LP"]
initials.append("LC") # adds "LC" to the end of the list
initials.insert(1, "LS") # adds "LS" at 1st index position (2nd spot)
print(initials) # "RM", "LS", "LP", "LC"


# To remove the last element in list, add list_name.pop()
todo = ["call mom", "dishes"]
todo.pop() #removes last element in list
print(todo) #call mom

# To remove a value AT SPECIFIC INDEX VALUE, add index to .pop()
todo = ["call mom", "dishes", "painting"]
todo.pop(1) #removes item at 1st index position (2nd item)
print(todo) # "call mom", "painting"

# Can store the removed value and print it
todo = ["call mom", "dishes", "painting"]
removed = todo.pop(0) # remove "call mom" and store assign it variable removed
print(removed) #prints "call mom"

# Organizing data
themes = ['classic', 'dark mode']
print(themes)

players = ['Federer', 'Murray']
print('Players for the match:')
print(players)

# Can include variables as elements in list
first = 'John'
second = 'Joseph'
third = 'Donnie'
winners = [first, second, third]
print(winners) # prints 'John', 'Joseph', 'Donnie'
print(winners[2]) #will print 'Donnie'


flavors = ['vanilla', 'chocolate', 'pistachio']
flavors[2] = 'strawberry'
print(flavors)


trading_values = [1,2]
trading_values.append(3) #adds 3 as the last element in list
print(trading_values) # 1,2,3

forecast = ['sunny', 'cloudy']
forecast.insert(0, 'windy') #will add 'windy' as first element in list
print(forecast) # 'windy', 'sunny', 'cloudy'


quiz_answers = [False, False, True, False]
print(quiz_answers) # False, False, True, False
quiz_answers.pop() # removes last item in list
print(quiz_answers) # False, False, True


# LOOPING OVER LISTS
# Use 'for' to loop over lists
# Console prints results vertically with no commas
# 1
# 2
final_scores = [17, 22, 34, 13]
for score in final_scores: # loop through using for & another variable name & :
    print(score) # prints 17,22,34,13


# The loop runs for as many elements as there are in the list

# The variable before 'in' holds value of the list element the loop is currently on
artists = ['Chagall', 'Lissitzky']
for artist in artists:
    print(artist) #prints 1st artist name, then prints 2nd artist name
    print("---") # prints ---, then prints again after 2nd artist name


student_grades = ['A', 'A-', 'C']
for grade in student_grades: 
    print(grade) # A A- C


singers = ['Bowie', 'Freddie']
for singer in singers:
    print(singer) # this should match the variable before in 
    print("is a legendary rocker")


consoles = ['Playstation', 'Xbox']
for console in consoles:
    print(console) # Playstation Xbox 


items = ['milk', 'tomato', 'apple']
for item in items:
    print(item) # milk tomato apple


supplies = ['pencil', 'book']
for value in supplies:
    print(value) # must be the same as variable before in - pencil book



# Can add or subtract from elements in list
data_points = [99, 99, 99, 99]
for data in data_points:
    print(data + 1) # adds 1 to each element in list = 100 100 100 100


minutes_worked = [123, 100, 99, 67]
for minutes in minutes_worked:
    print(minutes - 60) # subtracts 60 from each element in list = 63, 40, 39, 7


cubist_painters = ["Kahlo", "Chagall", "Dali"]
print("Below are some Cubist painters")
print(cubist_painters)