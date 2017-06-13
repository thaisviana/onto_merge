# -*- coding: utf-8 -*-
from nltk.stem.lancaster import LancasterStemmer
import nltk
import re
from nltk.corpus import stopwords


def preProcessing(text):
    #nltk.download('all')
    #stopwords_python = ["str","init","self","and","del","from","not","while","as","elif","global","or","with","assert","else","if","pass","yield","break","except","import","print","class","exec","in","raise","continue","finally","is","return","def","for","lambda","try"];
    stemer = LancasterStemmer()
    if type(text) == str:
        text = text.lower()
        """text = re.sub('\"', '', text)
        text = re.sub('\'', '', text)
        text = re.sub('#', '', text)
        text = remove_marks(text)
        text = re.sub('[^a-zA-Z0-9]+', ' ', text)"""
        tokens = nltk.word_tokenize(text)
    else :
        tokens = text
    bagOfWords = {}
    limit_bagOfWords ={}
    for token in tokens:
        if token not in stopwords.words('english') and len(token) > 1:
            token = stemer.stem(token)
            if token in bagOfWords:
                bagOfWords[token] += 1
            else:
                bagOfWords[token] = 1
    return bagOfWords


def remove_marks(text):
    text = text.replace("á", "a")
    text = text.replace("à", "a")
    text = text.replace("ã", "a")
    text = text.replace("â", "a")
    text = text.replace("ç", "c")
    text = text.replace("í", "i")
    text = text.replace("ì", "i")
    text = text.replace("î", "i")
    text = text.replace("é", "e")
    text = text.replace("è", "e")
    text = text.replace("ê", "e")
    text = text.replace("ó", "o")
    text = text.replace("ò", "o")
    text = text.replace("ô", "o")
    text = text.replace("õ", "o")
    text = text.replace("ú", "u")
    text = text.replace("ù", "u")
    text = text.replace("û", "u")
    text = text.replace("ü", "u")

    text = text.replace("Á", "a")
    text = text.replace("À", "a")
    text = text.replace("Ã", "a")
    text = text.replace("Â", "a")
    text = text.replace("Ç", "c")
    text = text.replace("Í", "i")
    text = text.replace("Ì", "i")
    text = text.replace("Î", "i")
    text = text.replace("É", "e")
    text = text.replace("È", "e")
    text = text.replace("Ê", "e")
    text = text.replace("Ó", "o")
    text = text.replace("Ò", "o")
    text = text.replace("Õ", "o")
    text = text.replace("Ô", "o")
    text = text.replace("Ú", "u")
    text = text.replace("Ù", "u")
    text = text.replace("Û", "u")
    text = text.replace("Ü", "u")
    return text
