# IF, ELIF, & ELSE statements 
# if and elif take conditions
# if (condition), elif (condition)
# else DOES NOT take a condition - it runs when if/elif are FALSE
hour = 9
if hour < 12:
    print("Good morning")
else:
    print("Good night")

hour = 10
if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")

hour = 15
if hour < 12:
    print("Good morning")
elif hour < 17: 
    print("Good afternoon")
else:  #ELSE runs when both if & elif conditions are FALSE
    print("Good night")

# can add as many elif statements as needed
hour = 20
if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
elif hour < 21:
    print("Good evening")
else: 
    print("Good night")

number = 6
if number < 5:
    print("Less than five")
elif number < 10:
    print("Less than 10")

score = 75
if score >= 90:
    print("You got an A!")
elif score >= 70:
    print("You passed")

score = 66
if score >= 90:
    print("You got an A!")
elif score >= 70:
    print("You passed")
else:
    print("Better luck next time")

topping = "pepperoni"
if topping == "pineapple":
    print("Request denied")
elif topping == "pepperoni":
    print("Request accepted")

 
topping = "vegetable"
if topping == "pineapple":
    print("Request denied")
elif topping == "pepperoni":
    print("Request accepted")
else:
    print("Could not process request.")

age = 90
if age <= 12:
    print("Where are your parents?")
elif age <= 16:
    print("You're too young to ride this ride.")
elif age < 100:
    print("Welcome!")



age = 17
has_permit = True

if age > 18:
    print("Can drive")

# run or skip code depending on 2 codes
age = 17
has_permit = True

# AND operator runs code if both conditions are TRUE 
if age > 16 and has_permit:  # if the age > 16 and has_permit is true, print can drive
    print("Can drive")

# AND operator will not run if 1 or more conditions is FALSE
age = 17 
had_permit = True

if age > 18 and has_permit == True: 
    print("Can drive")

# Add as many AND operators as you want
age = 17
has_permit = True
is_insured = True

if age > 16 and has_permit and is_insured: #if 17 and true and true print("can drive")
    print("Can drive")

year = 1998

if year > 1900 and year < 2020:
    print("valid entry")


# if subway defect and is sunny are TRUE And distance <= 2 miles, walk to work
subway_defect = True
is_sunny = True
distance = 2

if subway_defect and is_sunny and distance <= 2:  
    print("Walk to work")

# OR operator
# OR runs if at least 1 condition is TRUE
average_grade = "A"
final_score = 1400

if average_grade == "A" or final_score >= 1300:
    print("Certificate achieved")

# OR gets skipped if ALL conditions are FALSE
# when you run it, no results in console
average_grade = "B"
final_score = 1400

if average_grade == "A" or final_score >= 1500:
    print("Certificate achieved")

# OR running if at least 1 condition is true
average_grade = "A"
final_score = 1400

if average_grade == "A" or final_score >= 1500: # Code still runs b/c avg grade is True
    print("Certificate awarded!")

# Add as many OR conditions as you want
average_grade = "B"
final_score = 1400
won_competition = True

# avg grade & final score are FALSE but won competition is TRUE
if average_grade == "A" or final_score >= 1500 or won_competition: 
    print("Certificate given!")


is_summer = False
is_warm = True

if is_summer or is_warm:
    print("Go for a swim!")


is_weekend = False
on_vacation = True

if is_weekend or on_vacation:
    print("Go on a roadtrip")


# OR will not run b/c both coditions are FALSE
mobile_internet = False
wifi = False

if mobile_internet or wifi:
    print("Loading inbox...")


highest_score = 100
score = 70
level = 5

if score > highest_score or level == 5:
    print('You won!')


promote_article = False
views = 100
shares = 30
likes = 70

if views > 150 or shares >= 50 or likes >= 60:
    promote_article = True


# F STRING - can mix different data types in a statement
cocoa = 70
print(f"{cocoa}% cocoa") #prints out 70% cocoa

print(f'size: {750} x {1334} px') #prints 750 x 1334 px

