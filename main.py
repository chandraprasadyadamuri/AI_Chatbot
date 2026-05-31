import random
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="AI Intent Classification Chatbot API")

lemmatizer = WordNetLemmatizer()

# Load the saved model assets
try:
    with open('chatbot_model.pkl', 'rb') as f:
        model_assets = pickle.load(f)
    vectorizer = model_assets["vectorizer"]
    classifier = model_assets["classifier"]
    intents_data = model_assets["intents"]
except FileNotFoundError:
    print("❌ Error: 'chatbot_model.pkl' not found. Please run 'train.py' first.")

# Define the request body structure
class UserMessage(BaseModel):
    message: str

def predict_intent(text: str):
    # Preprocess incoming text
    tokens = nltk.word_tokenize(text.lower())
    cleaned_text = " ".join([lemmatizer.lemmatize(token) for token in tokens])
    
    # Vectorize and Predict
    text_vectorized = vectorizer.transform([cleaned_text])
    predicted_tag = classifier.predict(text_vectorized)[0]
    
    # Get prediction probabilities
    probabilities = classifier.predict_proba(text_vectorized)[0]
    max_prob = max(probabilities)
    
    # Fallback response threshold if the confidence score is too low (e.g., < 40%)
    if max_prob < 0.40:
        return "fallback"
        
    return predicted_tag

def get_response(tag: str):
    if tag == "fallback":
        return "I'm sorry, I didn't quite catch that. Could you please rephrase?"
    
    for intent in intents_data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I am experiencing some internal issues parsing that."

@app.post("/chat")
async def chat_endpoint(user_input: UserMessage):
    intent_tag = predict_intent(user_input.message)
    bot_response = get_response(intent_tag)
    
    return {
        "user_message": user_input.message,
        "predicted_intent": intent_tag,
        "bot_response": bot_response
    }

@app.get("/")
async def root():
    return {"status": "Chatbot API is online!"}