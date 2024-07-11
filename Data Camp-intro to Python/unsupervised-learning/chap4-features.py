# NMF applied to Wikipedia articles
# In the video, you saw NMF applied to transform a toy word-frequency array. Now it's your turn to apply NMF, this time using the tf-idf word-frequency array of Wikipedia articles, given as a csr matrix articles. Here, fit the model and transform the articles. In the next exercise, you'll explore the result.

# Import NMF
from sklearn.decomposition import NMF

# Create an NMF instance: model
model = NMF(n_components=6)

# Fit the model to articles
model.fit(articles)

# Transform the articles: nmf_features
nmf_features = model.transform(articles)

# Print the NMF features
print(nmf_features.round(2))


# [[0.   0.   0.   0.   0.   0.44]
#  [0.   0.   0.   0.   0.   0.57]
#  [0.   0.   0.   0.   0.   0.4 ]
#  [0.   0.   0.   0.   0.   0.38]
#  [0.   0.   0.   0.   0.   0.49]
#  [0.01 0.01 0.01 0.03 0.   0.33]
#  [0.   0.   0.02 0.   0.01 0.36]
#  [0.   0.   0.   0.   0.   0.49]
#  [0.02 0.01 0.   0.02 0.03 0.48]
#  [0.01 0.03 0.03 0.07 0.02 0.34]
#  [0.   0.   0.53 0.   0.03 0.  ]
#  [0.   0.   0.36 0.   0.   0.  ]
#  [0.01 0.01 0.31 0.06 0.01 0.02]
#  [0.   0.01 0.34 0.01 0.   0.  ]
#  [0.   0.   0.43 0.   0.04 0.  ]
#  [0.   0.   0.48 0.   0.   0.  ]
#  [0.01 0.02 0.38 0.03 0.   0.01]
#  [0.   0.   0.48 0.   0.   0.  ]
#  [0.   0.01 0.55 0.   0.   0.  ]
#  [0.   0.   0.47 0.   0.   0.  ]
#  [0.   0.01 0.02 0.52 0.06 0.01]
#  [0.   0.   0.   0.51 0.   0.  ]
#  [0.   0.01 0.   0.42 0.   0.  ]
#  [0.   0.   0.   0.44 0.   0.  ]
#  [0.   0.   0.   0.5  0.   0.  ]
#  [0.1  0.09 0.   0.38 0.   0.01]
#  [0.   0.   0.   0.57 0.   0.01]
#  [0.01 0.01 0.   0.47 0.   0.01]
#  [0.   0.   0.   0.58 0.   0.  ]
#  [0.   0.   0.   0.53 0.01 0.01]
#  [0.   0.41 0.   0.   0.   0.  ]
#  [0.   0.61 0.   0.01 0.   0.  ]
#  [0.01 0.26 0.   0.02 0.01 0.  ]
#  [0.   0.64 0.   0.   0.   0.  ]
#  [0.   0.61 0.   0.   0.   0.  ]
#  [0.   0.34 0.   0.   0.   0.  ]
#  [0.01 0.32 0.02 0.   0.01 0.  ]
#  [0.01 0.21 0.01 0.05 0.02 0.01]
#  [0.01 0.47 0.   0.02 0.   0.  ]
#  [0.   0.64 0.   0.   0.   0.  ]
#  [0.   0.   0.   0.   0.48 0.  ]
#  [0.   0.   0.   0.   0.49 0.  ]
#  [0.   0.   0.   0.   0.38 0.01]
#  [0.   0.   0.   0.01 0.54 0.  ]
#  [0.   0.   0.01 0.   0.42 0.  ]
#  [0.   0.   0.   0.   0.51 0.  ]
#  [0.   0.   0.   0.   0.37 0.  ]
#  [0.   0.   0.04 0.   0.23 0.  ]
#  [0.01 0.   0.02 0.01 0.33 0.04]
#  [0.   0.   0.   0.   0.42 0.  ]
#  [0.31 0.   0.   0.   0.   0.  ]
#  [0.37 0.   0.   0.   0.   0.  ]
#  [0.4  0.03 0.   0.02 0.   0.02]
#  [0.38 0.   0.   0.04 0.   0.01]
#  [0.44 0.   0.   0.   0.   0.  ]
#  [0.46 0.   0.   0.   0.   0.  ]
#  [0.28 0.   0.   0.05 0.   0.02]
#  [0.45 0.   0.   0.   0.01 0.  ]
#  [0.29 0.01 0.01 0.01 0.19 0.01]
#  [0.38 0.01 0.   0.1  0.01 0.  ]]




# NMF features of the Wikipedia articles
# Now you will explore the NMF features you created in the previous exercise. A solution to the previous exercise has been pre-loaded, so the array nmf_features is available. Also available is a list titles giving the title of each Wikipedia article.

# Import pandas
import pandas as pd

# Create a pandas DataFrame: df
df = pd.DataFrame(nmf_features, index=titles)

# Print the row for 'Anne Hathaway'
print(df.loc['Anne Hathaway'])

# Print the row for 'Denzel Washington'
print(df.loc['Denzel Washington'])

# 0    0.004
# 1    0.000
# 2    0.000
# 3    0.576
# 4    0.000
# 5    0.000
# Name: Anne Hathaway, dtype: float64
# 0    0.000
# 1    0.006
# 2    0.000
# 3    0.422
# 4    0.000
# 5    0.000
# Name: Denzel Washington, dtype: float64






