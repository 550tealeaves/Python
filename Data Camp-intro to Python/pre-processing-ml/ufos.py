# Take a look at the UFO dataset's column types using the .info() method. Two columns jump out for transformation: the seconds column, which is a numeric column but is being read in as object, and the date column, which can be transformed into the datetime type. That will make our feature engineering efforts easier later on.

# Print the DataFrame info
print(ufo.info())

# Change the type of seconds to float
ufo["seconds"] = ufo["seconds"].astype(float)

# Change the date column to type datetime
ufo["date"] = pd.to_datetime(ufo["date"])

# Check the column types
print(ufo.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4935 entries, 0 to 4934
# Data columns (total 11 columns):
#  #   Column          Non-Null Count  Dtype  
# ---  ------          --------------  -----  
#  0   date            4935 non-null   object 
#  1   city            4926 non-null   object 
#  2   state           4516 non-null   object 
#  3   country         4255 non-null   object 
#  4   type            4776 non-null   object 
#  5   seconds         4935 non-null   object 
#  6   length_of_time  4792 non-null   object 
#  7   desc            4932 non-null   object 
#  8   recorded        4935 non-null   object 
#  9   lat             4935 non-null   object 
#  10  long            4935 non-null   float64
# dtypes: float64(1), object(10)
# memory usage: 424.2+ KB
# None
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4935 entries, 0 to 4934
# Data columns (total 11 columns):
#  #   Column          Non-Null Count  Dtype         
# ---  ------          --------------  -----         
#  0   date            4935 non-null   datetime64[ns]
#  1   city            4926 non-null   object        
#  2   state           4516 non-null   object        
#  3   country         4255 non-null   object        
#  4   type            4776 non-null   object        
#  5   seconds         4935 non-null   float64       
#  6   length_of_time  4792 non-null   object        
#  7   desc            4932 non-null   object        
#  8   recorded        4935 non-null   object        
#  9   lat             4935 non-null   object        
#  10  long            4935 non-null   float64       
# dtypes: datetime64[ns](1), float64(2), object(8)
# memory usage: 424.2+ KB
# None





# Remove some of the rows where certain columns have missing values. You're going to look at the length_of_time column, the state column, and the type column. You'll drop any row that contains a missing value in at least one of these three columns.

# Count the missing values in the length_of_time, state, and type columns, in that order
print(ufo[["length_of_time", "state", "type"]].isna().sum())

# Drop rows where length_of_time, state, or type are missing
ufo_no_missing = ufo.dropna(subset=["length_of_time", "state", "type"])

# Print out the shape of the new dataset
print(ufo_no_missing.shape)

# length_of_time    143
# state             419
# type              159
# dtype: int64
# (4283, 4)





# Extracting numbers from strings
# The length_of_time field in the UFO dataset is a text field that has the number of minutes within the string. Here, you'll extract that number from that text field using regular expressions.


def return_minutes(time_string):
    
    # Search for numbers in time_string
    num = re.search("\d+", time_string)
    if num is not None:
        return int(num.group(0))
        
# Apply the extraction to the length_of_time column
ufo["minutes"] = ufo["length_of_time"].apply(return_minutes)

# Take a look at the head of both of the columns
print(ufo[["length_of_time", "minutes"]].head())

#     length_of_time  minutes
# 2  about 5 minutes      5.0
# 4       10 minutes     10.0
# 7        2 minutes      2.0
# 8        2 minutes      2.0
# 9        5 minutes      5.0



# Identifying features for standardization
# Investigate the variance of columns in the UFO dataset to determine which features should be standardized. After taking a look at the variances of the seconds and minutes column, you'll see that the variance of the seconds column is extremely high. Because seconds and minutes are related to each other (an issue we'll deal with when we select features for modeling), let's log normalize the seconds column.

# Check the variance of the seconds and minutes columns
print(ufo[["seconds", "minutes"]].var())

# Log normalize the seconds column
ufo["seconds_log"] = np.log(ufo["seconds"])

# Print out the variance of just the seconds_log column
print(ufo["seconds_log"].var())

# seconds    424087.417
# minutes       117.546
# dtype: float64
# 1.1223923881183004



# Encoding categorical variables
# There are couple of columns in the UFO dataset that need to be encoded before they can be modeled through scikit-learn. You'll do that transformation here, using both binary and one-hot encoding methods.

# Use pandas to encode us values as 1 and others as 0
ufo["country_enc"] = ufo["country"].apply(lambda val: 1 if val == "us" else 0)

# Print the number of unique type values
print(len(ufo["type"].unique()))

# Create a one-hot encoded set of the type values
type_set = pd.get_dummies(ufo["type"])

# Concatenate this set back to the ufo DataFrame
ufo = pd.concat([ufo, type_set], axis=1) 

#21



# Features from dates
# Another feature engineering task to perform is month and year extraction. Perform this task on the date column of the ufo dataset.

# Look at the first 5 rows of the date column
print(ufo["date"].head())

# Extract the month from the date column
ufo["month"] = ufo["date"].dt.month

# Extract the year from the date column
ufo["year"] = ufo["date"].dt.year

# Take a look at the head of all three columns
print(ufo[["date", "month", "year"]].head())

# 0   2002-11-21 05:45:00
# 1   2012-06-16 23:00:00
# 2   2013-06-09 00:00:00
# 3   2013-04-26 23:27:00
# 4   2013-09-13 20:30:00
# Name: date, dtype: datetime64[ns]
#                  date  month  year
# 0 2002-11-21 05:45:00     11  2002
# 1 2012-06-16 23:00:00      6  2012
# 2 2013-06-09 00:00:00      6  2013
# 3 2013-04-26 23:27:00      4  2013
# 4 2013-09-13 20:30:00      9  2013



# Text vectorization
# You'll now transform the desc column in the UFO dataset into tf/idf vectors, since there's likely something we can learn from this field.

# Take a look at the head of the desc field
print(ufo["desc"].head())

# Instantiate the tfidf vectorizer object
vec = TfidfVectorizer()

# Fit and transform desc using vec
desc_tfidf = vec.fit_transform(ufo["desc"])

# Look at the number of columns and rows
print(desc_tfidf.shape)

# 0    It was a large&#44 triangular shaped flying ob...
# 1    Dancing lights that would fly around and then ...
# 2    Brilliant orange light or chinese lantern at o...
# 3    Bright red light moving north to north west fr...
# 4    North-east moving south-west. First 7 or so li...
# Name: desc, dtype: object
# (1866, 3422)




# Selecting the ideal dataset
# Now to get rid of some of the unnecessary features in the ufo dataset. Because the country column has been encoded as country_enc, you can select it and drop the other columns related to location: city, country, lat, long, and state.

# You've engineered the month and year columns, so you no longer need the date or recorded columns. You also standardized the seconds column as seconds_log, so you can drop seconds and minutes.

# You vectorized desc, so it can be removed. For now you'll keep type.

# You can also get rid of the length_of_time column, which is unnecessary after extracting minutes.


# Make a list of features to drop   
to_drop = ["city", "country", "date", "desc", "lat", "length_of_time", "long", "minutes", "recorded", "seconds", "state"]

# Drop those features
ufo_dropped = ufo.drop(to_drop, axis=1)

# Let's also filter some words out of the text vector we created
filtered_words = words_to_filter(vocab, vec.vocabulary_, desc_tfidf, 4)






# Modeling the UFO dataset, part 1
# In this exercise, you're going to build a k-nearest neighbor model to predict which country the UFO sighting took place in. The X dataset contains the log-normalized seconds column, the one-hot encoded type columns, as well as the month and year when the sighting took place. The y labels are the encoded country column, where 1 is "us" and 0 is "ca".

# Take a look at the features in the X set of data
print(X.columns)

# Split the X and y sets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Fit knn to the training sets
knn.fit(X_train, y_train)

# Print the score of knn on the test sets
print(knn.score(X_test, y_test))


# Index(['seconds_log', 'changing', 'chevron', 'cigar', 'circle', 'cone', 'cross', 'cylinder', 'diamond', 'disk', 'egg', 'fireball', 'flash', 'formation', 'light', 'other', 'oval', 'rectangle',
#        'sphere', 'teardrop', 'triangle', 'unknown', 'month', 'year'],
#       dtype='object')
# 0.8650963597430407



# Modeling the UFO dataset, part 2
# Finally, you'll build a model using the text vector we created, desc_tfidf, using the filtered_words list to create a filtered text vector. Let's see if you can predict the type of the sighting based on the text. You'll use a Naive Bayes model for this.


# Use the list of filtered words we created to filter the text vector
filtered_text = desc_tfidf[:, list(filtered_words)]

# Split the X and y sets using train_test_split, setting stratify=y 
X_train, X_test, y_train, y_test = train_test_split(filtered_text.toarray(), y, stratify=y, random_state=42)

# Fit nb to the training sets
nb.fit(X_train, y_train)

# Print the score of nb on the test sets
print(nb.score(X_test, y_test))  #0.17987152034261242