##ENCODING CATEGORICAL VARIABLES

# Set up the LabelEncoder object
enc = LabelEncoder()

# Apply the encoding to the "Accessible" column
hiking["Accessible_enc"] = enc.fit_transform(hiking["Accessible"])

# Compare the two columns
print(hiking[["Accessible_enc", "Accessible"]].head())

#   Accessible_enc Accessible
# 0               1          Y
# 1               0          N
# 2               0          N
# 3               0          N
# 4               0          N



##ONE HOT ENCODING
# Transform the category_desc column
category_enc = pd.get_dummies(volunteer["category_desc"])

# Take a look at the encoded columns
print(category_enc.head())



#    Education  Emergency Preparedness  Environment  Health  Helping Neighbors in Need  Strengthening Communities
# 0          0                       0            0       0                          0                          0
# 1          0                       0            0       0                          0                          1
# 2          0                       0            0       0                          0                          1
# 3          0                       0            0       0                          0                          1
# 4          0                       0            1       0                          0                          0




##--ENGINEERING NUMERICAL FEATURES--##

	# • If you have a collection of features related to 1 entity (ex: temp on diff days)
# 		○ You can use an aggregate (sum, avg etc) to use as feature for modeling

# How to take an aggregate as feature for modeling?
# 	1. Subset the cols you need to aggregate w/ .loc 
# 	2. Set axis=1 to calculate mean for each row
# 	3. Save results in mean col


# Convert dates
# 	• Use pd.to_datetime() function 
# 	• Then extract the months - for example - with dt.month attribute
# 	•  Can now model with the month col values
	
# Use .loc to create a mean column
running_times_5k["mean"] = running_times_5k.loc[:, "run1":"run5"].mean(axis=1)

# Take a look at the results
print(running_times_5k.head())

#     name  run1  run2  run3  run4  run5   mean
# 0    Sue  20.1  18.5  19.6  20.3  18.3  19.36
# 1   Mark  16.5  17.1  16.9  17.6  17.3  17.08
# 2   Sean  23.5  25.1  25.2  24.6  23.9  24.46
# 3   Erin  21.7  21.1  20.9  22.1  22.2  21.60
# 4  Jenny  25.8  27.1  26.1  26.7  26.9  26.52
	



##EXTRACTING DATETIME COMPONENTS
# First, convert string column to date column
volunteer["start_date_converted"] = pd.to_datetime(volunteer["start_date_date"])

# Extract just the month from the converted column
volunteer["start_date_month"] = volunteer["start_date_converted"].dt.month

# Take a look at the converted and new month columns
print(volunteer[["start_date_converted", "start_date_month"]].head())


#   start_date_converted  start_date_month
# 0           2011-07-30                 7
# 1           2011-02-01                 2
# 2           2011-01-29                 1
# 3           2011-02-14                 2
# 4           2011-02-05                 2
	
	








###--EXTRACTING TEXT--###

# Write a pattern to extract numbers and decimals
def return_mileage(length):
    
    # Search the text for matches
    mile = re.search("\d+\.\d+", length)
    
    # If a value is returned, use group(0) to return the found value
    if mile is not None:
        return float(mile.group(0))
        
# Apply the function to the Length column and take a look at both columns
hiking["Length_num"] = hiking["Length"].apply(return_mileage)
print(hiking[["Length", "Length_num"]].head())


#        Length  Length_num
# 0   0.8 miles        0.80
# 1    1.0 mile        1.00
# 2  0.75 miles        0.75
# 3   0.5 miles        0.50
# 4   0.5 miles        0.50





##VECTORIZING TEXT

# Take the title text
title_text = volunteer["title"]

# Create the vectorizer method
tfidf_vec = TfidfVectorizer()

# Transform the text into tf-idf vectors
text_tfidf = tfidf_vec.fit_transform(title_text)




##TEXT CLASSIFICATION USING TF/IDF VECTORS
# Split the dataset according to the class distribution of category_desc
y = volunteer["category_desc"]
X_train, X_test, y_train, y_test = train_test_split(text_tfidf.toarray(), y, stratify=y, random_state=42)

# Fit the model to the training data
nb.fit(X_train, y_train)

# Print out the model's accuracy
print(nb.score(X_test, y_test)) #0.5161290322580645



##REDUNDANT FEATURES##
# 	• Goal of feature selection is to remove unnecessary features that create noise
# 	• How do you know if feature is unnecessary?
# 		○ Check to see if there is a redundancy 

# What's a redundant feature?
# 	• Exists in another form as another feature
# 	• If 2 features strongly correlated
# 	• Duplicated features

# 	• Feature selection = iterative process


# Scenarios for manual removal of features
# 	• Dataset has repeated info in feature set
# 		○ Ex: city/state, lat/long (may only need 1)
# 		○ Drop one based on the end goal
# 	• If you take avg to use, you can drop the values used to calculate the avg


# Correlated features
# 	• Use corr() method


# 	• Features A/B have scores near 1, so one should be dropped 


##SELECT RELEVANT FEATURES
# Create a list of redundant column names to drop
to_drop = ["category_desc", "created_date", "locality", "region", "vol_requests"]

# Drop those columns from the dataset
volunteer_subset = volunteer.drop(to_drop, axis=1)

# Print out the head of volunteer_subset
print(volunteer_subset.head())


#                                                title  hits  postalcode  vol_requests_lognorm  created_month  Education  Emergency Preparedness  Environment  Health  Helping Neighbors in Need  \
# 1                                       Web designer    22     10010.0                 0.693              1          0                       0            0       0                          0   
# 2      Urban Adventures - Ice Skating at Lasker Rink    62     10026.0                 2.996              1          0                       0            0       0                          0   
# 3  Fight global hunger and support women farmers ...    14      2114.0                 6.215              1          0                       0            0       0                          0   
# 4                                      Stop 'N' Swap    31     10455.0                 2.708              1          0                       0            1       0                          0   
# 5                               Queens Stop 'N' Swap   135     11372.0                 2.708              1          0                       0            1       0                          0   

#    Strengthening Communities  
# 1                          1  
# 2                          1  
# 3                          1  
# 4                          0  
# 5                          0  




##CHECKING FOR CORRELATED FEATURES
# Print out the column correlations of the wine dataset
print(wine.corr())

# Drop that column from the DataFrame
wine = wine.drop("Flavanoids", axis=1)

print(wine.head())




