# 🚦 ToxicMeter – Toxicity Predictor

**ToxicMeter** is a lightweight web application that predicts and visualizes the level of toxicity in a given piece of text. It uses a machine learning model trained on the Jigsaw Toxic Comment dataset and provides real-time classification for six different types of toxic behaviors.

---

## 🧠 Features

- Detects 6 types of toxicity:
  - ☣️ `toxic`
  - 💢 `severe_toxic`
  - 🤬 `obscene`
  - 🔪 `threat`
  - 😤 `insult`
  - 👥 `identity_hate`
- Clean and responsive UI
- Traffic-light color-coded display:
  - 🟢 Low (Safe)
  - 🟡 Moderate
  - 🔴 High toxicity
- Real-time predictions using a scikit-learn model
- Lightweight Flask backend with REST API
- JS-powered frontend interaction

---

## 🔁 Workflow

1. **User inputs text** via the interface.
2. **Frontend (`script.js`)** sends a `POST` request to the `/predict` API.
3. **Flask backend (`app.py`)**:
   - Receives the text
   - Cleans it using `preprocessing.py`
   - Feeds it to the trained model (`toxicity_model.pkl`)
   - Returns probability scores for each toxicity label
4. **Frontend** visualizes each label with color-coded indicators.
5. If all labels are below 50%, the app marks the text as **safe ✅**.

---

> Designed to be simple, fast, and informative for identifying toxic language in real time.
