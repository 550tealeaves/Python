# ****FUNCTIONS****
# - reusable code that performs specific task

#Python has several built-in functions

#MAX()
#Ex: find max value in a list
fam = [1.73, 1.68, 1.71, 1.89]
max(fam) #1.89
#function max works like a black box - passed it a list of values, then the implementation of max() that we don't know produces an output

#Can assign result of a function call to a new variable
tallest = max(fam)
print(tallest) #1.89

#ROUND()
# takes 2 inputs (# for rounding, & precision (# decimals))
round(1.68, 1) #1.7
round(1.685545856, 6) #1.685546

#Can use round w/o precision input - will round to nearest integer
round(6.784324757574) #7


#HELP()
#Provides explanation on functions
help(round) # round(number, ndigits=None)
    # Round a number to a given precision in decimal digits.
    # The return value is an integer if ndigits is omitted or None.  Otherwise
    # the return value has the same type as the number.  ndigits may be negative.

help(max) #max(...)
#     max(iterable, *[, default=obj, key=func]) -> value
#     max(arg1, arg2, *args, *[, key=func]) -> value
#     With a single iterable argument, return its biggest item. The
#     default keyword-only argument specifies an object to return if
#     the provided iterable is empty.
#     With two or more arguments, return the largest argument.

# ALTERNATIVE TO help() is ?function - which doesn't work in VS code but does work in data camp's Python editor


# Exercises
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1)) # class 'list'

# Print out length of var1
print(len(var1)) # 4

# Convert var2 to an integer: out2
out2 = int(var2) 


help(sorted) #sorted(iterable, /, *, key=None, reverse=False)
    # Return a new list containing all items from the iterable in ascending order.        
    # A custom key function can be supplied to customize the sort order, and the
    # reverse flag can be set to request the result in descending order.
    #BY DEFAULT, key=None & reverse=False


# SORTED()
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second
print(full) # [11.25, 18.0, 20.0, 10.75, 9.5]

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted) #[20.0, 18.0, 11.25, 10.75, 9.5]
