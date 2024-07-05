	# • Data frame = 2D data structures
	# 	○ Col (variables)
	# 	○ Rows (index)
	# 		§ Default index = row #
	# 		§ But can specify col as index
	# • Flat files
	# 	○ Simple easy to make format
	# 	○ Exported in diff applications
	# 	○ Data stored as plain text (no formatting)
	# 	○ 1 row/line
	# 	○ Use delimiter to separate values for diff fields
	# 	○ Ex: CSV
	# 	○ read_csv() - 1 pandas function loads them all 

	# • To import file
	# 	1. Import pandas as pd
	# 	2. Tax_data = pd.read_csv("filename.csv)
	# 	3. Tax_data.head()

	# • If the file is not a csv
	# 	○ Specify delimiter w/ sep argument
	# 	○ Tax_data = pd.read_csv("filename.tsv", sep="\t")
	# 	○ Tax_data.head(3)


##EXERCISE 1 - LOAD DATA FROM CSV
# Import pandas as pd
import pandas as pd

# Read the CSV and assign it to the variable data
data = pd.read_csv("vt_tax_data_2016.csv")

# View the first few lines of data
print(data.head())


#    STATEFIPS STATE  zipcode  agi_stub      N1  ...  A85300  N11901  A11901  N11902  A11902
# 0         50    VT        0         1  111580  ...       0   10820    9734   88260  138337
# 1         50    VT        0         2   82760  ...       0   12820   20029   68760  151729
# 2         50    VT        0         3   46270  ...       0   10810   24499   34600   90583
# 3         50    VT        0         4   30070  ...       0    7320   21573   21300   67045
# 4         50    VT        0         5   39530  ...       0   12500   67761   23320  103034

# [5 rows x 147 columns]



##EXERCISE 2 - LOAD OTHER FLAT FILES = USE SEP ARGUMENT
# Import pandas with the alias pd
import pandas as pd

# Load TSV using the sep keyword argument to set delimiter
data = pd.read_csv("vt_tax_data_2016.tsv", sep="\t")

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()





### MODIFY FLAT FILES IMPORT ### 
# What if you only want to import certain parts of a dataset? 

# Use shape attribute to see how many rows & col 


# How to wittle down the dataset? 

# Limit columns 

# Choose cols to load w/ usecols keyword argument 

# Takes list of col #s or names OR a function to filter col names 


# Limiting rows 

# Use nrows argument to limit # rows loaded 

# Takes an integer  

# Check shape attribute to ensure this works 

# Use nrows & skiprows together to process file in pieces 

# Skiprows accepts list of row #s, a # of rows to skip OR function to filter rows & skips them 

# Set header=None so pandas knows there's no col names 

 

 

##EXERCISE 1 - IMPORT SUBSET OF COLS
# Create list of columns to use
cols = ["zipcode", "agi_stub", "mars1", "MARS2", "NUMDEP"]

# Create dataframe from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols=cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())


#            zipcode   mars1  MARS2  NUMDEP
# agi_stub                                
# 1         1439444  170320  28480   52490
# 2         1439444  104000  37690   64660
# 3         1439444   39160  45390   47330
# 4         1439444   11670  44410   37760
# 5         1439444    7820  67750   60730
# 6         1439444    1210  16340   16300




## EXERCISE 2 - IMPORT FILE IN CHUNKS
# Create dataframe of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None,
                       		  names=list(vt_data_first500))

# View the Vermont dataframes to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())

 
#    STATEFIPS STATE  zipcode  agi_stub      N1  ...  A85300  N11901  A11901  N11902  A11902
# 0         50    VT        0         1  111580  ...       0   10820    9734   88260  138337
# 1         50    VT        0         2   82760  ...       0   12820   20029   68760  151729
# 2         50    VT        0         3   46270  ...       0   10810   24499   34600   90583
# 3         50    VT        0         4   30070  ...       0    7320   21573   21300   67045
# 4         50    VT        0         5   39530  ...       0   12500   67761   23320  103034

# [5 rows x 147 columns]
#    STATEFIPS STATE  zipcode  agi_stub   N1  ...  A85300  N11901  A11901  N11902  A11902
# 0         50    VT     5356         2  180  ...       0      50      76     130     212
# 1         50    VT     5356         3   80  ...       0      40     142      50     148
# 2         50    VT     5356         4   50  ...       0       0       0      30      87
# 3         50    VT     5356         5   80  ...       0      30     531      30     246
# 4         50    VT     5356         6    0  ...       0       0       0       0       0

# [5 rows x 147 columns]

 

 

 


 

# Check dataframe and there are no column names b/c header row exclude 

 

 

# Assigning col names 

# Pass list to names argument 

# List must have name for every col in data 

# Rename columns AFTER import 

 

 


# Results in 1 row w/ ~150 col 