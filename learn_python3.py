#Variable names - use _this_variable_name = underscore character. It adds imaginary spaces b/w words in variable name
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers  #100-30=70
cars_driven = drivers  #30
carpool_capacity = cars_driven * space_in_a_car  #30*4=120
average_passengers_per_car = passengers / cars_driven  #90/30 = 3

# insert the variables in the sentence - don't need brackets b/c not formatted string
print('There are', cars, 'cars available.') #100
print("There are only", drivers, "drivers available.") #30
print("There will be", cars_not_driven, "empty cars today.") #70
print("We can transport", carpool_capacity, "people today.") #120
print("We have", passengers, "to carpool today.") #90
print("We need to put about", average_passengers_per_car, "in each car.") #3.0


#FORMATTED STRING
#embed variables inside a string using {} sequence. Must begin string w/ "f" for format

my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = "Brown"

print(f"Let's talk about {my_name}.") #Let's talk about Zed A. Shaw
print(f"He's {my_height} inches tall.") #He's 74in tall
print(f"He's {my_weight} pounds.") #He's 180lbs
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.") #He's got blue eyes & brown hair
print(f"His teeth are usually {my_teeth} depending on the coffee.") #His teeth are usually white depending on the coffee

#Add multiple variables 
total = my_age + my_height + my_weight
print(f'If I add {my_age}, {my_height}, and {my_weight}, I get {total}') #If I add 35+74+180, I get 289
