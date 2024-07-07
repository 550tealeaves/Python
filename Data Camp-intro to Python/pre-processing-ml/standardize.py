# 	• Might have data w/ numerical noise
# 		○ Due to feature selection 
# 		○ Standardization
# 			§ Transforms continuous data to make it appear normally distributed


# When to standard?
# 	• Model in linear space
# 	• Features on diff scales
# 		○ Linearity assumptions


###MODELING W/O NORMALIZING
# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

knn = KNeighborsClassifier()

# Fit the knn model to the training data
knn.fit(X_train, y_train)

# Score the model on the test data
print(knn.score(X_test, y_test)) #0.6888888888888889










