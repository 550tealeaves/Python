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


#SETTING/REMOVING INDEXES
# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

            # date     city        country  avg_temp_c
# 0     2000-01-01  Abidjan  Côte D'Ivoire      27.293
# 1     2000-02-01  Abidjan  Côte D'Ivoire      27.685
# 2     2000-03-01  Abidjan  Côte D'Ivoire      29.061
# 3     2000-04-01  Abidjan  Côte D'Ivoire      28.162
# 4     2000-05-01  Abidjan  Côte D'Ivoire      27.547
# ...          ...      ...            ...         ...
# 16495 2013-05-01     Xian          China      18.979
# 16496 2013-06-01     Xian          China      23.522
# 16497 2013-07-01     Xian          China      25.251
# 16498 2013-08-01     Xian          China      24.528
# 16499 2013-09-01     Xian          China         NaN

# [16500 rows x 4 columns]
#               date        country  avg_temp_c
# city                                         
# Abidjan 2000-01-01  Côte D'Ivoire      27.293
# Abidjan 2000-02-01  Côte D'Ivoire      27.685
# Abidjan 2000-03-01  Côte D'Ivoire      29.061
# Abidjan 2000-04-01  Côte D'Ivoire      28.162
# Abidjan 2000-05-01  Côte D'Ivoire      27.547
# ...            ...            ...         ...
# Xian    2013-05-01          China      18.979
# Xian    2013-06-01          China      23.522
# Xian    2013-07-01          China      25.251
# Xian    2013-08-01          China      24.528
# Xian    2013-09-01          China         NaN

# [16500 rows x 3 columns]
#           city       date        country  avg_temp_c
# 0      Abidjan 2000-01-01  Côte D'Ivoire      27.293
# 1      Abidjan 2000-02-01  Côte D'Ivoire      27.685
# 2      Abidjan 2000-03-01  Côte D'Ivoire      29.061
# 3      Abidjan 2000-04-01  Côte D'Ivoire      28.162
# 4      Abidjan 2000-05-01  Côte D'Ivoire      27.547
# ...        ...        ...            ...         ...
# 16495     Xian 2013-05-01          China      18.979
# 16496     Xian 2013-06-01          China      23.522
# 16497     Xian 2013-07-01          China      25.251
# 16498     Xian 2013-08-01          China      24.528
# 16499     Xian 2013-09-01          China         NaN

# [16500 rows x 4 columns]
#             date        country  avg_temp_c
# 0     2000-01-01  Côte D'Ivoire      27.293
# 1     2000-02-01  Côte D'Ivoire      27.685
# 2     2000-03-01  Côte D'Ivoire      29.061
# 3     2000-04-01  Côte D'Ivoire      28.162
# 4     2000-05-01  Côte D'Ivoire      27.547
# ...          ...            ...         ...
# 16495 2013-05-01          China      18.979
# 16496 2013-06-01          China      23.522
# 16497 2013-07-01          China      25.251
# 16498 2013-08-01          China      24.528
# 16499 2013-09-01          China         NaN

# [16500 rows x 3 columns]


##SUBSETTING W/ LOC
# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])


#             date              city country  avg_temp_c
# 10725 2000-01-01            Moscow  Russia      -7.313
# 10726 2000-02-01            Moscow  Russia      -3.551
# 10727 2000-03-01            Moscow  Russia      -1.661
# 10728 2000-04-01            Moscow  Russia      10.096
# 10729 2000-05-01            Moscow  Russia      10.357
# ...          ...               ...     ...         ...
# 13360 2013-05-01  Saint Petersburg  Russia      12.355
# 13361 2013-06-01  Saint Petersburg  Russia      17.185
# 13362 2013-07-01  Saint Petersburg  Russia      17.234
# 13363 2013-08-01  Saint Petersburg  Russia      17.153
# 13364 2013-09-01  Saint Petersburg  Russia         NaN

# [330 rows x 4 columns]
#                        date country  avg_temp_c
# city                                           
# Moscow           2000-01-01  Russia      -7.313
# Moscow           2000-02-01  Russia      -3.551
# Moscow           2000-03-01  Russia      -1.661
# Moscow           2000-04-01  Russia      10.096
# Moscow           2000-05-01  Russia      10.357
# ...                     ...     ...         ...
# Saint Petersburg 2013-05-01  Russia      12.355
# Saint Petersburg 2013-06-01  Russia      17.185
# Saint Petersburg 2013-07-01  Russia      17.234
# Saint Petersburg 2013-08-01  Russia      17.153
# Saint Petersburg 2013-09-01  Russia         NaN

# [330 rows x 3 columns]



##SETTING MULTI-LEVEL INDEXES
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

#                               date  avg_temp_c
# country  city                                 
# Brazil   Rio De Janeiro 2000-01-01      25.974
#          Rio De Janeiro 2000-02-01      26.699
#          Rio De Janeiro 2000-03-01      26.270
#          Rio De Janeiro 2000-04-01      25.750
#          Rio De Janeiro 2000-05-01      24.356
# ...                            ...         ...
# Pakistan Lahore         2013-05-01      33.457
#          Lahore         2013-06-01      34.456
#          Lahore         2013-07-01      33.279
#          Lahore         2013-08-01      31.511
#          Lahore         2013-09-01         NaN

# [330 rows x 2 columns]


##SORTING BY INDEX VALUES
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending=[True, False]))

#                          date  avg_temp_c
# country     city                         
# Afghanistan Kabul  2000-01-01       3.326
#             Kabul  2000-02-01       3.454
#             Kabul  2000-03-01       9.612
#             Kabul  2000-04-01      17.925
#             Kabul  2000-05-01      24.658
# ...                       ...         ...
# Zimbabwe    Harare 2013-05-01      18.298
#             Harare 2013-06-01      17.020
#             Harare 2013-07-01      16.299
#             Harare 2013-08-01      19.232
#             Harare 2013-09-01         NaN

# [16500 rows x 2 columns]
#                             date  avg_temp_c
# country       city                          
# Côte D'Ivoire Abidjan 2000-01-01      27.293
#               Abidjan 2000-02-01      27.685
#               Abidjan 2000-03-01      29.061
#               Abidjan 2000-04-01      28.162
#               Abidjan 2000-05-01      27.547
# ...                          ...         ...
# China         Xian    2013-05-01      18.979
#               Xian    2013-06-01      23.522
#               Xian    2013-07-01      25.251
#               Xian    2013-08-01      24.528
#               Xian    2013-09-01         NaN

# [16500 rows x 2 columns]
#                          date  avg_temp_c
# country     city                         
# Afghanistan Kabul  2000-01-01       3.326
#             Kabul  2000-02-01       3.454
#             Kabul  2000-03-01       9.612
#             Kabul  2000-04-01      17.925
#             Kabul  2000-05-01      24.658
# ...                       ...         ...
# Zimbabwe    Harare 2013-05-01      18.298
#             Harare 2013-06-01      17.020
#             Harare 2013-07-01      16.299
#             Harare 2013-08-01      19.232
#             Harare 2013-09-01         NaN

# [16500 rows x 2 columns]
