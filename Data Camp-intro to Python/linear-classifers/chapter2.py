# Changing the model coefficients
# When you call fit with scikit-learn, the logistic regression coefficients are automatically learned from your dataset. In this exercise you will explore how the decision boundary is represented by the coefficients. To do so, you will change the coefficients manually (instead of with fit), and visualize the resulting classifiers.
# Set the coefficients
model.coef_ = np.array([[-1,1]])
model.intercept_ = np.array([-3])

# Plot the data and decision boundary
plot_classifier(X,y,model)

# Print the number of errors
num_err = np.sum(y != model.predict(X))
print("Number of errors:", num_err)

#Number of errors: 0



##LOSS FUNCTION###
# In this exercise you'll implement linear regression "from scratch" using scipy.optimize.minimize.

# The squared error, summed over training examples
def my_loss(w):
    s = 0
    for i in range(y.size):
        # Get the true and predicted target values for example 'i'
        y_i_true = y[i]
        y_i_pred = w@X[i]
        s = s + (y_i_true - y_i_pred)**2
    return s

# Returns the w that makes my_loss(w) smallest
w_fit = minimize(my_loss, X[0]).x
print(w_fit)

# Compare with scikit-learn's LinearRegression coefficients
lr = LinearRegression(fit_intercept=False).fit(X,y)
print(lr.coef_)

# [-9.28967297e-02  4.87153175e-02 -4.05723042e-03  2.85399119e+00
#  -2.86835054e+00  5.92815219e+00 -7.26944750e-03 -9.68513678e-01
#   1.71156278e-01 -9.39664456e-03 -3.92187072e-01  1.49054687e-02
#  -4.16304299e-01]
# [-9.28965170e-02  4.87149552e-02 -4.05997958e-03  2.85399882e+00
#  -2.86843637e+00  5.92814778e+00 -7.26933458e-03 -9.68514157e-01
#   1.71151128e-01 -9.39621540e-03 -3.92190926e-01  1.49056102e-02
#  -4.16304471e-01]




# Comparing the logistic and hinge losses
# In this exercise you'll create a plot of the logistic and hinge losses using their mathematical expressions, which are provided to you.

# Mathematical functions for logistic and hinge losses
def log_loss(raw_model_output):
   return np.log(1+np.exp(-raw_model_output))
def hinge_loss(raw_model_output):
   return np.maximum(0,1-raw_model_output)

# Create a grid of values and plot
grid = np.linspace(-2,2,1000)
plt.plot(grid, log_loss(grid), label='logistic')
plt.plot(grid, hinge_loss(grid), label='hinge')
plt.legend()
plt.show()



# Implementing logistic regression
# This is very similar to the earlier exercise where you implemented linear regression "from scratch" using scipy.optimize.minimize. However, this time we'll minimize the logistic loss and compare with scikit-learn's LogisticRegression (we've set C to a large value to disable regularization; more on this in Chapter 3!).

# The logistic loss, summed over training examples
def my_loss(w):
    s = 0
    for i in range(y.size):
        raw_model_output = w@X[i]
        s = s + log_loss(raw_model_output * y[i])
    return s

# Returns the w that makes my_loss(w) smallest
w_fit = minimize(my_loss, X[0]).x
print(w_fit)

# Compare with scikit-learn's LogisticRegression
lr = LogisticRegression(fit_intercept=False, C=1000000).fit(X,y)
print(lr.coef_)


# [ 1.0365215  -1.65378094  4.08263334 -9.40917487 -1.06787256  0.07896421
#  -0.85110535 -2.44101394 -0.45285584  0.43353384]
# [[ 1.03665946 -1.65380077  4.08233062 -9.40904867 -1.06787935  0.07901598
#   -0.85099843 -2.44107473 -0.45288928  0.43348202]]