	# • Dictionaries
	# 	○ Way to store data
	# 	○ Holds set of key values pairs
	# 	○ Use {} to create them
	# 	○ Can extract values using []


	# • Several ways to create dataframe - 2 below
	# 	○ From list of dictionaries
	# 		§ Built row by row
	# 	○ From dictionary of lists
	# 		§ Built column by column


	# • Dictionary contains list (on left of col = col name, on right = values



	# • In example, 1st col = "name"
	# • Value = list w/ the actual names
	# 	○ ["Ginger", "Scout"]
		
		

	# • Then pass it into pd.dataframe



##EXERCISE 1
import pandas as pd
# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)


#          date  small_sold  large_sold
# 0  2019-11-03    10376832     7835071
# 1  2019-11-10    10717154     8561348



##EXERCISE 2
import pandas as pd
# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)


    #        date  small_sold  large_sold
    # 0  2019-11-17    10859987     7674135
    # 1  2019-12-01     9291631     6238096