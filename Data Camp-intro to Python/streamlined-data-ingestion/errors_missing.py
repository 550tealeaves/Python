# Col flat file import issues 

# Values  



# Specifying data types 

# Pandas automatically infers col data type 

# Use .dtypes() to see data types in columns 

  

# Dtype 

# Takes a dictionary 

# Each key = col name 

# Each value = data type col should be  

# Must be passed in "" 

  

# Customizing missing data values 

# Pandas may automatically interpret missing values as NA 

# Can also use dummy codes to represent missing values 

# Use na_values argument to set custom missing values 

# Accepts  

# Single value 

# List  

# Dictionary of cols & values   

# Any zipcode that has 0 will be treated as missing data 



# Lines with errors 

# Can have an error trying to load file 

# 2 arguments to fix this 

# Error= booelan 

# Set error_bad_lines = False  

# Skips unparseable records 

# Set war_bad_lines=True 

# See msgs when records skipped 

 

 

 


 