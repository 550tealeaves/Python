##STRINGS AND TEXT##
# Use .format() syntax to apply format to already created string
types_of_people = 10 #store 10 in variable types_of_people
x = f"There are {types_of_people} types of people."  #include types of people w/in {} in the F string

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f'I said: {x}')
print(f"Manuel replied, after being questioned by the administrator, '{x}' The administrator, a corrugated frown on his face looked incredulous at the reply. 'Who are these people?' he demanded. Swallowing the lump in his throat, Manuel cautiously replied, '{y}' I did not invite them.")
print(f"Additionally, I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of "
e = "a string with a right side."

print(w+e)



##MORE PRINTING##
print("Mary had a little lamb.")
print("It's fleece was white as {}." .format('snow'))
print("And everywhere that Mary went.")
print("."*25) #prints period 25 times


# Creating a word using variables
end1 = "C"
end2 = "h"
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# print variables in particular order to spell mystery phrase
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') #prints Cheese
# if no end='  ' then it will print the next line as a next line so Cheese (1 line) and then Burger (2nd line)
# but with end=' ' it adds a space between Cheese & Burger
print(end7 + end8 + end9 + end10 + end11 + end12) # prints Burger



##PRINTING PRINTING
formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter)) # will print 16 {}
print(formatter.format(
    "Try your",
    "Own text here",
    "Perhaps a poem",
    "Or a song about trepidation"
))



##PRINTING, PRINTING, PRINTING##
# assign days of the week to a variable - these will all print out on the same line
days = "Mon Tue Wed Thu Fri Sat Sun"
# assign some months to a variable
# the \n puts the next text on new line - so each month will appear as its own line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print("Here are the days: ", days)
print("here are the months: ", months)

print("""
There's something devious going on here.
With the 3 double-quotes.
We'll be able to type as much as our heart desires.
Even 4 lines if we want, or 5, or 6.
""")



##ESCAPE QUOTES SEQUENCE##

#2 ways create string that goes across multiple lines
# (1) \n puts new line character into the string

#ESCAPE SEQUENCE
# Use \ to escape single/double quotes - see height example

# (2)Triple quotes """ - cna write as many lines in between

height = "I am 6'2\" tall." # \ helps escape double-quote in string
height2 = 'I am 6\'2" tall.' # \ helps escape single-quotes in string

print(f"Using double quotes, this is my height: {height}")
print(f'Using single quotes, this is my height: {height2}')

# \t creates horizontal tab
tabby_cat = "\tI'm tabbed in"
# \n to split string into 2 lines
persian_cat = "I'm split\non a line."
# \\ adds backslash to string
backslash_cat = "I'm \\ a \\ feral \\ dog \\ looking \\ to \\ eat \\ your \\ cat."

# Use """ to write multiple lines in string
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fish treatos
\t* Catnip\n\t* Grass
"""

lard_cat = "Regardless of his shame, he squeaked, \"Could we get some Friskies?"
lard_cat2 = "Regardless of his shame, he squeaked, \"Could we get some Friskies?\""
lard_cat3 = "Regardless of his shame, he squeaked, \'Could we get some Friskies?"

print(tabby_cat)
print(persian_cat)
print(fat_cat)
print(lard_cat)
print(lard_cat2)
print(lard_cat3)




##ASKING QUESTIONS##
# Most software will receive an input, change it, and prints output to show changes.


# input() brings textbox for you to response - after you respond, it will print those answers next to the question
print("How old are you?", end =' ') # end=' ' tells print to not end the line w/ a new line character & go to the next line
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()


##PROMPTING PEOPLE##
# You can use input() to put in propmt to indicate what person should type by placing a string inside

# Prompts user with "Name?" and assigns result into variable y
# Used to ask question and get answer
y = input("Name? ")

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you are {age} years old, {height} tall, and {weight}lbs heavy")



## FUNCTIONS AND VARIABLES ##
# Variables in function are not connected to the variables in the script

# Define the function (cheese_and_crackers) and its 2 arguments - cheese_count & boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f'You have {cheese_count} cheeses!')
  print(f'You have {boxes_of_crackers} boxes of crackers!')
  print("Man, that's enough for a party!")
  print("Get a blanket.\n") # will print this on a new line

# 4 ways to pass values into function cheese_and_crackers

# (1) pass in numbers
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30) # pass 20,30 into the place of cheese_count & boxes_of_crackers

# (2) pass in variables
print("OR, we may utilize the variables from the script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # pass these 2 variables (10 & 50) as arguments into cheese_and_crackers function

# (3) pass in math equation
print("we can even do math inside too:")
cheese_and_crackers(10 - 27, 5 + 6) # can pass the arguments as 2 separate math equation

# (4) pass in combo of math and variables
print('Additionally, we can combine the two, variables and math:')
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)