print(f"{49}% of social media users are women") #prints 49% of sm users are women

print(f'{200} grams of flour and {3} sticks of butter')

# CAN USE F STRINGS TO INSERT VARIABLES 
percentage = 11.19
print(f'water is {percentage}% hydrogen') # water is 11.19% hydrogen 


version = 4
print(f'update to version {version}') # update to version 4


hydrogen = 11.19
oxygen = 88.81
# water is 11.19% hydrogen & 88.81% oxygen 
print(f'water is {hydrogen}% hydrogen and {oxygen}% oxygen') 

# CAN DO MATH OPERATIONS WITH VARIABLES IN F STRINGS
tries = 3
current_try = 1

print(f'{tries - current_try} tries left') # (3-1) = 2 tries left

bobcats = 3
coyotes = 1
print(f"the score is {bobcats} : {coyotes}") # the score is 3:1


#INSERT VARIABLES INTO F STRINGS
planet = "Jupiter"
moons = 70
rings = 4
print(f'{planet} has {moons} moons and {rings} rings') #Jupiter has 70 moons & 4 rings


#USE VARIABLES W/IN OTHER VARIABLES IN F-STRINGS
author = "Virginia Wolf"
description = f"a book by {author}"
print(f"A Room of one's own is {description}") # A room of one's own is a book by Virgina Wolf


# check is there is a duplicate - email has been used before
email = "johnsmith@gmail.com"
is_duplicate = True

if is_duplicate:
    print(f'{email} is already in use')

# is_morning will skip the code block b/c it's FALSE
is_morning = False
is_evening = True

if is_morning:
    print('Good morning, Alex!')



# LOOPS
# SELF-ASSIGNING OPERATORS
wallet = 3
print(wallet)

# Self-assignment - setting variable to its own value
wallet = wallet
print(wallet)

# B/c you can self-assign variables, you can increase/decrease variables set to #s
wallet = 3
wallet = wallet + 1
print(wallet) # answer is 4

# Self-assigning variables let you track changes over time
wallet = 3
wallet = wallet + 2 # answer is 5
wallet = wallet - 1 # answer is 4
print(wallet) #output = 4

# Self-assigning lets you track changes in strings too
name = "Account name: "
name = name + " Elton" #output = Account name: Elton
name = name + " John" #output = Account name: Elton John
print(name) #output = Account name: Elton John

name = "Joanne"
name = name + " Rowling"
print(name) #output = Joanne Rowling


cards = 3
cards = cards - 1
cards = cards + 4
print(cards) #output = 6

name = "Jennifer"
name = name + " Lopez"
print(name) #Jennifer Lopez

# Instead of re-writing variable name, can use += to add # to increase variable
sales = 5
sales += 1
print(sales) #output = 6

marbles = 6
marbles += 2 
print(marbles) #8

yards = 80
yards += 10
print(yards) # 90

# Use -= to decrease variable 
sales = 5
sales -= 3
print(sales) #output = 2

speed = 200
speed -= 1
print(speed) #199

account = 1000
account -= 200
print(account) #800


# WHILE LOOPS
# programs repeat same lines of code over tob build things

# How to repeat code?
# 1. Write the code over - time-consuming
print("and again")
print('and again')
print('and again')

# To build bigger programs/sites, repeat code lines using WHILE LOOP
while True:  #will repeat it ad-infinitum
    print('and again')


# WHILE LOOP repeats code block while condition is TRUE
# If while loop condition stays True = infinite loop 
# will not run if FALSE
while False:
    print('skip me')

# To stop a while loop, create a variable OUTSIDE of the loop
# set the same variable (inside same code block) to False to break the while loop

keep_going = True
while keep_going == True:
    print('once more')
    keep_going = False

keep_going = True
while keep_going == True:
    print('and again')

    keep_going = False
    
    print('one more time')

auto_pilot = False
while auto_pilot == True:
    print('Autopilot on: vroom!')
    auto_pilot = False