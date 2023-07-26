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
    print("Go on a road trip")


# OR will not run b/c both conditions are FALSE
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
print(f"A Room of one's own is {description}") # A room of one's own is a book by Virginia Wolf


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

# += also works to join strings
title = "Dr."
title += " Jane Doe"
print(title) # prints Dr. Jane Doe

title1 = "Dr."
title1 = title1 + " Jane Doe"
print(title1) # second way to join strings - prints Dr. Jane Doe

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


# CONTROLLING WHILE LOOPS
# 1. Start w/ variable set to # = "counter variable"
# Counter variable counts # times loop repeats 

counter = 1

# 2. Use comparison in the condition to compare counter variable to a #
counter = 1

while counter < 4:

# 3. Inside code block, make condition return FALSE & stop loop by incrementing counter variable
# increases counter by 1 each time loop runs code block 
counter = 1

while counter < 4:  # will print out "1" 3x
    print(counter)
    counter += 1  #output = 123 b/c counter increments by 1 and stops loop

counter = 1

while counter < 10: # will print out "1" 9x
    print(counter) #if you stop here, repeats 1 ad-infinitum
    counter += 1 #output = 1-9 b/c counter increments by 1 - stops loop

# Changing counter variable's value changes WHEN loop starts
counter = 5 

while counter < 10: # will start at "5" and repeat it 5 more times
    print(counter) #if you stop here - it will repeat 5 ad-infinitum
    counter += 1 #output = 5,6,7,8,9 b/c it increments and stops at 10

# Code order affects what console shows
# place counter += 1 first to show 6-10
counter = 5 # counter starts at 5

while counter < 10:
    counter += 1
    print(counter) #output = 6,7,8,9,10 - stops at 10

counter = 1

while counter < 5:
    print(counter)
    counter += 1 #output = 1,2,3,4 - stops at 4
 
speed = 2  # counter variable starts at 2

while speed < 5:
    print(speed)
    speed += 1 #output = 2,3,4 - stops at 4

# Use counter variable to control loops w/ strings 
list_number = 1 #counter starts at 1

while list_number < 11:
    print('Add entry...') # will output "Add entry"
    list_number += 1 # stops Add entry... after 10 repeats

releases = 1 #counter starts at 1
while releases < 8:
    print(releases)
    releases += 1 #output = 1,2,3,4,5,6,7 - stops at 7


# if counter increment is BEFORE print function - output shows the end # & omits starting
# counter = 3 - while counter <8 = results 4,5,6,7,8 (includes 8, excludes 3)
counter = 3 #counter starts at 3

while counter < 8:
    counter += 1
    print(counter) #output = 4,5,6,7,8 - stops at 8


# if counter increment is AFTER print function - output includes starting # & omits ending - counter = 3, while counter < 8 - output = 3,4,5,6,7 (includes 3, omits 8)
counter = 3 #counter starts at 3

while counter < 8:
    print(counter) 
    counter += 1 #output = 3,4,5,6,7 - stops at 7

# Show picture of flag
first_counter = 0

while first_counter < 5:
    print('**********---------')
    first_counter += 1

second_counter = 0

while second_counter < 4:
    print('------------------')
    second_counter += 1


# FOR LOOPS
# Use for loops to write programs w/ less code 
# Use for i (variable) in range():
for i in range(4): # for in this loop repeat below 4x
    print("**********---------")
for i in range(4): # for in this loop repeat below 4x
    print("------------------")


for i in range(5):
    print('Happy birthday to you!') #will repeat statement 5x


# add # inside range, like 6, = loop over code block 6x, from 0-5
for i in range(6):
    print(i) #output = 0,1,2,3,4,5 (6x)

# variable "i" = counter variable - counts what repetition of loop we're in
for i in range(3):
    print(i) #output = 0,1,2
    print('For loops are great!') #prints string 3x


for i in range(2): # i = counter variable - 0,1
    print('We will') # prints string 2x
print('Rock you!') #outside code block - EXCLUDED from for loop - runs 1x


print('Everybody wants to') #prints 1x b/c not attached to loop

for i in range(3): #counter variable = 0,1,2
    print('be like me') # print string 3x


for i in range(2):
    print('Accessing GDP values')


for x in range(5): # x = counter variable - 0,1,2,3,4
    print("Round:") # prints Round: 5x
    print(x) #prints 0,1,2,3,4


for i in range(3): #i = cv - 0,1,2
    print('Adding entries...') # prints string 3x
print('All entries added') #outside code block = runs 1x only

# inside for loop's code block, add ~ to the line variable by using the += operator
print("*")
line = ""
for i in range(4):
    line += "~"
    print(line) # prints 1 line ~, 2nd line ~~, 3rd line ~~~, 4th = ~~~~


# counter variable can be named "counter", "i", or anything else
print ("Zero to four:")
for repetition in range(5): # counter var = repetition
    print(repetition) # prints 0,1,2,3,4 (5 #s)

for i in range(3):
    print("Polly wants a cracker!") #will print statement 3x 


year = 2020
while year <= 2025: #year = counter var
    print(f"It's {year}") # prints statement but with increase year
    year += 1 #will print out It's 2020, "" 2021, "" 2022, "" 2023, "" 2024, "" 2025


year = 2025
while year <= 2100:
    print(f"It's {year}")
    year += 5 # prints all years in 5-yr increments from 2025 to 2100 w/ statement

# have to know what outputs will be
i = 0  # i assigned value of 0
while i < 10: # value of i will always be less than 10
    i += 1 # i reassigned to 0 (initial assignment) + 1  = 0+1 = 1
    print(i) # prints 1-10

i = 0  # i assigned value of 0
while i < 10:  # value of i will always be less than 10
    print(i)
    break

for i in range(3):
    print("Polly wants a cracker!")  # will print statement 3x

counter = 1
while counter < 5:
    counter +=1
    print(counter)
