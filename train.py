import json
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Explicitly download assets
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()

# 1. Load the dataset
with open('intents.json', 'r') as f:
    intents_data = json.load(f)

X = []  
y = []  

for intent in intents_data['intents']:
    for pattern in intent['patterns']:
        # Tokenize and clean text
        tokens = nltk.word_tokenize(pattern.lower())
        cleaned_pattern = " ".join([lemmatizer.lemmatize(token) for token in tokens])
        
        X.append(cleaned_pattern)
        y.append(intent['tag'])

# 2. Vectorize the text data (add lowercase=False since we already did it manually)
vectorizer = TfidfVectorizer(lowercase=False)
X_vectorized = vectorizer.fit_transform(X)

# 3. Train the Classifier
classifier = LogisticRegression(max_iter=200)
classifier.fit(X_vectorized, y)

# 4. Save the trained model, vectorizer, and original dataset configuration
model_assets = {
    "vectorizer": vectorizer,
    "classifier": classifier,
    "intents": intents_data
}

with open('chatbot_model.pkl', 'wb') as f:
    pickle.dump(model_assets, f)

print("🏆 Model successfully re-trained with lowercase matching!")