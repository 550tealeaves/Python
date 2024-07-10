# 	• Examples of parameters
# 		○ Alpha
# 			§ For ridge/lasso regressions
# 		○ n_neighbors
# 			§ For KNN

# 	• Try different hyperparameter values
# 	• Key is fitting them separately and evaluating them
# 	• Cross-val on training set
# 	• Use test set for final eval


# Grid search
# 	• Choose grid of possible hyperparameters to try 
# 	• Ex: can search across 2 hyperpameters for a KNN model
# 		○ Type of metric
# 		○ # neighbors

# 	• Can perform k-fold cross-validation for each combo of hyperparameters
# 	• Will show the mean scores
# 	• Choose hyperparameters that perform best

# 	• When performing grid search, code the hyperparameters that you want to tune as key/values pairs in dictionary and assign result to variable, param_grid
# 	• Will return a GridSearch object that can be fitted onto training data 
# 	• That fit will do the cross-validated grid search 
# 	• Print model's attributes best params_ & best score_, respectively to get the best performing hyperparameters + the mean cross-validation score over that fold


# Limitations of grid search
# 	• Doesn't scale well
# 		○ # fits = (# hyperparameters X # values X # folds)


# ALTERNATIVE APPROACH
# 	• RandomizedSearchCV
# 		○ Random search that picks random hyperparameters 
# 		○ n_iter argument determines how many hyperparameters are tested
		
			
# Evaluating on test set
# 	• Shows that this performs slightly better than grid search 



# Now you have seen how to perform grid search hyperparameter tuning, you are going to build a lasso regression model with optimal hyperparameters to predict blood glucose levels using the features in the diabetes_df dataset.

# X_train, X_test, y_train, and y_test have been preloaded for you. A KFold() object has been created and stored for you as kf, along with a lasso regression model as lasso.

# Import GridSearchCV
from sklearn.model_selection import GridSearchCV

# Set up the parameter grid
param_grid = {"alpha": np.linspace(0.00001, 1, 20)}

# Instantiate lasso_cv
lasso_cv = GridSearchCV(lasso, param_grid, cv=kf)

# Fit to the training data
lasso_cv.fit(X_train, y_train)
print("Tuned lasso paramaters: {}".format(lasso_cv.best_params_))
print("Tuned lasso score: {}".format(lasso_cv.best_score_))

# Tuned lasso paramaters: {'alpha': 1e-05}
# Tuned lasso score: 0.33078807238121977





# Hyperparameter tuning with RandomizedSearchCV
# As you saw, GridSearchCV can be computationally expensive, especially if you are searching over a large hyperparameter space. In this case, you can use RandomizedSearchCV, which tests a fixed number of hyperparameter settings from specified probability distributions.

# Training and test sets from diabetes_df have been pre-loaded for you as X_train. X_test, y_train, and y_test, where the target is "diabetes". A logistic regression model has been created and stored as logreg, as well as a KFold variable stored as kf.

# You will define a range of hyperparameters and use RandomizedSearchCV, which has been imported from sklearn.model_selection, to look for optimal hyperparameters from these options.

# Create the parameter space
params = {"penalty": ["l1", "l2"],
         "tol": np.linspace(0.0001, 1.0, 50),
         "C": np.linspace(0.1, 1.0, 50),
         "class_weight": ["balanced", {0:0.8, 1:0.2}]}

# Instantiate the RandomizedSearchCV object
logreg_cv = RandomizedSearchCV(logreg, params, cv=kf)

# Fit the data to the model
logreg_cv.fit(X_train, y_train)

# Print the tuned parameters and score
print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_))
print("Tuned Logistic Regression Best Accuracy Score: {}".format(logreg_cv.best_score_))

# Tuned Logistic Regression Parameters: {'tol': 0.14294285714285712, 'penalty': 'l2', 'class_weight': 'balanced', 'C': 0.6326530612244898}
# Tuned Logistic Regression Best Accuracy Score: 0.7460082633613221