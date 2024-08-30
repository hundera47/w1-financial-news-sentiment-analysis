import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import spacy
import gensim
from gensim import corpora

# Download NLTK data if not already present
nltk.download('vader_lexicon')
nltk.download('stopwords')

# Load the English language model for spacy
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("SpaCy model 'en_core_web_sm' not found. Please install it using 'python -m spacy download en_core_web_sm'.")
