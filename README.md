# 🤖 AI Chatbot Project

## 📌 Project Overview

This project is an NLP-based AI chatbot developed using Python and a web-based deployment framework. The chatbot accurately predicts user intent from natural language text inputs and generates suitable replies using a trained Machine Learning classifier.

The system utilizes Natural Language Processing (NLP) techniques to clean user messages, maps them to contextual categories via a trained classification model, and delivers predefined retrieval-based responses through an interactive web interface.

---

## 🚀 Features

- **NLP-Based Text Processing:** Normalizes text through tokenization and lemmatization.
- **Intent Classification:** Uses Machine Learning algorithms to identify user intent.
- **Retrieval-Based Responses:** Returns predefined responses based on detected intent.
- **Web API Support:** Backend API built using FastAPI.
- **Interactive Chat Interface:** Responsive chatbot UI using Panel.
- **Automated Training Pipeline:** Train and save the chatbot model with a single script.
- **JSON-Based Intent Dataset:** Easy-to-expand dataset structure.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| NLTK | Natural Language Processing |
| Scikit-Learn | Machine Learning |
| FastAPI | Backend API Development |
| Panel | Interactive Chat Interface |
| JSON | Intent Dataset Storage |
| Pickle | Model Serialization |

---

## 📁 Project Structure

```text
AI-Chatbot-Project/
│
├── app.py                 # Panel-based chatbot UI
├── main.py                # FastAPI backend API
├── train.py               # Model training script
├── intents.json           # Intent dataset
├── chatbot_model.pkl      # Trained model file
├── README.md              # Project documentation
│
├── screenshots/           # Project screenshots
└── demo/                  # Demo video files
```

---

## 📊 How the Project Works

### 1. User Input
The user enters a message through the chatbot interface.

### 2. NLP Preprocessing
The message is:
- Converted to lowercase
- Tokenized using NLTK
- Lemmatized using WordNet Lemmatizer

### 3. Feature Engineering
The cleaned text is converted into numerical vectors using **TF-IDF Vectorization**.

### 4. Intent Classification
A **Logistic Regression Classifier** predicts the most suitable intent.

### 5. Confidence Evaluation
If the prediction confidence is above the threshold, the intent is accepted. Otherwise, the chatbot returns a fallback response.

### 6. Response Generation
A random response corresponding to the predicted intent is returned to the user.

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/AI-Chatbot-Project.git
cd AI-Chatbot-Project
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install nltk
pip install scikit-learn
pip install fastapi
pip install uvicorn
pip install panel
```

Or:

```bash
pip install -r requirements.txt
```

---

## 🏋️ Train the Chatbot Model

Run:

```bash
python train.py
```

Expected Output:

```text
🏆 Model successfully re-trained with lowercase matching!
```

This creates:

```text
chatbot_model.pkl
```

---

## ▶️ Run the FastAPI Backend

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 💬 Run the Chatbot UI

```bash
panel serve app.py --port 9000 --show
```

Open:

```text
http://localhost:9000/app
```

---

## 📡 API Example

### Request

```json
{
  "message": "Hello"
}
```

### Response

```json
{
  "user_message": "Hello",
  "predicted_intent": "greeting",
  "bot_response": "Hello! How can I help you today?"
}
```

---

## 🧪 Sample Test Cases

### Greeting

**Input**

```text
Hello there!
```

**Expected Output**

```text
Hello! How can I help you today?
```

### Business Hours

**Input**

```text
What are your timings?
```

**Expected Output**

```text
We are open from 9 AM to 6 PM, Monday through Friday.
```

### Support Request

**Input**

```text
I need help
```

**Expected Output**

```text
You can reach our support team for assistance.
```

### Fallback Scenario

**Input**

```text
Can I buy a slice of pizza?
```

**Expected Output**

```text
I'm sorry, I didn't quite catch that. Could you please rephrase?
```

---

## 📋 Deliverables Checklist

| Deliverable | Status |
|-------------|--------|
| Intent Dataset (`intents.json`) | ✅ Completed |
| Model Training Pipeline (`train.py`) | ✅ Completed |
| Machine Learning Classifier | ✅ Completed |
| Response Generation Logic | ✅ Completed |
| FastAPI Backend (`main.py`) | ✅ Completed |
| Panel Chat Interface (`app.py`) | ✅ Completed |
| NLP Preprocessing Pipeline | ✅ Completed |
| Trained Model File (`chatbot_model.pkl`) | ✅ Completed |
| GitHub Repository Documentation | ✅ Completed |

---

## ✨ Features Implemented

- Intent Classification using Machine Learning
- TF-IDF Feature Extraction
- Logistic Regression Classifier
- NLTK-based Text Processing
- FastAPI REST API
- Panel Interactive UI
- Confidence-Based Fallback Responses
- Expandable Intent Dataset
- Randomized Response Selection

---

## 🔮 Future Enhancements

### 🎙️ Voice Assistant Integration
Convert speech input into text using Speech Recognition APIs.

### 🗄️ Database Integration
Store and retrieve chat history using SQL or NoSQL databases.

### 🧠 Deep Learning Models
Upgrade from Logistic Regression to Transformer-based architectures.

### 🌍 Multi-language Support
Enable chatbot interaction in multiple regional and international languages.

### ☁️ Cloud Deployment
Deploy the chatbot on cloud platforms such as AWS, Azure, or GCP.

---

## 📚 Learning Outcomes

This project demonstrates:

- Natural Language Processing (NLP)
- Text Classification
- Machine Learning Model Development
- FastAPI API Development
- Interactive Dashboard Creation
- Model Serialization with Pickle
- Chatbot Design and Deployment

---

## 👨‍💻 Author

**Y CHANDRA PRASAD **

**Department:** Computer Science & Engineering

**Institution:** JNTUACEK

---

## ⭐ Project Summary

The AI Chatbot Project successfully combines NLP, Machine Learning, FastAPI, and Panel to create an intelligent conversational assistant capable of identifying user intent and providing meaningful responses through both API and web-based interfaces.
