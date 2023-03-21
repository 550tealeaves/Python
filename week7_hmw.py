# For Q1 - Q11, use the "#" key to annotate the code and 
# explain what *each line* of code is accomplishing
# Be as specific as possible. 
# Each line of code is worth .5 point for a total of 10 points. 


Q1. 
import nltk  #must import library to use it 

Q2. 
from nltk.book import *  #imports the books 

Q3. 
text4.concordance("great")

Q4. 
text4.similar("great")

Q5. 
text4_tokens = []   #creating an empty list and setting it equal to new variable - text4_tokens
for t in text4:   # for every item (words) in text4 - "t" could be any thing
    if t.isalpha():  # isalpha() looks for only letters - if t is a letter
        t = t.lower()  #take the "t" that are letters and make them lowercase and store it as t
        text4_tokens.append(t)  #add those lowercase words into the original list

Q6.
text4_slice = text4_tokens[0:10000]
len(set(text4_slice)) / len(text4_slice)


Q7. 
from nltk.corpus import stopwords  #imports preset list of stop words from nltk corpus - can add more to the list

Q8. 
stops = stopwords.words('english') #want the English stop words and setting that equal to variable stops to store it

Q9. 
text4_stops = [t for t in text4_tokens if t not in stops] #keep everything that is not in the English stop list - keep "t" from t in text4 if "t" is not in stops list and store it as variable in text4_stops

Q10.
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

Q11. 
text4_clean = []
for t in text4_stops: 
    t_lem = wordnet_lemmatizer.lemmatize(t) 
    text4_clean.append(t_lem) 


