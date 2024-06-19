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