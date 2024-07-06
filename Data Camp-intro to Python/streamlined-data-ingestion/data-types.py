##EXERCISE 1 - SPECIFY DATA TYPE
# Load csv with no additional arguments
data = pd.read_csv("vt_tax_data_2016.csv")

# Print the data types
print(data.dtypes)

# STATEFIPS     int64
# STATE        object
# zipcode       int64
# agi_stub      int64
# N1            int64
#               ...  
# A85300        int64
# N11901        int64
# A11901        int64
# N11902        int64
# A11902        int64
# Length: 147, dtype: object



##EXERCISE 2 - SET CUSTOM NA VALUES
# Create dict specifying that 0s in zipcode are NA values
null_values = {"zipcode":0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv", 
                   na_values=null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])

#    STATEFIPS STATE  zipcode  agi_stub      N1  ...  A85300  N11901  A11901  N11902  A11902
# 0         50    VT      NaN         1  111580  ...       0   10820    9734   88260  138337
# 1         50    VT      NaN         2   82760  ...       0   12820   20029   68760  151729
# 2         50    VT      NaN         3   46270  ...       0   10810   24499   34600   90583
# 3         50    VT      NaN         4   30070  ...       0    7320   21573   21300   67045
# 4         50    VT      NaN         5   39530  ...       0   12500   67761   23320  103034
# 5         50    VT      NaN         6    9620  ...   20428    3900   93123    2870   39425

# [6 rows x 147 columns]




##EXERCISE 3 - SKIP BAD DATA
try:
  # Set warn_bad_lines to issue warnings about bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines=False, 
                     warn_bad_lines=True)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")


#    STATEFIPS STATE  zipcode  agi_stub      N1  ...  A85300  N11901  A11901  N11902  A11902
# 0         50    VT        0         1  111580  ...       0   10820    9734   88260  138337
# 1         50    VT        0         2   82760  ...       0   12820   20029   68760  151729
# 2         50    VT        0         3   46270  ...       0   10810   24499   34600   90583
# 3         50    VT        0         5   39530  ...       0   12500   67761   23320  103034
# 4         50    VT        0         6    9620  ...   20428    3900   93123    2870   39425

# [5 rows x 147 columns]