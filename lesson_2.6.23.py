1+1
2**4
True
type(False)
2**5
type("hello world")
type('hola mundo')
type(1.5)
type(65)
type("arrow")
type(["coffe", "yogurt", "oatmeal"])
type([1,5,7,8])
type([1, "bananas", 7, "eight"])
my_variable = "hello"
my_variable.upper() 
'any string'.upper()
'RANDOM STRING'.lower()
'nastasia'.upper()
classes = ['intro to python', 'edu tech', 'data viz', 'digital story']
classes.append('env tech')
classes
classes.remove('data viz')
classes
for drama in "entourage":
    print(drama)



#BOOLEANS
#can generate True/False by setting variables = to a negated variable
open_slot = True
is_available = not open_slot
print(is_available) #False

is_even = not False
print(is_even) #True


flight_mode = True
update = not flight_mode
print(update) #False 


flight_mode = True
updating = not flight_mode #False
use_apps = not updating #True
print(use_apps) #True


#Using != to check if variables are different
num_1 = 17
num_2 = 23
print(num_1 != num_2) #True


tries_left = 1
game_over = tries_left == 0
print("Game over:") #Game over:
print(game_over) #False


player_1 = 0
player_2 = 10
player_1 = 10 #reassigns new value to existing variable

same_score = player_1 == player_2 #see if variables are equal to each other

print("It's a tie:") #It's a tie
print(same_score) #True


#Can reassign a value to itself
downloaded = 9
downloaded = downloaded + 1
print(downloaded) #10

in_progress = downloaded != 10  #downloaded doesn't equal 10

print("Download finished:")
print(in_progress) #False b/c 10 is equal to 10


#Data types
first = 0
second = 0
print(first >= second) #True



paid = 5
price = 2
give_change = paid > price #5>2 
print(give_change) #True


characters = 134
limit_reached = characters >= 250   #134 >=250
print('Character limit reached:')
print(limit_reached) #False


value = 90
minimum = 100
give_discount = value >= minimum #90 >= 100
print("Give discount:")
print(give_discount) #False


capacity = 1000
emails = 157
full = emails >= capacity # 157 >= 1000
print("Inbox full")
print(full) #False

product_id = '37'
print(type(product_id)) #string


# F-strings - use to mix strings and numbers together
ingredient = "sugar"
quantity = 100
print(f'Add {quantity} grams of {ingredient}') #Add 100 grams of sugar


task = "dishes"
print(f'todo: {task}')


requests = 2
print(f'{requests} new friend requests') #2 new friend requests


# 2 ways to print the same statement 
name = "Joshua"
print("Hello, " + name + "!") #Hello, Joshua!
print(f'Hello, {name}!') #Hello, Joshua


#Can use F-string to insert number 
min_age = 18
max_age = 28
print(f'{88}% of social media users are between {min_age} and {max_age} years old')


print(f'Mexico was the leading avocado producer in {2018}')


first = 'English'
second = 'Mandarin Chinese'
third = 'Hindi'
print(f'Most spoken languages: {first}, {second}, {third}.') #Most spoken languages: English, Mandarin Chinese, Hindi



hours = 14
minutes = 45
destination = "Paris"

print(f'Your flight to {destination} will depart at {hours}:{minutes}.') #Your flight to Paris will depart at 14:45. 


#Can save f string into a variable - don't need ()
percentage = 11.19 #float
fact = f'water is {percentage}% hydrogen' 
print(fact)  # water is 11.19% hydrogen


#Those < 17 cannot drive 
sams_age = 16
too_young = sams_age < 17 #compare sams_age (16) to too_young (17)
car_driver = sams_age == 17 #does 16 equal 17

print(f'Is Sam too young to drive?') 
print(f'Can Sam drive a car? {car_driver}') #False



#Compare passwords to see if they are the same
old_password = 'hello123'
new_password = 'goodbye321'
compare_old_new = old_password != new_password #compare if hello123 is NOT equal to goodbye 321 - True
repeat_new_password = 'goodbye321'
compare_new = new_password == repeat_new_password #are values in new_password & repeat_new password variables the same - True 

print(f'Is new password different from old password? {compare_old_new}') #True
print(f'Has new password been introduced correctly? {compare_new}') #True


#Does the person need to buy an adult ticket? 
age = 15
adult_ticket = age >= 12  #15 >= 12
print(f'Buy one adult ticket: {adult_ticket}') #True


