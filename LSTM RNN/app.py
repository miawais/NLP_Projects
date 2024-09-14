import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load LSTM RNN Model
model = load_model('Word_Predictor.h5')

# Load Tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Define max_sequence_len (adjust as needed)
max_sequence_len = 50  # Replace with the actual maximum sequence length used during model training

# Predict Function
def predict_next_word(model, tokenizer, input_text, max_sequence_len):
    if not input_text.strip():  # Handle empty input case
        return ""
    input_sequence = tokenizer.texts_to_sequences([input_text])
    input_sequence = pad_sequences(input_sequence, maxlen=max_sequence_len - 1, padding='pre')
    predictions = model.predict(input_sequence)
    predicted_index = np.argmax(predictions, axis=-1)
    predicted_word = tokenizer.index_word.get(predicted_index[0], "")
    return predicted_word

# Building Streamlit App
st.title("Next Word Predictor with LSTM RNN Model")

input_text = st.text_input("Enter Your Sentence to Predict Next Word")

if st.button("Predict Next Word"):
    if input_text:
        next_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
        st.write(f'Next Word: {next_word}')
    else:
        st.write("Please enter a sentence.")
