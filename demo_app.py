from flask import Flask, render_template, request 
#use flask to create web apps
import spacy 
#text-analysis library
from PyDictionary import PyDictionary 
#matches definitions to words
import inflect 
#generates plurals, singular nouns, ordinals, indefinite articles, converts #s to words
import re 
# search for words 

app = Flask(__name__)
#define new variable app
#stores flask web app

def replace_nouns(input_text): #defining new function "replace_nouns" which takes "input_text" (text) as input
    nlp = spacy.load('en_core_web_sm') #initiates spacy
    doc = nlp(input_text) #processing "input_text" through spacy library to tokenize text
    dictionary=PyDictionary() #initiating PyDictionary & storing it in new variable "dictionary"
    p = inflect.engine() #initiates inflect & storing it in "p" variable 
    output_text = "" #creating EMPTY string & storing it in variable "output_text"
    for token in doc: #for token in "doc" variable 
        if token.pos_ == 'NOUN': # if token is a noun
            word = token.text #convert token into text & store it in "word" variable
            #plural = p.plural_noun(word) 
            if word == plural: #if word is equivalent to plural of the word
                definition = dictionary.meaning(word) #find meaning of the word & store it in "definition" variable
                if definition:
                    definition = definition['Noun'][0].split(' ') #take 1st definition of noun and splits it into a list of strings
                    definition = ' '.join([w for w in definition if not re.match(r'^[a-zA-Z]{1,2}$', w)])  
                    output_text += definition.capitalize() + " "
                else:
                    output_text += word + " "
            else:
                definition = dictionary.meaning(word)
                if definition:
                    definition = definition['Noun'][0].split(' ')
                    definition = ' '.join([w for w in definition if not re.match(r'^[a-zA-Z]{1,2}$', w)])
                    output_text += p.plural(definition) + " "
                else:
                    output_text += p.plural(word) + " "
        else:
            output_text += token.text + " "

    return output_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    input_text = request.form['input_text']
    output_text = replace_nouns(input_text)
    return render_template('index.html', output_text=output_text)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
