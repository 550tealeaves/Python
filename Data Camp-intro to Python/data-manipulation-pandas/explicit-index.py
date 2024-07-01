# 	• DataFrames have 3 parts
# 		○ NumPy array for data
# 		○ Index for columns
# 		○ Index for rows 

# 	• .columns
# 		○ Has index object of col names
# 	• .index
# 		○ Has index object of row #s
# Setting an index 
# 	• Moves col from dataframe body to the index  
# 	• Use .set_index() method

# 	• Output changes - name is now part of index 
# 	• Index values are left aligned
# 	• Col values are right aligned 



# Removing an index
# 	• Use .reset_index() method
# 	• Undos action 
# 	• In example, name returns back to columns
# Dropping index
# 	• .reset_index() method has drop argument (drop=True)
# 		○ Will discard index
# 	• In example - the name col/contents is gone
# Indexes are necessary b/c they make subsetting code cleaner
# 	• .loc is a subsetting method for DataFrames 
# 		○ Filters on index values
# 		○ Below examples, to subset to specific names, pass the list of names to the .loc
# 	• Index values don't have to be unique
# 	• Subsetting on loc and selecting labrador returns the labrador rows




# Multi-level indexes aka hierarchical indexes
# 	• Can include mult cols in index by passing them as a list to .set_index() method 
# 	• Below example - pass in breed & color
# 		○ Now they are moved to index position 
# Implication that inner level index (color) nested w/in outer level index (breed) 
# Subset outer level w/ list
# 	• To take subset of rows in outer level index = pass list of index value to .loc
# 	• Below example - passed in 2 breeds
# 		○ Output has all dogs from both the breeds
# 			§ 2 labs, 1 chihuahua

# Subset on inner level w/ list of tuples
# 	• Pass list of tuples to subset on inner level index
# 	• Below ex
# 		○ 1st tuple = specifies Lab (outer) & Brown (inner)
# 		○ 2nd tuple = specifies Chihuahua (outer) & Tan (inner)
# 	• Rows must match all the conditions set 
# 		○ Ex: black lab not returned
# Sort by index values
# 	• Use .sort_index() method 
# Default sorts all next levels from outer to inner in ascending order
# Controlling sort_index
# 	• Pass lists to the level & ascending arguments of .sort_index() method to control the sorting
# 	• Below ex: will sort color ascending order and breed in descending order
# Cons
# 	• Index values are data 
# 		○ So storing data in diff forms makes it harder to conceptualize
# 	• Index violates tidy data principles
# 		○ Data should be stored as tabular
# 		○ Index values don't have their own column = violation
# 	• Must learn 2 syntaxes
# 		○ Diff syntaxes for cols & indexes
# 		○ Complicated code = errors
