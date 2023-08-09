# Library imports
import pandas as pd
import numpy as np
import spacy
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import joblib
import string
from spacy.lang.en.stop_words import STOP_WORDS
from flask import Flask, request, jsonify, render_template
import nltk

from custom_tokenizer_function import CustomTokenizer

# Load trained Pipeline
model = joblib.load('model/sentiment_model.pkl')

stopwords = list(STOP_WORDS)

# Create the app object
app = Flask(__name__)

# Define predict function
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    new_review = [str(x) for x in request.form.values()]
    predictions = model.predict(new_review)[0]
    if predictions==0:
        return render_template('index.html', prediction_text='Negative')
    else:
        return render_template('index.html', prediction_text='Positive')


if __name__ == "__main__":
    app.run(debug=True)