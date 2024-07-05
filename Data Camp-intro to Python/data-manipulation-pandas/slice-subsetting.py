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



#EXAMPLE 1
import pandas as pd
temperatures = pd.read_pickle("/usr/local/share/datasets/temperatures_no_unc.pkl")

temperatures_ind = temperatures.set_index(["country", "city"])
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])

    #                               date  avg_temp_c
    # country  city                                   
    # Pakistan Faisalabad       2000-01-01      12.792
    #          Faisalabad       2000-02-01      14.339
    #          Faisalabad       2000-03-01      20.309
    #          Faisalabad       2000-04-01      29.072
    #          Faisalabad       2000-05-01      34.845
    # ...                              ...         ...
    # Russia   Saint Petersburg 2013-05-01      12.355
    #          Saint Petersburg 2013-06-01      17.185
    #          Saint Petersburg 2013-07-01      17.234
    #          Saint Petersburg 2013-08-01      17.153
    #          Saint Petersburg 2013-09-01         NaN
    
    # [1155 rows x 2 columns]
    #                          date  avg_temp_c
    # country city                             
    # Mexico  Mexico     2000-01-01      12.694
    #         Mexico     2000-02-01      14.677
    #         Mexico     2000-03-01      17.376
    #         Mexico     2000-04-01      18.294
    #         Mexico     2000-05-01      18.562
    # ...                       ...         ...
    # Morocco Casablanca 2013-05-01      19.217
    #         Casablanca 2013-06-01      23.649
    #         Casablanca 2013-07-01      27.488
    #         Casablanca 2013-08-01      27.952
    #         Casablanca 2013-09-01         NaN
    
    # [330 rows x 2 columns]
    #                       date  avg_temp_c
    # country  city                         
    # Pakistan Lahore 2000-01-01      12.792
    #          Lahore 2000-02-01      14.339
    #          Lahore 2000-03-01      20.309
    #          Lahore 2000-04-01      29.072
    #          Lahore 2000-05-01      34.845
    # ...                    ...         ...
    # Russia   Moscow 2013-05-01      16.152
    #          Moscow 2013-06-01      18.718
    #          Moscow 2013-07-01      18.136
    #          Moscow 2013-08-01      17.485
    #          Moscow 2013-09-01         NaN
    
    # [660 rows x 2 columns]



##EXAMPLE 2
temperatures_ind = temperatures.set_index(["country", "city"])
temperatures_srt = temperatures_ind.sort_index()
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad"), "date":"avg_temp_c"])


#                        date  avg_temp_c
# country city                            
# India   Hyderabad 2000-01-01      23.779
#         Hyderabad 2000-02-01      25.826
#         Hyderabad 2000-03-01      28.821
#         Hyderabad 2000-04-01      32.698
#         Hyderabad 2000-05-01      32.438
# ...                      ...         ...
# Iraq    Baghdad   2013-05-01      28.673
#         Baghdad   2013-06-01      33.803
#         Baghdad   2013-07-01      36.392
#         Baghdad   2013-08-01      35.463
#         Baghdad   2013-09-01         NaN

# [2145 rows x 2 columns]
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
#                         date  avg_temp_c
# country city                            
# India   Hyderabad 2000-01-01      23.779
#         Hyderabad 2000-02-01      25.826
#         Hyderabad 2000-03-01      28.821
#         Hyderabad 2000-04-01      32.698
#         Hyderabad 2000-05-01      32.438
# ...                      ...         ...
# Iraq    Baghdad   2013-05-01      28.673
#         Baghdad   2013-06-01      33.803
#         Baghdad   2013-07-01      36.392
#         Baghdad   2013-08-01      35.463
#         Baghdad   2013-09-01         NaN

# [2145 rows x 2 columns]




##EXAMPLE 3
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])

            # date     city        country  avg_temp_c
# 120   2010-01-01  Abidjan  Côte D'Ivoire      28.270
# 121   2010-02-01  Abidjan  Côte D'Ivoire      29.262
# 122   2010-03-01  Abidjan  Côte D'Ivoire      29.596
# 123   2010-04-01  Abidjan  Côte D'Ivoire      29.068
# 124   2010-05-01  Abidjan  Côte D'Ivoire      28.258
# ...          ...      ...            ...         ...
# 16474 2011-08-01     Xian          China      23.069
# 16475 2011-09-01     Xian          China      16.775
# 16476 2011-10-01     Xian          China      12.587
# 16477 2011-11-01     Xian          China       7.543
# 16478 2011-12-01     Xian          China      -0.490

# [2400 rows x 4 columns]
#                   city    country  avg_temp_c
# date                                         
# 2010-01-01  Faisalabad   Pakistan      11.810
# 2010-01-01   Melbourne  Australia      20.016
# 2010-01-01   Chongqing      China       7.921
# 2010-01-01   São Paulo     Brazil      23.738
# 2010-01-01   Guangzhou      China      14.136
# ...                ...        ...         ...
# 2011-12-01      Nagoya      Japan       6.476
# 2011-12-01   Hyderabad      India      23.613
# 2011-12-01        Cali   Colombia      21.559
# 2011-12-01        Lima       Peru      18.293
# 2011-12-01     Bangkok   Thailand      25.021

# [2400 rows x 3 columns]
#                 city        country  avg_temp_c
# date                                           
# 2010-08-01  Calcutta          India      30.226
# 2010-08-01      Pune          India      24.941
# 2010-08-01     Izmir         Turkey      28.352
# 2010-08-01   Tianjin          China      25.543
# 2010-08-01    Manila    Philippines      27.101
# ...              ...            ...         ...
# 2011-02-01     Kabul    Afghanistan       3.914
# 2011-02-01   Chicago  United States       0.276
# 2011-02-01    Aleppo          Syria       8.246
# 2011-02-01     Delhi          India      18.136
# 2011-02-01   Rangoon          Burma      26.631

# [700 rows x 3 columns]


##EXAMPLE 4 - SUBSET BY ROW/COL #
# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22, 1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])


# Abidjan
#         date     city        country  avg_temp_c
# 0 2000-01-01  Abidjan  Côte D'Ivoire      27.293
# 1 2000-02-01  Abidjan  Côte D'Ivoire      27.685
# 2 2000-03-01  Abidjan  Côte D'Ivoire      29.061
# 3 2000-04-01  Abidjan  Côte D'Ivoire      28.162
# 4 2000-05-01  Abidjan  Côte D'Ivoire      27.547
#              country  avg_temp_c
# 0      Côte D'Ivoire      27.293
# 1      Côte D'Ivoire      27.685
# 2      Côte D'Ivoire      29.061
# 3      Côte D'Ivoire      28.162
# 4      Côte D'Ivoire      27.547
# ...              ...         ...
# 16495          China      18.979
# 16496          China      23.522
# 16497          China      25.251
# 16498          China      24.528
# 16499          China         NaN

# [16500 rows x 2 columns]
#          country  avg_temp_c
# 0  Côte D'Ivoire      27.293
# 1  Côte D'Ivoire      27.685
# 2  Côte D'Ivoire      29.061
# 3  Côte D'Ivoire      28.162
# 4  Côte D'Ivoire      27.547