# 🚦 ToxicMeter – Toxicity Predictor

**ToxicMeter** is a full-stack web application that predicts the toxicity level of user-entered text. It analyzes text for various toxic traits such as insults, threats, and identity-based hate using a trained machine learning model. The goal is to provide users with real-time feedback on the toxicity of their input in an intuitive and visually engaging format.

---

## 🔍 Overview

This application allows users to enter any sentence or paragraph, and instantly receive a breakdown of how toxic the text is. The output highlights different toxicity categories with color-coded indicators — making it simple to understand and interpret.

The app uses a trained machine learning model behind the scenes to make accurate predictions. It has two main parts:

- A **frontend** built with HTML, CSS, and JavaScript
- A **backend** powered by **Flask (Python)** that processes input and returns predictions from a pre-trained model

---

## ✨ Key Features

- Supports **six toxicity categories**:
  - `toxic`, `severe_toxic`, `obscene`, `threat`, `insult`, `identity_hate`
- Displays **percent scores** for each category
- Simple and clean **user interface**
- Color-coded output:
  - 🟢 Low (<30%)
  - 🟡 Medium (30–70%)
  - 🔴 High (>70%)
- Tag for **safe input** if all scores are low

---

## ⚙️ How It Works

1. The user types text into the input box.
2. On clicking **"Analyze"**, the text is sent to the Flask backend via a POST request.
3. The backend:
   - Cleans the input text
   - Converts it into TF-IDF vectors
   - Uses a trained logistic regression model to make predictions
4. The result is sent back to the frontend and visualized for the user.

---

## 🛠️ Project Structure

toxicity-predictor/
├── app.py # Flask backend (API)
├── index.html # Frontend interface
├── styles.css # Styling
├── script.js # JS logic (API calls + DOM updates)
├── requirements.txt # Python dependencies
├── train.py # Script to train the ML model
├── model/
│ ├── toxicity_model.pkl # Saved trained model
│ └── preprocessing.py # Text cleaning function
└── README.md # You're reading it!

markdown
Copy
Edit

---

## 🧠 Training the Model

The machine learning model used in this project was trained on the **Jigsaw Toxic Comment Classification** dataset from Kaggle. It is a multi-label classification problem where each comment can belong to more than one toxicity category.

The training steps (in `train.py`) are:

- Load and preprocess the dataset
- Clean the text (remove punctuation, lowercase, lemmatize)
- Vectorize text using **TF-IDF**
- Train a `OneVsRestClassifier` with **Logistic Regression**
- Save the trained model as `toxicity_model.pkl`

To retrain the model:

```bash
python train.py
📦 Technologies Used
🔹 Frontend
HTML5

CSS3

JavaScript (Vanilla)

🔹 Backend
Python 3

Flask

Flask-CORS

scikit-learn

NLTK

joblib
```
