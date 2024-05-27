# For Q1 - Q7, use the "#" key to annotate the code and 
# explain what *each line* of code is accomplishing
# Be as specific as possible. 
# Each line of code is worth .5 point for a total of 9 points. 
# For Q8, answer two questions connected to the code below the question, each worth .5 points

# Q1 - library for data requests
import requests

# Q2 - connect to the text of the website - get function is part of requests library - url listed as string - save results in variable 
response = requests.get("https://apnews.com/article/business-health-north-america-post-traumatic-stress-disorder-ap-top-news-af93ce6f3daf4a8b97f21b9cde196cda")

# Q3 - define new variable set that equal to response.text - extract text
html_string = response.text 
print(html_string)

# Q4 import BeautifulSoup - library that parses through HTML text
from bs4 import BeautifulSoup

# Q5 - save results of parsing into variable soup and then extract the text from soup variable & save it as variable - article
soup = BeautifulSoup(html_string)
article = soup.get_text()
print(article)

# Q6 aving your results as a text file to use in other apps
# for new files, must have "w" (write)
# gets variable name "file" - to write to this file the variable - article
# will create the file in the same folder as this juptyer file or VS code file
with open("AP_article.txt","w") as file: 
    file.write(article)


# Q7.
from wordcloud import WordCloud   
import matplotlib.pyplot as plt

unique_string=(" ").join(article)
wordcloud = WordCloud(max_font_size=40).generate(unique_string)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# Q8. The following questions relate to the script below. You may test the code using the files
# folder created during our class session. 
# 1. (0.5 points) Which Python libraries need to be imported for the script to run?
# 2. (0.5 points)There are five errors in the script below. Can you spot and correct them (mention the line number as it appears on your script)?

directory = "files"
files = glob(f"{directory}/*.txt") 

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

id = 0
lexical_density = []  
for filepath in file: #this should be files
    text = open(filepath, encoding='utf-8').read()
    text_tokens = nltk.word_tokenize(text)
    nltk_text = nltk.Text(text_tokens)
    text_lower = [t.lower() for t in nltk_text if t.isalnum()]
    text_stops = [t for t in text_lower if t not in stops]
    text_clean = [WordNetLemmatizer().lemmatize(t, get_wordnet_pos(t)) for t in text_clean] 
    
# save cleaned files

    # id += 1
    # # with open(f"files_cleaned/article_cleaned_{id}.txt", "w") as file 
    #     file.write(str(text_clean))

# create Word Clouds
    unique_string=(" ").join(text_clean)
    wordcloud = WordCloud(max_font_size=40).generate(unique_string)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# save Word Clouds

    id += 1
    wordcloud.to_file(f"wordclouds/word_cloud_{id}.png")

# Establish lexical density
    text_clean_slice = text_clean [0:600]
    ld_results = len(text_clean_slice) / len(text_clean_slice) 
    print(ld_results)
    ld_dict = {'File_name': filepath, 'lexical_density': ld_results}
    lexical_density.append(ld_dict)

print(lexical_density)

