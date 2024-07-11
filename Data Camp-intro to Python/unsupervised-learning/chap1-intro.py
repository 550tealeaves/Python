# Import KMeans
from sklearn.cluster import KMeans

# Create a KMeans instance with 3 clusters: model
model = KMeans(n_clusters=3)

# Fit model to points
model.fit(points)

# Determine the cluster labels of new_points: labels
labels = model.predict(new_points)

# Print cluster labels of new_points
print(labels)

# [1 2 0 1 2 1 2 2 2 0 1 2 2 0 0 2 0 0 2 2 0 2 1 2 1 0 2 0 0 1 1 2 2 2 0 1 2
#  2 1 2 0 1 1 0 1 2 0 0 2 2 2 2 0 0 1 1 0 0 0 1 1 2 2 2 1 2 0 2 1 0 1 1 1 2
#  1 0 0 1 2 0 1 0 1 2 0 2 0 1 2 2 2 1 2 2 1 0 0 0 0 1 2 1 0 0 1 1 2 1 0 0 1
#  0 0 0 2 2 2 2 0 0 2 1 2 0 2 1 0 2 0 0 2 0 2 0 1 2 1 1 2 0 1 2 1 1 0 2 2 1
#  0 1 0 2 1 0 0 1 0 2 2 0 2 0 0 2 2 1 2 2 0 1 0 1 1 2 1 2 2 1 1 0 1 1 1 0 2
#  2 1 0 1 0 0 2 2 2 1 2 2 2 0 0 1 2 1 1 1 0 2 2 2 2 2 2 0 0 2 0 0 0 0 2 0 0
#  2 2 1 0 1 1 0 1 0 1 0 2 2 0 2 2 2 0 1 1 0 2 2 0 2 0 0 2 0 0 1 0 1 1 1 2 0
#  0 0 1 2 1 0 1 0 0 2 1 1 1 0 2 2 2 1 2 0 0 2 1 1 0 1 1 0 1 2 1 0 0 0 0 2 0
#  0 2 2 1]





# Import pyplot
from matplotlib import pyplot as plt

# Assign the columns of new_points: xs and ys
xs = new_points[:,0]
ys = new_points[:,1]

# Make a scatter plot of xs and ys, using labels to define the colors
plt.scatter(xs, ys, c=labels, alpha=0.5)

# Assign the cluster centers: centroids
centroids = model.cluster_centers_

# Assign the columns of centroids: centroids_x, centroids_y
centroids_x = centroids[:,0]
centroids_y = centroids[:,1]

# Make a scatter plot of centroids_x and centroids_y
plt.scatter(centroids_x, centroids_y, marker='D', s=50)
plt.show()




# How many clusters of grain?
# In the video, you learned how to choose a good number of clusters for a dataset using the k-means inertia graph. You are given an array samples containing the measurements (such as area, perimeter, length, and several others) of samples of grain. What's a good number of clusters in this case?

ks = range(1, 6)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)
    
    # Fit model to samples
    model.fit(samples)
    
    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)
    
# Plot ks vs inertias
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()









# Evaluating the grain clustering
# In the previous exercise, you observed from the inertia plot that 3 is a good number of clusters for the grain data. In fact, the grain samples come from a mix of 3 different grain varieties: "Kama", "Rosa" and "Canadian". In this exercise, cluster the grain samples into three clusters, and compare the clusters to the grain varieties using a cross-tabulation.

# Create a KMeans model with 3 clusters: model
model = KMeans(n_clusters=3)

# Use fit_predict to fit model and obtain cluster labels: labels
labels = model.fit_predict(samples)

# Create a DataFrame with clusters and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['varieties'])

# Display ct
print(ct)


# varieties  Canadian wheat  Kama wheat  Rosa wheat
# labels                                           
# 0                       0           1          60
# 1                      68           9           0
# 2                       2          60          10



# Scaling fish data for clustering
# You are given an array samples giving measurements of fish. Each row represents an individual fish. The measurements, such as weight in grams, length in centimeters, and the percentage ratio of height to length, have very different scales. In order to cluster this data effectively, you'll need to standardize these features first. In this exercise, you'll build a pipeline to standardize and cluster the data.

# Perform the necessary imports
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Create scaler: scaler
scaler = StandardScaler()

