import numpy as np
import pandas as pd
import pickle
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import py_vncorenlp

vncore = py_vncorenlp.VnCoreNLP(save_dir="../Model", annotators=["wseg"], max_heap_size='-Xmx500m')

def vncore_process(data):
    #py_vncorenlp.download_model(save_dir='./Model') #install py_vncorenlp
    return vncore.word_segment(data)

def transform_text(text, shortwords_dict):
    # Pattern to match URLs
    text = re.sub(r'http[s]?://\S+', 'link', text)
    
    # Pattern to match 10-digit phone numbers
    text = re.sub(r'\b\d{10}\b', 'phone_number', text)
    
    # Remove duplicated characters at the end of words
    text = re.sub(r'(\w)\1+\b', r'\1', text)
    
    # Replace words exactly with their corresponding replacements
    for word, replacement in shortwords_dict.items():
        text = re.sub(r'\b' + re.escape(word) + r'\b', replacement, text)   
    return text

def preprocess(data):
    # Process data
    shortwords_dict = pd.read_csv("../Data/vietnamese_shortwords.csv", sep=';', header=None, index_col=0).squeeze().to_dict()
    if isinstance(data, pd.Series):
        data = data.apply(lambda x: transform_text(str(x).lower(), shortwords_dict))
        data = data.apply(lambda x: vncore_process(x))
        data = data.apply(' '.join)
    else:  # If the input is a single text entry
        data = transform_text(data.lower(), shortwords_dict)
        data = vncore_process(data)
        data = ' '.join(data)
    return data

def countVectorizer_fit(data):
    #Load precessed_data
    processed_data = preprocess(data)
    # Load stopwords
    stopwords = pd.read_csv("../Data/vietnamese_stopwords.csv", header=None).squeeze().tolist()

    # Vectorize text
    vectorizer = CountVectorizer(stop_words=stopwords)
    data_vectorized = vectorizer.fit_transform(processed_data)
    return vectorizer, data_vectorized
    
def tfidfVectorizer_fit(data):
    #Load precessed_data
    processed_data = preprocess(data)
    # Load stopwords
    stopwords = pd.read_csv("../Data/vietnamese_stopwords.csv", header=None).squeeze().tolist()

    # Vectorize text
    vectorizer = TfidfVectorizer(stop_words=stopwords)
    data_vectorized = vectorizer.fit_transform(processed_data)
    return vectorizer, data_vectorized
