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