# NMF learns topics of documents
# In the video, you learned when NMF is applied to documents, the components correspond to topics of documents, and the NMF features reconstruct the documents from the topics. Verify this for yourself for the NMF model that you built earlier using the Wikipedia articles. Previously, you saw that the 3rd NMF feature value was high for the articles about actors Anne Hathaway and Denzel Washington. In this exercise, identify the topic of the corresponding NMF component.

# Import pandas
import pandas as pd

# Create a DataFrame: components_df
components_df = pd.DataFrame(model.components_, columns=words)

# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())


# (6, 13125)
# film       0.628
# award      0.253
# starred    0.245
# role       0.211
# actress    0.186
# Name: 3, dtype: float64





# Explore the LED digits dataset
# In the following exercises, you'll use NMF to decompose grayscale images into their commonly occurring patterns. Firstly, explore the image dataset and see how it is encoded as an array. You are given 100 images as a 2D array samples, where each row represents a single 13x8 image. The images in your dataset are pictures of a LED digital display.

# Import pyplot
from matplotlib import pyplot as plt

# Select the 0th row: digit
digit = samples[0,:]

# Print digit
print(digit)

# Reshape digit to a 13x8 array: bitmap
bitmap = digit.reshape((13, 8))

# Print bitmap
print(bitmap)

# Use plt.imshow to display bitmap
plt.imshow(bitmap, cmap='gray', interpolation='nearest')
plt.colorbar()
plt.show()


# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0.
#  0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 0.
#  0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 0.
#  0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.
#  0. 0. 0. 0. 0. 0. 0. 0.]
# [[0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 1. 1. 1. 1. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]]





# NMF learns the parts of images
# Now use what you've learned about NMF to decompose the digits dataset. You are again given the digit images as a 2D array samples. This time, you are also provided with a function show_as_image() that displays the image encoded by any 1D array:

# Import NMF
from sklearn.decomposition import NMF

# Create an NMF model: model
model = NMF(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)

# Select the 0th row of features: digit_features
digit_features = features[0,:]

# Print digit_features
print(digit_features)


# [4.76823559e-01 0.00000000e+00 0.00000000e+00 5.90605054e-01
#  4.81559442e-01 0.00000000e+00 7.37551667e-16]




# PCA doesn't learn parts
# Unlike NMF, PCA doesn't learn the parts of things. Its components do not correspond to topics (in the case of documents) or to parts of images, when trained on images. Verify this for yourself by inspecting the components of a PCA model fit to the dataset of LED digit images from the previous exercise. The images are available as a 2D array samples. Also available is a modified version of the show_as_image() function which colors a pixel red if the value is negative.

# Import PCA
from sklearn.decomposition import PCA

# Create a PCA instance: model
model = PCA(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)
    



# Which articles are similar to 'Cristiano Ronaldo'?
# In the video, you learned how to use NMF features and the cosine similarity to find similar articles. Apply this to your NMF model for popular Wikipedia articles, by finding the articles most similar to the article about the footballer Cristiano Ronaldo. The NMF features you obtained earlier are available as nmf_features, while titles is a list of the article titles.

# Perform the necessary imports
import pandas as pd
from sklearn.preprocessing import normalize

# Normalize the NMF features: norm_features
norm_features = normalize(nmf_features)

# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=titles)

# Select the row corresponding to 'Cristiano Ronaldo': article
article = df.loc['Cristiano Ronaldo']

# Compute the dot products: similarities
similarities = df.dot(article)

# Display those with the largest cosine similarity
print(similarities.nlargest())


# Cristiano Ronaldo                1.0
# Franck Ribéry                    1.0
# Radamel Falcao                   1.0
# Zlatan Ibrahimović               1.0
# France national football team    1.0
# dtype: float64




# Recommend musical artists part I
# In this exercise and the next, you'll use what you've learned about NMF to recommend popular music artists! You are given a sparse array artists whose rows correspond to artists and whose columns correspond to users. The entries give the number of times each artist was listened to by each user.

# Perform the necessary imports
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

# Create a MaxAbsScaler: scaler
scaler = MaxAbsScaler()

# Create an NMF model: nmf
nmf = NMF(n_components=20)

# Create a Normalizer: normalizer
normalizer = Normalizer()

# Create a pipeline: pipeline
pipeline = make_pipeline(scaler, nmf, normalizer)

# Apply fit_transform to artists: norm_features
norm_features = pipeline.fit_transform(artists)






# Recommend musical artists part II
# Suppose you were a big fan of Bruce Springsteen - which other musical artists might you like? Use your NMF features from the previous exercise and the cosine similarity to find similar musical artists. A solution to the previous exercise has been run, so norm_features is an array containing the normalized NMF features as rows. The names of the musical artists are available as the list artist_names.


# Import pandas
import pandas as pd

# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=artist_names)

# Select row of 'Bruce Springsteen': artist
artist = df.loc['Bruce Springsteen']

# Compute cosine similarities: similarities
similarities = df.dot(artist)

# Display those with highest cosine similarity
print(similarities.nlargest())


# Bruce Springsteen    1.000
# Neil Young           0.956
# Van Morrison         0.872
# Leonard Cohen        0.865
# Bob Dylan            0.859
# dtype: float64