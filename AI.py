import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.optimizers import Adam


data = pd.read_csv('Provide Dataset Here')

# Combine all toxic labels into one
data['unethical'] = data[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].max(axis=1)
 
# Keep only the necessary columns
data = data[['comment_text', 'unethical']]

# Preprocess the text
def preprocess_text(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\r', ' ', text)
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    return text

data['comment_text'] = data['comment_text'].apply(preprocess_text)

# Split the data
X = data['comment_text'].values
y = data['unethical'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tokenize the text
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

# Pad the sequences
max_length = 100
X_train_pad = pad_sequences(X_train_seq, maxlen=max_length, padding='post')
X_test_pad = pad_sequences(X_test_seq, maxlen=max_length, padding='post')

# Define the model
model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=128, input_length=max_length))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

# Train the model
epochs = 5  # You can increase this for better performance
batch_size = 64

history = model.fit(X_train_pad, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.1, verbose=1)

model.save('/content/drive/My Drive/unethical_content_model.h5')