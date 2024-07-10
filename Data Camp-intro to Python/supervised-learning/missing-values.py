# 	• Missing data must be handled

# What to do with missing data?


# Dropping missing data
# 	• Common way is to drop missing value that accounts for < 5% of total data
# 	• Use dropna() method
# 		○ Pass list of columns w/ < 5% missing values to the subset argument
# 		○ Will remove the entire row in columns that have missing data


# Impute values
# 	• Replace missing w/ educated guess
# 	• Common to use mean
# 	• Also can use the median or other values
# 	• For categorical values - usu use the most frequent value (mode)
# 	• Split data before to prevent leakage

	
# 	• First split the data
# 	• Run imputer on categorical variables


# 	• Call second imputer for numerical values
# 	• Imputers = transforms


# Impute with pipeline
# 	• Object to run series of transformations and build model in 1 workflow


# 	• In pipeline, each step except the last must be a transformer




# Print missing values for each column
print(music_df.isna().sum().sort_values())

# genre                 8
# popularity           31
# loudness             44
# liveness             46
# tempo                46
# speechiness          59
# duration_ms          91
# instrumentalness     91
# danceability        143
# valence             143
# acousticness        200
# energy              200
# dtype: int64





# Print missing values for each column
print(music_df.isna().sum().sort_values())

# Remove values where less than 5% are missing
music_df = music_df.dropna(subset=['genre', 'popularity', 'loudness', 'liveness', 'tempo'])






# Print missing values for each column
print(music_df.isna().sum().sort_values())

# Remove values where less than 5% are missing
music_df = music_df.dropna(subset=["genre", "popularity", "loudness", "liveness", "tempo"])

# Convert genre to a binary feature
music_df["genre"] = np.where(music_df["genre"] == "Rock", 1, 0)

print(music_df.isna().sum().sort_values())
print("Shape of the `music_df`: {}".format(music_df.shape))

# genre                 8
# popularity           31
# loudness             44
# liveness             46
# tempo                46
# speechiness          59
# duration_ms          91
# instrumentalness     91
# danceability        143
# valence             143
# acousticness        200
# energy              200
# dtype: int64
# popularity            0
# liveness              0
# loudness              0
# tempo                 0
# genre                 0
# duration_ms          29
# instrumentalness     29
# speechiness          53
# danceability        127
# valence             127
# acousticness        178
# energy              178
# dtype: int64
# Shape of the `music_df`: (892, 12)





# Import modules
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Instantiate an imputer
imputer = SimpleImputer()

# Instantiate a knn model
knn = KNeighborsClassifier(n_neighbors=3)

# Build steps for the pipeline
steps = [("imputer", imputer), 
         ("knn", knn)]







# Having set up the steps of the pipeline in the previous exercise, you will now use it on the music_df dataset to classify the genre of songs. What makes pipelines so incredibly useful is the simple interface that they provide.

steps = [("imputer", imp_mean),
        ("knn", knn)]

# Create the pipeline
pipeline = Pipeline(steps)

# Fit the pipeline to the training data
pipeline.fit(X_train, y_train)

# Make predictions on the test set
y_pred = pipeline.predict(X_test)

# Print the confusion matrix
print(confusion_matrix(y_test, y_pred))

# [[79  9]
#  [ 4 82]]