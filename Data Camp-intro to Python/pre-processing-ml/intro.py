##EX 1 - DROP MISSING DATA
# Drop the Latitude and Longitude columns from volunteer
volunteer_cols = volunteer.drop(["Latitude", "Longitude"], axis=1)

# Drop rows with missing category_desc values from volunteer_cols
volunteer_subset = volunteer_cols.dropna(subset=["category_desc"])

# Print out the shape of the subset
print(volunteer_subset.shape) #617, 33



###CONVERTING DATA TYPES
# 	• Think about the types you have because may have to transfer them
# 	• Pandas data types have subtle differences 
# 	• Most common
# 		○ Object 
# 			§ String values
# 			§ Mix types
# 		○ Int64
# 			§ Integer
# 		○ Float64
# 			§ Float
# 		○ Datetime64
# 			§ Dates/times


# Converting column types
# 	• .info() shows the type for col C is object
# 	• However, the dataframe shows that column C has numeric values
	
	
# 	• Use .astype() method to convert columns
# 	• Ensure that all values with a column can be converted w/o issue



###EXERCISE 1 - CONVERTING COLUMN TYPE
# Print the head of the hits column
print(volunteer["hits"].head())

# Convert the hits column to type int
volunteer["hits"] = volunteer["hits"].astype("int")

# Look at the dtypes of the dataset
print(volunteer.dtypes)

# 0    737
# 1     22
# 2     62
# 3     14
# 4     31
# Name: hits, dtype: int64
# opportunity_id          int64
# content_id              int64
# vol_requests            int64
# event_time              int64
# title                  object
# hits                    int64
# summary                object
# is_priority            object
# category_id           float64
# category_desc          object
# amsl                  float64
# amsl_unit             float64
# org_title              object
# org_content_id          int64
# addresses_count         int64
# locality               object
# region                 object
# postalcode            float64
# primary_loc           float64
# display_url            object
# recurrence_type        object
# hours                   int64
# created_date           object
# last_modified_date     object
# start_date_date        object
# end_date_date          object
# status                 object
# Latitude              float64
# Longitude             float64
# Community Board       float64
# Community Council     float64
# Census Tract          float64
# BIN                   float64
# BBL                   float64
# NTA                   float64
# dtype: object





# Create a DataFrame with all columns except category_desc
X = volunteer.drop("category_desc", axis=1)

# Create a category_desc labels dataset
y = volunteer[["category_desc"]]

# Use stratified sampling to split up the dataset according to the y dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Print the category_desc counts from y_train
print(y_train["category_desc"].value_counts())

# Strengthening Communities    230
# Helping Neighbors in Need     89
# Education                     69
# Health                        39
# Environment                   24
# Emergency Preparedness        11
# Name: category_desc, dtype: int64



