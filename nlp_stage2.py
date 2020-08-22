import nltk
from nltk.stem.lancaster import LancasterStemmer
import random
stemmer = LancasterStemmer()
import json
import pickle
import pandas as pd
import numpy as np
import tensorflow as tf

data = pickle.load(open("data.pickle","rb"))
words = data["words"]
classes = data["classes"]

def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                # if show_details:
                #     print ("found in bag: %s" % w)

    return(np.array(bag))

# p = bow("Hello how are you?", words)
# print (p)
# print (classes)
model = tf.keras.models.load_model("my_model.h5")

def classify_local(sentence):
    ERROR_THRESHOLD = 0.25
    
    # generate probabilities from the model
    input_data = pd.DataFrame([bow(sentence, words)], dtype=float, index=['input'])
    results = model.predict([input_data])[0]
    # filter out predictions below a threshold, and provide intent index
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], str(r[1])))
    # return tuple of intent and probability
    
    return return_list

def final_fuction(sentence):
    ints=classify_local(sentence)
    ints=ints[0][0]
    with open('intents.json') as file :
        answer = json.load(file)

    for tg in answer["intents"]:
        if tg["tag"]==ints:
            resposes=tg["responses"]

    # print(random.choice(resposes))
    return  random.choice(resposes)