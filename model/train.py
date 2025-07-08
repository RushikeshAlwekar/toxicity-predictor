# train.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

from model.preprocessing import clean_text

# 1. Load dataset
data = pd.read_csv("train.csv")

# 2. Preprocess text
data['cleaned_text'] = data['comment_text'].apply(clean_text)

# 3. Define features and labels
X = data['cleaned_text']
y = data[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']]

# 4. Split data (optional)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Build pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=10000, ngram_range=(1,2))),
    ('clf', OneVsRestClassifier(LogisticRegression(solver='liblinear')))
])

# 6. Train model
pipeline.fit(X_train, y_train)

# 7. Save model
os.makedirs("model", exist_ok=True)
joblib.dump(pipeline, "model/toxicity_model.pkl")

print("✅ Model trained and saved to model/toxicity_model.pkl")
