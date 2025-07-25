from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from model.preprocessing import clean_text
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

model = joblib.load('model/toxicity_model.pkl')
labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

@app.route('/')
def home():
    return "✅ Toxicity Predictor Backend is running."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    comment = data.get('text', '')
    cleaned = clean_text(comment)
    
    probas = model.predict_proba([cleaned])  # returns list of (n_labels) arrays
    result = {}
    for i, label in enumerate(labels):
        result[label] = round(probas[i][0][1] * 100, 2)

    result['safe'] = all(p < 50 for label, p in result.items())
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
