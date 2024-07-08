###EX 1 - LOG NORMALIZATION
# Print out the variance of the Proline column
print(wine["Proline"].var()) ##99166.71735542436

# Apply the log normalization function to the Proline column
wine["Proline_log"] = np.log(wine["Proline"])

# Check the variance of the normalized Proline column
print(wine["Proline_log"].var()) #0.17231366191842012



##SCALING DATA
##EXERCISE 1 - SCALING DATA - STANDARDIZING COLUMNS
# Import StandardScaler
from sklearn.preprocessing import StandardScaler

# Create the scaler
scaler = StandardScaler()

# Subset the DataFrame you want to scale 
wine_subset = wine[["Ash", "Alcalinity of ash", "Magnesium"]]

# Apply the scaler to wine_subset
wine_subset_scaled = scaler.fit_transform(wine_subset)






## K-NEAREST NEIGHBORS

# 	• Have to standardize linear data or else could bias the results

# K-nearest neighbors
# 	• Classifies data based on distance to training set data
# 	• New data point assigned the same label as the majority of the points surrounding it

# How to do compute it? 
# 	1. Split the data = evaluate model's performance on new data
# 		a. Must do this before pre-processing so that test data is not used to teach the model 
# 		b. If testing data is used = data leakage
# 	2. Preprocess training data
# 	3. Instantiate a k-neighbors classifier & a standard scaler to scale features
# 		a. Fit the training features using the fit_transform() method
# 		b. Use the transform() method to pre-process the test features
# 	4. Transform() method used = test features won't be used to fit model = no data leakage
# 	5. Fit the knn.fit  model to the scaled training features 
# 	6. Use .score() method to return the test set accuracy on scaled test features 




# Split the dataset and labels into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Fit the k-nearest neighbors model to the training data
knn.fit(X_train, y_train)

# Score the model on the test data
print(knn.score(X_test, y_test)) #0.7777777777777778






###--KNN ON SCALED DATA --##
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Instantiate a StandardScaler
scaler = StandardScaler()

# Scale the training and test features
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Fit the k-nearest neighbors model to the training data
knn.fit(X_train_scaled, y_train)

# Score the model on the test data
print(knn.score(X_test_scaled, y_test)) #0.9333333333333333
