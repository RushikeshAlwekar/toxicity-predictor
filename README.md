# 🚦 ToxicMeter – Toxicity Predictor

**ToxicMeter** is a simple web application that predicts the toxicity levels of any given text using a machine learning model trained on the Jigsaw Toxic Comment dataset. It highlights different types of toxic behavior in real time.

---

## 🧠 Features

- Detects six types of toxicity:
  - `toxic`
  - `severe_toxic`
  - `obscene`
  - `threat`
  - `insult`
  - `identity_hate`
- Color-coded result visualization:
  - 🟢 Green: Low toxicity
  - 🟡 Yellow: Medium
  - 🔴 Red: High toxicity
- Simple UI for fast interaction
- REST API backend with Flask
- Model predictions using scikit-learn

---

## 🗂️ Project Structure

toxicity-predictor/
├── app.py # Flask backend
├── index.html # Frontend HTML
├── styles.css # Frontend CSS
├── script.js # Frontend JavaScript
├── requirements.txt # Python dependencies
├── model/
│ ├── toxicity_model.pkl # Trained ML model
│ └── preprocessing.py # Text cleaning function
└── README.md

yaml
Copy
Edit

---

## ⚙️ How It Works

1. User enters a text in the web interface.
2. Frontend sends a POST request to `/predict` endpoint.
3. Flask backend:
   - Cleans the text
   - Feeds it to the trained model
   - Returns probability scores for each toxic trait
4. Frontend displays results with intuitive visuals.

---

## 🚀 Deployment

### 🔹 Backend (Flask Web Service)

- **Hosting**: [Render](https://render.com)
- **Start Command**:  
  python app.py

markdown
Copy
Edit

- **Builds from**: root directory
- **Environment**:
- No special environment variables needed unless setting `PORT` manually
- **Requirements**: defined in `requirements.txt`

### 🔹 Frontend (Static Site)

- **Hosting**: Render Static Site
- **Root Directory**: `./`
- **Build Command**: _(leave blank)_
- **Publish Directory**: `./`

> ✅ **Important**: In `script.js`, update the fetch URL from `http://127.0.0.1:10000/predict` to your deployed backend URL:

```js
const response = await fetch("https://your-backend-name.onrender.com/predict", {
method: "POST",
headers: {
  "Content-Type": "application/json",
},
body: JSON.stringify({ text: input }),
});
💻 Run Locally
Clone the repository:

bash
Copy
Edit
git clone https://github.com/<your-username>/toxicity-predictor.git
cd toxicity-predictor
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Start the Flask server:

bash
Copy
Edit
python app.py
Open index.html in your browser to use the frontend locally.

📦 Dependencies
Flask

Flask-CORS

scikit-learn

nltk

joblib

Install with:

bash
Copy
Edit
pip install -r requirements.txt
```
