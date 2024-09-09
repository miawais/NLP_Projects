#importing required libraries
import numpy as np
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

# Loading the IMDB dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Loading Pre-Trained Model
model = load_model('IMDB_RNN_MODEL.h5')

# Defining Helper Functions
# Function to Decode Reviews
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

# Function to preprocess user input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

# Prediction Function
def predict_sentiment(review):
    preprocessed_input = preprocess_text(review)
    prediction = model.predict(preprocessed_input)
    
    # Condition for Prediction
    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'
    return sentiment, prediction[0][0]

# Building The Streamlit App
st.title('SENTIMENT ANALYSIS')
st.write('Enter A Movie Review To Get Sentiment (Positive OR Negative)')

# User Input
user_input = st.text_area('Movie Review')

if st.button('Classify'):
    # Preprocess Input
    preprocessed_input = preprocess_text(user_input)
    
    # Make Prediction
    sentiment, prediction_score = predict_sentiment(user_input)
    
    # Display The Sentiment
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {prediction_score}')
else:
    st.write('Please Enter a Valid Movie Review')
