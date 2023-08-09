# Sentiment Analysis-Alexa Amazon Reviews
## Applcation Demo Page
![image](https://github.com/S-shubham08/Sentiment-Analysis-amazon_reviews/assets/127888794/c4f20dcf-77d1-44b2-917b-04f7b26c8fe7)

## Project Description
This project implements sentiment analysis using the SpaCy natural language processing library and a Linear Support Vector Machine (SVM) classifier. The goal is to classify text into positive, negative, or neutral sentiments. The project also includes a Flask web application that allows users to input text and receive sentiment predictions.

### Installation:

1. Create a new Environment
```
conda create -p venv python=3.8 -y
```
2. Install the required packages
```
pip install -r requirements.txt
```

### Model Training
- Prepare the sentiment analysis dataset with labeled sentiment data.
- Implement text preprocessing using the SpaCy library.
- Train a Linear SVM classifier using the preprocessed text features.

### Usage
- Train the Linear SVM classifier using the SpaCy model and labeled sentiment data.
- Save the trained model for sentiment classification.

### Flask Web App
- Implement a Flask web application to create a user-friendly interface for sentiment analysis.
- Create a Python script app.py that loads the trained SVM model and provides an interface for users to input text and receive sentiment predictions.
