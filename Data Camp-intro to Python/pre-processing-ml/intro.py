##EX 1 - DROP MISSING DATA
# Drop the Latitude and Longitude columns from volunteer
volunteer_cols = volunteer.drop(["Latitude", "Longitude"], axis=1)

# Drop rows with missing category_desc values from volunteer_cols
volunteer_subset = volunteer_cols.dropna(subset=["category_desc"])

# Print out the shape of the subset
print(volunteer_subset.shape) #617, 33