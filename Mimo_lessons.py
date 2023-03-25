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




