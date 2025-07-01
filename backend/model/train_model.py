import pandas as pd
import nltk
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from preprocessing import clean_text

nltk.download('stopwords')

# Load and clean data
df = pd.read_csv('data/train.csv')
df['comment_text'] = df['comment_text'].fillna('').apply(clean_text)

labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
X = df['comment_text']
y = df[labels]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=10000)),
    ('clf', MultiOutputClassifier(LogisticRegression(max_iter=1000)))
])

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, 'backend/model/toxicity_model.pkl')
print("✅ Model trained and saved with severity support.")