# Create KMeans instance: kmeans
kmeans = KMeans(n_clusters=4)

# Create pipeline: pipeline
pipeline = make_pipeline(scaler, kmeans)



# Clustering the fish data
# You'll now use your standardization and clustering pipeline from the previous exercise to cluster the fish by their measurements, and then create a cross-tabulation to compare the cluster labels with the fish species.

# Import pandas
import pandas as pd

# Fit the pipeline to samples
pipeline.fit(samples)

# Calculate the cluster labels: labels
labels = pipeline.predict(samples)

# Create a DataFrame with labels and species as columns: df
df = pd.DataFrame({'labels': labels, 'species': species})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['species'])

# Display ct
print(ct)


# species  Bream  Pike  Roach  Smelt
# labels                            
# 0            0     0      0     13
# 1           33     0      1      0
# 2            0    17      0      0
# 3            1     0     19      1



# Clustering stocks using KMeans
# In this exercise, you'll cluster companies using their daily stock price movements (i.e. the dollar difference between the closing and opening prices for each trading day). You are given a NumPy array movements of daily price movements from 2010 to 2015 (obtained from Yahoo! Finance), where each row corresponds to a company, and each column corresponds to a trading day.

# Import Normalizer
from sklearn.preprocessing import Normalizer

# Create a normalizer: normalizer
normalizer = Normalizer()

# Create a KMeans model with 10 clusters: kmeans
kmeans = KMeans(n_clusters=10)

# Make a pipeline chaining normalizer and kmeans: pipeline
pipeline = make_pipeline(normalizer, kmeans)

# Fit pipeline to the daily price movements
pipeline.fit(movements)


# Pipeline(steps=[('normalizer', Normalizer()),
#                 ('kmeans', KMeans(n_clusters=10))])




# Which stocks move together?
# In the previous exercise, you clustered companies by their daily stock price movements. So which company have stock prices that tend to change in the same way? You'll now inspect the cluster labels from your clustering to find out.

# Import pandas
import pandas as pd

# Predict the cluster labels: labels
labels = pipeline.predict(movements)

# Create a DataFrame aligning labels and companies: df
df = pd.DataFrame({'labels': labels, 'companies': companies})

# Display df sorted by cluster label
print(df.sort_values('labels'))


#     labels                           companies
# 59       0                               Yahoo
# 15       0                                Ford
# 35       0                            Navistar
# 26       1                      JPMorgan Chase
# 16       1                   General Electrics
# 58       1                               Xerox
# 11       1                               Cisco
# 18       1                       Goldman Sachs
# 20       1                          Home Depot
# 5        1                     Bank of America
# 3        1                    American express
# 55       1                         Wells Fargo
# 1        1                                 AIG
# 38       2                               Pepsi
# 40       2                      Procter Gamble
# 28       2                           Coca Cola
# 27       2                      Kimberly-Clark
# 9        2                   Colgate-Palmolive
# 54       3                            Walgreen
# 36       3                    Northrop Grumman
# 29       3                     Lookheed Martin
# 4        3                              Boeing
# 0        4                               Apple
# 47       4                            Symantec
# 33       4                           Microsoft
# 32       4                                  3M
# 31       4                           McDonalds
# 30       4                          MasterCard
# 50       4  Taiwan Semiconductor Manufacturing
# 14       4                                Dell
# 17       4                     Google/Alphabet
# 24       4                               Intel
# 23       4                                 IBM
# 2        4                              Amazon
# 51       4                   Texas instruments
# 43       4                                 SAP
# 45       5                                Sony
# 48       5                              Toyota
# 21       5                               Honda
# 22       5                                  HP
# 34       5                          Mitsubishi
# 7        5                               Canon
# 56       6                            Wal-Mart
# 57       7                               Exxon
# 44       7                        Schlumberger
# 8        7                         Caterpillar
# 10       7                      ConocoPhillips
# 12       7                             Chevron
# 13       7                   DuPont de Nemours
# 53       7                       Valero Energy
# 39       8                              Pfizer
# 41       8                       Philip Morris
# 25       8                   Johnson & Johnson
# 49       9                               Total
# 46       9                      Sanofi-Aventis
# 37       9                            Novartis
# 42       9                   Royal Dutch Shell
# 19       9                     GlaxoSmithKline
# 52       9                            Unilever
# 6        9            British American Tobacco




