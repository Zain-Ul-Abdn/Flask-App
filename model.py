import re
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Function to preprocess text
def preprocess_text(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\r', ' ', text)
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    return text

# Function to preprocess input sentence and make prediction
def is_unethical(sentence):
    # Load the tokenizer
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)

    # Preprocess the sentence
    sentence = preprocess_text(sentence)
    sentence_seq = tokenizer.texts_to_sequences([sentence])
    sentence_pad = pad_sequences(sentence_seq, maxlen=100, padding='post')

    # Load the trained model
    model = load_model('unethical_content_model.h5')

    # Predict
    prediction = model.predict(sentence_pad)
    return prediction[0][0] >= 0.5


