"""
Use Case: Rating Prediction
Create a model that will predict the rating based on the feedback of the
customer.
Feature: Text
Label: Stars
Dataset: yelp.csv
The dataset can be downloaded from https://www.kaggle.com/datasets
"""
# Rating Prediction from Customer Feedback (Text)

# Step 1: Import Libraries
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Step 2: Load Dataset
df = pd.read_csv('13_Introduction_To_NLP/yelp.csv')  
print("First 5 rows:")
print(df[['text','stars']].head())

# Step 3: Text Preprocessing Function
def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # Remove punctuation/numbers
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stopwords.words('english')]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(w) for w in tokens]
    return " ".join(tokens)

# Step 4: Apply Preprocessing
df['clean_text'] = df['text'].apply(preprocess_text)
df = df[df['clean_text'] != ""]  # Remove empty reviews

# Step 5: Convert Text to TF-IDF Features
tfidf = TfidfVectorizer(max_features=5000)  # Limit features for performance
X = tfidf.fit_transform(df['clean_text'])

# Step 6: Label
y = df['stars']  # Ratings

# Step 7: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 8: Build Model (Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)

# Step 9: Predictions
y_pred = model.predict(X_test)

# Step 10: Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")
