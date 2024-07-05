# SLICING LISTS

# 	• Breeds is a list
# 	• Slice list by putting the indexes for the first and last positions, separated by :
# 		○ Last position is exclusive
# 		○ Breeds[2:5]
# 			§ Chow chow, Schnauzer, Labrador
# 			§ Indexes 2, 3, 4
# 		○ To start slice from the beginning (index=0), leave first index blank and only add the end
# 			§ Breeds[:3]
# 				□ Labrador, Poodle, Chow Chow
# 		○ To return the whole list, don't add any indexes - just include the :
# 			§ Breeds[:]
# 				□ Returns whole list


# SLICING DATAFRAMES
# 	• Have to first sort the index of the dataframe before slicing it


	
# Slice outer level index 

# 	• To slice rows at the outer level of the index, use loc and pass the 1st/last values separately
# 		○ Unlike lists, this includes the last value

# Slice inner index level

# 	• Above technique DOES NOT work for inner level of the index
# 		○ Returns empty dataframe
# 	• To slice inner index level = pass the first and last positions as tuples
# 		○ Dogs_srt.loc[("Labrador, "Brown"):("Schnauzer", "Gray")]
# 			§ First position = tuple of Labrador & Brown
# 			§ Last position = tuple of Schnauzer & Gray



# Slice columns in dataframe

# 	• Because dataframes = 2D objects, can slice columns
# 		○ Pass 2 arguments to loc
# 			§ If you want to subset columns but keep all rows then
# 				□ ":" = first argument
# 				□ Column names as 1st/last positions to slice on 


# Slice on rows and columns of dataframe
# 	• Pass correct slice as  arguments
# 		○ For rows - pass the 1st/last positions as tuples, separated by :
# 		○ For cols - pass the cols that you want 

# Use of slices
# 	• Subset dataframes by range of dates
# 		○ Ex: set date of birth col as index and then sort 
# 		○ Slice dates with same syntax 
# 	• Can slice by partial dates
# 		○ Can opt to include Y-M-D parts or combination - Y-M, M-D, M, D, Y only
# 		○ Ex: dogs.loc["2014":"2016"]
# 			§ Will output all dates in 2014, 2015, & 2016
			

# Subset by row/col #
# 	• Like list slicing where the end # is NOT included
# 	• Rows - 5th row is not included
# 	• Col - 4th col is not included


breeds = ["Labrador", "Poodle", "Chow Chow", "Schnauzer", "Labrador", "Chihuahua", "St. Bernard"]

breeds[2:5] #['Chow Chow', 'Schnauzer', 'Labrador']
#last index is always excluded


breeds[:3] #['Labrador', 'Poodle', 'Chow Chow']

breeds[:] #returns all items



##SLICE DATA FRAME - 1ST SORT INDEX, THEN SLICE
import pandas as pd

dogs = pd.read_csv("Data Camp-intro to Python/data-manipulation-pandas/dogs.csv", index_col=0)

dogs.head()

dogs_srt = dogs.set_index(["breed", "color"]).sort_index()
print(dogs_srt)

#                       name  height_cm  weight_kg date_of_birth  
# breed       color
# Chihuahua   Tan     Stella         18          2     4/20/2015  
# Chow Chow   Brown     Lucy         46         24     8/25/2014  
# Labrador    Black      Max         59         29     1/20/2017  
#             Brown    Bella         56         24      7/1/2013  
# Poodle      Black  Charlie         43         24     9/16/2016  
# Schnauzer   Gray    Cooper         49         17    12/11/2011  
# St. Bernard White   Bernie         77         74     2/27/2018 



#SLICE OUTER INDEX LEVEL - USE .LOC & PASS 1ST/LAST VALUES SEPARATELY - WILL INCLUDE THE LAST INDEX, UNLIKE LIST SLICING
dogs_srt.loc["Chow Chow": "Poodle"] #shows all rows from Chow CHow to Poodle

# breed     color
# Chow Chow Brown     Lucy         46         24     8/25/2014    
# Labrador  Black      Max         59         29     1/20/2017    
#           Brown    Bella         56         24      7/1/2013    
# Poodle    Black  Charlie         43         24     9/16/2016   


#SLICE INNER INDEX LEVEL - PASS 1ST/LAST POSITIONS AS TUPLES
dogs_srt.loc["Tan": "Grey"] #DOES NOT WORK

dogs_srt.loc[("Labrador", "Brown"):("Schnauzer", "Grey")] #tuples

#                    name  height_cm  weight_kg date_of_birth
# breed     color
# Labrador  Brown    Bella         56         24      7/1/2013    
# Poodle    Black  Charlie         43         24     9/16/2016    
# Schnauzer Gray    Cooper         49         17    12/11/2011


#SLICE COLUMNS IN DATAFRAME - PASS 2 ARGUMENTS TO LOC [:, "start_col": "end_col"]
dogs_srt.loc[:, "name": "height_cm"] #returns all the rows for name & height_cm col

#                       name  height_cm
# breed       color
# Chihuahua   Tan     Stella         18
# Chow Chow   Brown     Lucy         46
# Labrador    Black      Max         59
#             Brown    Bella         56
# Poodle      Black  Charlie         43
# Schnauzer   Gray    Cooper         49
# St. Bernard White   Bernie         77



#SLICE ON ROWS & COLS OF DATAFRAME - FOR ROWS, PASS 1ST/LAST TUPLES & FOR COLS, PASS COLS YOU WANT TO KEEP
#tuples must be wrapped in (), but cols don't need that
dogs_srt.loc[("Labrador", "Brown"): ("Schnauzer", "Grey"), "name":"height_cm"] #returns Lab, brown to Schnauzer, grey rows & includes name & hegiht_cm col

#                    name  height_cm
# breed     color
# Labrador  Brown    Bella         56
# Poodle    Black  Charlie         43
# Schnauzer Gray    Cooper         49


#SLICES OFTEN USED TO SUBSET RANGE OF DATES
#1ST SORT INDEX
dogs = dogs.set_index("date_of_birth").sort_index()
print(dogs)

#                   name        breed  ... height_cm  weight_kg
# date_of_birth                        ...
# 1/20/2017          Max     Labrador  ...        59         29   
# 12/11/2011      Cooper    Schnauzer  ...        49         17   
# 2/27/2018       Bernie  St. Bernard  ...        77         74   
# 4/20/2015       Stella    Chihuahua  ...        18          2   
# 7/1/2013         Bella     Labrador  ...        56         24   
# 8/25/2014         Lucy    Chow Chow  ...        46         24   
# 9/16/2016      Charlie       Poodle  ...        43         24 


#CAN ALSO SLICE USING PARTIAL DATES
#Get dogs w/ DOB b/w 2014 and 2016
dogs.loc["2014:2016"] #doesn't work well b/c dates are not in Y-M-D format


#SUBSETTING BY ROW/COL #S - USE .ILOC
print(dogs.iloc[2:5, 1:4]) #like list subset - row 5, col 4 excluded

#                      breed  color  height_cm
# date_of_birth
# 2/27/2018      St. Bernard  White         77
# 4/20/2015        Chihuahua    Tan         18
# 7/1/2013          Labrador  Brown         56