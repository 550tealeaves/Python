# Correlated data in nature
# You are given an array grains giving the width and length of samples of grain. You suspect that width and length will be correlated. To confirm this, make a scatter plot of width vs length and measure their Pearson correlation.

# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Assign the 0th column of grains: width
width = grains[:,0]

# Assign the 1st column of grains: length
length = grains[:,1]

# Scatter plot width vs length
plt.scatter(width, length)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation
correlation, pvalue = pearsonr(width, length)

# Display the correlation
print(correlation) #0.8604149377143469




# Decorrelating the grain measurements with PCA
# You observed in the previous exercise that the width and length measurements of the grain are correlated. Now, you'll use PCA to decorrelate these measurements, then plot the decorrelated points and measure their Pearson correlation.

# Import PCA
from sklearn.decomposition import PCA

# Create PCA instance: model
model = PCA()

# Apply the fit_transform method of model to grains: pca_features
pca_features = model.fit_transform(grains)

# Assign 0th column of pca_features: xs
xs = pca_features[:,0]

# Assign 1st column of pca_features: ys
ys = pca_features[:,1]

# Scatter plot xs vs ys
plt.scatter(xs, ys)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation of xs and ys
correlation, pvalue = pearsonr(xs, ys)

# Display the correlation
print(correlation) #5.4909917646575975e-17




# The first principal component
# The first principal component of the data is the direction in which the data varies the most. In this exercise, your job is to use PCA to find the first principal component of the length and width measurements of the grain samples, and represent it as an arrow on the scatter plot.

# Make a scatter plot of the untransformed points
plt.scatter(grains[:,0], grains[:,1])

# Create a PCA instance: model
model = PCA()

# Fit model to points
model.fit(grains)

# Get the mean of the grain samples: mean
mean = model.mean_

# Get the first principal component: first_pc
first_pc = model.components_[0,:]

# Plot first_pc as an arrow, starting at mean
plt.arrow(mean[0], mean[1], first_pc[0], first_pc[1], color='red', width=0.01)

# Keep axes on same scale
plt.axis('equal')
plt.show()




# Variance of the PCA features
# The fish dataset is 6-dimensional. But what is its intrinsic dimension? Make a plot of the variances of the PCA features to find out. As before, samples is a 2D array, where each row represents a fish. You'll need to standardize the features first.

# Perform the necessary imports
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

# Create scaler: scaler
scaler = StandardScaler()

# Create a PCA instance: pca
pca = PCA()

# Create pipeline: pipeline
pipeline = make_pipeline(scaler, pca)

# Fit the pipeline to 'samples'
pipeline.fit(samples)

# Plot the explained variances
features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_)
plt.xlabel('PCA feature')
plt.ylabel('variance')
plt.xticks(features)
plt.show()





# Dimension reduction of the fish measurements
# In a previous exercise, you saw that 2 was a reasonable choice for the "intrinsic dimension" of the fish measurements. Now use PCA for dimensionality reduction of the fish measurements, retaining only the 2 most important components.

# Import PCA
from sklearn.decomposition import PCA

# Create a PCA instance with 2 components: pca
pca = PCA(n_components=2)

# Fit the PCA instance to the scaled samples
pca.fit(scaled_samples)

# Transform the scaled samples: pca_features
pca_features = pca.transform(scaled_samples)

# Print the shape of pca_features
print(pca_features.shape)  #(85, 2)





# A tf-idf word-frequency array
# In this exercise, you'll create a tf-idf word frequency array for a toy collection of documents. For this, use the TfidfVectorizer from sklearn. It transforms a list of documents into a word frequency array, which it outputs as a csr_matrix. It has fit() and transform() methods like other sklearn objects.

# Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Create a TfidfVectorizer: tfidf
tfidf = TfidfVectorizer() 

# Apply fit_transform to document: csr_mat
csr_mat = tfidf.fit_transform(documents)

# Print result of toarray() method
print(csr_mat.toarray())

