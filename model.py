import re
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

tokenizer = Tokenizer(num_words=5000)
loaded_model = load_model('unethical_content_model.h5')

def preprocess_text(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\r', ' ', text)
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    return text

def is_unethical(sentence):
    # Preprocess the sentence
    sentence = preprocess_text(sentence)
    sentence_seq = tokenizer.texts_to_sequences([sentence])
    sentence_pad = pad_sequences(sentence_seq, maxlen=100, padding='post')

    # Predict
    prediction = loaded_model.predict(sentence_pad)
    return prediction[0][0] > 0.5


