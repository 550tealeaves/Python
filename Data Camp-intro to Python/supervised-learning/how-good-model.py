# Import confusion matrix
from sklearn.metrics import confusion_matrix, classification_report

knn = KNeighborsClassifier(n_neighbors=6)

# Fit the model to the training data
knn.fit(X_train, y_train)

# Predict the labels of the test data: y_pred
y_pred = knn.predict(X_test)

# Generate the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# [[116  35]
#  [ 46  34]]
#               precision    recall  f1-score   support

#            0       0.72      0.77      0.74       151
#            1       0.49      0.42      0.46        80

#     accuracy                           0.65       231
#    macro avg       0.60      0.60      0.60       231
# weighted avg       0.64      0.65      0.64       231