# Plots
# 	• Help visualize data
# 	• 

# Histogram
# 	• Use matplotlib.pyplot as plt
# 	• Create histogram
# 		○ Select col that you want to show
# 	• Plt.show() to show hist
# 	• Ex: lots of dogs are 50-60cm tall


	
# 	• Change bins using bins argument
# 	• More/less bins can help see how distribution is shaped


# Bar plots
# 	• Show relationship b/w categorical & numeric variables
# 	• To compute avg weight by breed
# 		○ Group by breed
# 		○ Select weight column
# 		○ Take the mean
# 	• Use .plot() method to create bar
# 		○ .plot(kind="bar")
# 		○ Use title argument to add title to chart
# 			§ .plot(kind="bar", title="Mean weight by dog breed")
# 	• Ex below shows that St. Bernards are heaviest breed on avg



# Line Plots
# 	• Relationship b/w time & numeric variables
# 	• Use .plot() method w/ 3 arguments
# 		○ X
# 		○ Y
# 		○ Kind="line"
# 		○ Optional - rot=
# 			§ This argument lets you rotate the axis labels



# Scatterplots
# 	• For 2 numeric variables
# 	• 3 arguments
# 		○ X
# 		○ Y
# 		○ Kind="scatter"
# 	• Ex: taller dogs tend to weigh more
	


# Layering plots
# 	• Hist of female dog heights
# 	• Add hist of male dog heights on top
# 	• How to determine which color is which
# 		○ Pass in list of labels
# 	• To make the plot better
# 		○ Make it translucent - with .hist(alpha=  )


import pandas as pd
import matplotlib.pyplot as plt

dogs = pd.read_csv("Data Camp-intro to Python/data-manipulation-pandas/dogs.csv", index_col=0)

dogs.head()

dogs["height_cm"].hist()
plt.show()


##Adjust dist shape w/ # of bins
dogs["height_cm"].hist(bins=20)
plt.show()

dogs["height_cm"].hist(bins=5)
plt.show()





##BAR PLOTS
avg_weight_by_breed = dogs.groupby("breed")["weight_kg"].mean()
print(avg_weight_by_breed)

# breed
# Chihuahua       2.0
# Chow Chow      24.0
# Labrador       26.5
# Poodle         24.0
# Schnauzer      17.0
# St. Bernard    74.0
# Name: weight_kg, dtype: float64


avg_weight_by_breed.plot(kind="bar", color="gold")
plt.show()

avg_weight_by_breed.plot(kind="bar", title="Mean weight by dog breed", color="red")
plt.show()


##LINE PLOT - NEED X, Y, AND KIND="LINE"
dogs.plot(x="date_of_birth", y="weight_kg", kind="line", rot=50)
plt.show() #line doesn't show well b/c dates in wrong format


##SCATTERPLOT
dogs.plot(x="height_cm", y="weight_kg", kind="scatter")
plt.show()


# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")


# Show the plot
plt.show()





##EXERCISE 4
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()



##EXAMPLE 5
# Histogram of conventional avg_price 
avocados[avocados["type"] == "conventional"]["avg_price"].hist()

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist()

# Add a legend
plt.legend(['conventional', 'organic'])

# Show the plot
plt.show()





##EXERCISE 6 - LAYERS 3 HISTOGRAMS
# Modify histogram transparency to 0.5
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5)

# Modify histogram transparency to 0.5
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()


##EXERCISE 7
# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()






