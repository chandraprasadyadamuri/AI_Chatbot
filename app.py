import random
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
import panel as pn

# Initialize Panel extension
pn.extension(design="material")

# Download assets to match the backend environment
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()

# Load saved model assets
with open('chatbot_model.pkl', 'rb') as f:
    model_assets = pickle.load(f)
vectorizer = model_assets["vectorizer"]
classifier = model_assets["classifier"]
intents_data = model_assets["intents"]

def predict_intent(text: str):
    # Preprocess user input exactly how we trained it
    tokens = nltk.word_tokenize(text.lower().strip())
    cleaned_text = " ".join([lemmatizer.lemmatize(token) for token in tokens])
    
    # If the user typed an empty message or single special character, skip ML
    if not cleaned_text:
        return "fallback"
        
    # Vectorize and Predict
    text_vectorized = vectorizer.transform([cleaned_text])
    predicted_tag = classifier.predict(text_vectorized)[0]
    
    # Check max probability confidence
    probabilities = classifier.predict_proba(text_vectorized)[0]
    max_prob = max(probabilities)
    
    # Lowered confidence fallback buffer to 30% for a cleaner demo experience
    if max_prob < 0.30:
        return "fallback"
        
    return predicted_tag

def get_response(tag: str):
    if tag == "fallback":
        return "I'm sorry, I didn't quite catch that. Could you please rephrase?"
    for intent in intents_data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I am experiencing technical parsing issues."

def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    intent_tag = predict_intent(contents)
    bot_response = get_response(intent_tag)
    return bot_response

# Build visual frame layout
chat_interface = pn.chat.ChatInterface(
    callback=callback, 
    callback_user="AI Assistant",
    placeholder_text="Thinking...",
    show_clear=False,
    show_undo=False
)

template = pn.template.MaterialTemplate(
    title="AI Intent Classification Chatbot System",
    main=[chat_interface],
    header_background="#2196F3"
)

template.servable()