# Get the words: words
words = tfidf.get_feature_names()

# Print words
print(words)


# [[0.51785612 0.         0.         0.68091856 0.51785612 0.        ]
#  [0.         0.         0.51785612 0.         0.51785612 0.68091856]
#  [0.51785612 0.68091856 0.51785612 0.         0.         0.        ]]
# ['cats', 'chase', 'dogs', 'meow', 'say', 'woof']






# Clustering Wikipedia part I
# You saw in the video that TruncatedSVD is able to perform PCA on sparse arrays in csr_matrix format, such as word-frequency arrays. Combine your knowledge of TruncatedSVD and k-means to cluster some popular pages from Wikipedia. In this exercise, build the pipeline. In the next exercise, you'll apply it to the word-frequency array of some Wikipedia articles.

# Create a Pipeline object consisting of a TruncatedSVD followed by KMeans. (This time, we've precomputed the word-frequency matrix for you, so there's no need for a TfidfVectorizer).

# Perform the necessary imports
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components=50)

# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters=6)

# Create a pipeline: pipeline
pipeline = make_pipeline(svd, kmeans)





# Clustering Wikipedia part II
# It is now time to put your pipeline from the previous exercise to work! You are given an array articles of tf-idf word-frequencies of some popular Wikipedia articles, and a list titles of their titles. Use your pipeline to cluster the Wikipedia articles.

# Import pandas
import pandas as pd

# Fit the pipeline to articles
pipeline.fit(articles)

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})

# Display df sorted by cluster label
print(df.sort_values('label'))


#     label                                        article
# 59      0                                    Adam Levine
# 57      0                          Red Hot Chili Peppers
# 56      0                                       Skrillex
# 55      0                                  Black Sabbath
# 54      0                                 Arctic Monkeys
# 53      0                                   Stevie Nicks
# 52      0                                     The Wanted
# 51      0                                     Nate Ruess
# 50      0                                   Chad Kroeger
# 58      0                                         Sepsis
# 30      1                  France national football team
# 31      1                              Cristiano Ronaldo
# 32      1                                   Arsenal F.C.
# 33      1                                 Radamel Falcao
# 37      1                                       Football
# 35      1                Colombia national football team
# 36      1              2014 FIFA World Cup qualification
# 38      1                                         Neymar
# 39      1                                  Franck Ribéry
# 34      1                             Zlatan Ibrahimović
# 26      2                                     Mila Kunis
# 28      2                                  Anne Hathaway
# 27      2                                 Dakota Fanning
# 25      2                                  Russell Crowe
# 29      2                               Jennifer Aniston
# 23      2                           Catherine Zeta-Jones
# 22      2                              Denzel Washington
# 21      2                             Michael Fassbender
# 20      2                                 Angelina Jolie
# 24      2                                   Jessica Biel
# 10      3                                 Global warming
# 11      3       Nationally Appropriate Mitigation Action
# 13      3                               Connie Hedegaard
# 14      3                                 Climate change
# 12      3                                   Nigel Lawson
# 16      3                                        350.org
# 17      3  Greenhouse gas emissions by the United States
# 18      3  2010 United Nations Climate Change Conference
# 19      3  2007 United Nations Climate Change Conference
# 15      3                                 Kyoto Protocol
# 8       4                                        Firefox
# 1       4                                 Alexa Internet
# 2       4                              Internet Explorer
# 3       4                                    HTTP cookie
# 4       4                                  Google Search
# 5       4                                         Tumblr
# 6       4                    Hypertext Transfer Protocol
# 7       4                                  Social search
# 49      4                                       Lymphoma
# 42      4                                    Doxycycline
# 47      4                                          Fever
# 46      4                                     Prednisone
# 44      4                                           Gout
# 43      4                                       Leukemia
# 9       4                                       LinkedIn
# 48      4                                     Gabapentin
# 0       4                                       HTTP 404
# 45      5                                    Hepatitis C
# 41      5                                    Hepatitis B
# 40      5                                    Tonsillitis

