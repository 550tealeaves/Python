	# • Dictionaries is a python type
	# • For example, need to track world population
	# 	○ You can create 2 lists, one with the population and the other w/ the countries
	# 	○ Would be very time consuming for large lists to find the correct indices
	# • Dictionaries let you connect the country to the pop w/o finding index
	# • To create dictionary
	# 	○ Use {}
	# 	○ Add key: value pairs inside
	# 	○ To access the population for a country, pass the key into the dictionary and it will extract the value


## EXAMPLE
#store the key value pairs in dictionary called world
world = {
    "afghanistan": 30.55,
    "albania": 2.77,
    "algeria": 39.21
}
world["algeria"] #39.21



## EXERCISE 1 - MOTIVATION FOR DICTIONARIES
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger]) #berlin




## EXERCISE 2 - CREATE DICTIONARY
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid','france':'paris', 'germany': 'berlin', 'norway': 'oslo'}

# Print europe
print(europe)





## EXERCISE 3 - ACCESS DICTIONARY
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out the values in europe
print(europe.values())

# Print out value that belongs to key 'norway'
print(europe['norway'])


##DICTIONARIES PART 2
# 	• Keys should be immutable objects
# 		○ Stings, floats, booleans are immutable
# 		○ But lists are mutable = can change the contents
	
	
	
# Principality of Sealand
# 	• To add the country of Sealand and it's population to the world dictionary that was already created, 
# 		○ World['sealand'] = 0.000027
# 	• If you call world, sealand will be included 
# 	• Can also check using a boolean 


	# • To update a value within the dictionary, 
	# 	○ Each key in dictionary is unique, so Python knows that you are updating the value instead of replacing the key 
	# 	○ World['sealand'] = 0.000028
	# • To remove a key/value pair in the dictionary, use del
	# 	○ Del(world['sealand'])
	# 		§ Will remove sealand & corresponding value
	# 	○ Print(world)
	# 		§ Sealand is gone

## EXAMPLE
world['sealand'] = 0.00027

#check to see that new key/value pair added
world #adds sealand & value to the dictionary

#can also check if key is in dictionary using boolean
"sealand" in world # TRUE

#Update the value of the key, "sealand"
world['sealand'] = 0.0045
world

#Delete a key value pair
del(world['sealand'])
world #removes sealand as key/value pair




##EXERCISE 1 - ADDING MORE KEY/VALUE PAIRS
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)








## EXERCISE 2 - DICTIONARY MANIPULATION
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)








## EXERCISE 3 - DICTIONARICEPTION
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)