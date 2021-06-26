from textblob import TextBlob,Word
import random
import nltk

def nlp_classification(text):
    print("Summary:"+"\n"+text)
    summary=TextBlob(text)
    #nltk.download('averaged_perceptron_tagger')
    print("POS tagging:"+str(summary.tags))
    print("tokenization:"+str(summary.words))
    print("plural of :"+summary.words[2]+"-->"+summary.words[2].pluralize())
    print("plural of :"+summary.words[8]+"-->"+summary.words[8].singularize())
    print("sentences:"+str(summary.sentences))
    nltk.download('wordnet')
    nouns=[]
    for word,tag in summary.tags:
        if tag=="NN":
            nouns.append(word)
    print("this text is about...")
    for item in random.sample(nouns,3):
        word=Word(item)
        word.lemmatize()
        print(word.pluralize())

text="Building a web application allows you and via the internet from the houses."
nlp_classification(text)