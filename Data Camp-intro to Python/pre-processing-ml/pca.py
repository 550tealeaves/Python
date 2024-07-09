# PCA keeps # components = to # input features

# 	• Most of variance explained w/ 1st component = can drop the other components that don't

# 	• PCA is a blackbox method
# 		○ Hard to interpret components


    
    
# In this exercise, you'll apply PCA to the wine dataset, to see if you can increase the model's accuracy.

# Instantiate a PCA object
pca = PCA()

# Define the features and labels from the wine dataset
X = wine.drop("Type", axis=1)
y = wine["Type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Apply PCA to the wine dataset
pca_X_train = pca.fit_transform(X_train)
pca_X_test = pca.transform(X_test)

# Look at the percentage of variance explained by the different components
print(pca.explained_variance_ratio_)

# [9.97795009e-01 2.02071827e-03 9.88350594e-05 5.66222566e-05
#  1.26161135e-05 8.93235789e-06 3.13856866e-06 1.57406401e-06
#  1.15918860e-06 7.49332354e-07 3.70332305e-07 1.94185373e-07
#  8.08440051e-08]





# Now that you have run PCA on the wine dataset, you'll finally train a KNN model using the transformed data.
# Fit knn to the training data
knn.fit(pca_X_train, y_train)

# Score knn on the test data and print it out
print(knn.score(pca_X_test, y_test)) #0.7777777777777778

