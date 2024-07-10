
# 	• Real world data is messy and often requires pre-processing before building models

# 	• 1st create binary features for each of the 10 genres
# 	• But if a song is not any of the 1st 9 genres, then implicitly it is in the Rock genre
# 	• So you can delete the Rock feature b/c it's a duplication that may affect models = only need 9 features

# 	• Can see how popularity differs by genre

# How to create dummy variables?
# 	1. Import pandas
# 	2. Load data
# 	3. Use pd.get_dummies() method & pass in the categorical column
# 		a. Set drop_first argument to True b/c only need 9/10 features
# 	4. Print dataframe.head()
# 	5. Use pd.concat() to bring the dummy variables back into the original dataframe
# 		a. Pass list w/ music_df (dataframe) & music_dummies (dummies dataframe)
# 		b. Set axis=1
# 	6. Remove "genre" column using drop() method on the music_dummies variable 
# 		a. Set axis=1


# Encoding dummy variables
# 	• If dataframe has 1 cat feature, then parse the entire dataframe and skip step of combining variables




# Create music_dummies
music_dummies = pd.get_dummies(music_df, drop_first=True)

# Print the new DataFrame
print("New DataFrame-music_dummies: {}".format(music_dummies))

# Print the new DataFrame's shape
print("Shape of music_dummies: {}".format(music_dummies.shape))



# New DataFrame-music_dummies:      popularity  acousticness  danceability  duration_ms  energy  ...  genre_Electronic  genre_Hip-Hop  genre_Jazz  genre_Rap  genre_Rock
# 0          41.0     6.440e-01         0.823     236533.0   0.814  ...                 0              0           1          0           0
# 1          62.0     8.550e-02         0.686     154373.0   0.670  ...                 0              0           0          1           0
# 2          42.0     2.390e-01         0.669     217778.0   0.736  ...                 1              0           0          0           0
# 3          64.0     1.250e-02         0.522     245960.0   0.923  ...                 0              0           0          0           1
# 4          60.0     1.210e-01         0.780     229400.0   0.467  ...                 0              0           0          1           0
# ..          ...           ...           ...          ...     ...  ...               ...            ...         ...        ...         ...
# 995        65.0     9.830e-04         0.531     216067.0   0.855  ...                 0              0           0          0           1
# 996        38.0     3.320e-02         0.608     218624.0   0.938  ...                 1              0           0          0           0
# 997        56.0     5.790e-03         0.939     144453.0   0.373  ...                 0              0           0          1           0
# 998        64.0     2.500e-01         0.546     178147.0   0.631  ...                 0              0           0          0           1
# 999        61.0     7.250e-02         0.641         -1.0   0.792  ...                 0              0           0          0           1

# [1000 rows x 20 columns]
# In [1]:



#Shape of music_dummies: (1000, 20)







# Now you have created music_dummies, containing binary features for each song's genre, it's time to build a ridge regression model to predict song popularity.
# The model will be evaluated by calculating the average RMSE, but first, you will need to convert the scores for each fold to positive values and take their square root. This metric shows the average error of our model's predictions, so it can be compared against the standard deviation of the target value—"popularity".

# Create X and y
X = music_dummies.drop("popularity", axis=1).values
y = music_dummies["popularity"].values

# Instantiate a ridge model
ridge = Ridge(alpha=0.2)

# Perform cross-validation
scores = cross_val_score(ridge, X, y, cv=kf, scoring="neg_mean_squared_error")

# Calculate RMSE
rmse = np.sqrt(-scores)
print("Average RMSE: {}".format(np.mean(rmse)))
print("Standard Deviation of the target array: {}".format(np.std(y)))


# Average RMSE: 8.236853840202299
# Standard Deviation of the target array: 14.02156909907019







