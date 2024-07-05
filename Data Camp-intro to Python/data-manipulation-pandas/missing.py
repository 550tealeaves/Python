import pandas as pd

dogs = pd.read_csv("Data Camp-intro to Python/data-manipulation-pandas/dogs.csv", index_col=0)

dogs.head()


dogs.isna()
dogs.isna().any()


dogs.isna().sum()





#EXERCISE 4
# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = ____

# Create histograms of the filled columns
____

# Show the plot
plt.show()

