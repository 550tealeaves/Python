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



