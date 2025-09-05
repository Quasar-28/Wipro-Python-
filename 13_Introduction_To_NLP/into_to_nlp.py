# Perform Text Preprocessing on SMSSpamCollection Dataset. The dataset can be downloaded from https://www.kaggle.com/datasets
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

# Load Kaggle CSV
df = pd.read_csv(
    '13_Introduction_To_NLP/spam.csv',
    usecols=[0,1],
    names=['label','message'],
    encoding='ISO-8859-1',
    skiprows=1
)

# Text preprocessing function
def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower()
    # Remove non-alphabetic characters
    text = re.sub(r'[^a-z\s]', '', text)
    # Tokenization
    tokens = word_tokenize(text)
    # Remove stopwords
    tokens = [w for w in tokens if w not in stopwords.words('english')]
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(w) for w in tokens]
    return " ".join(tokens)

# Apply preprocessing
df['clean_message'] = df['message'].apply(preprocess_text)
df = df[df['clean_message'] != ""]  # Remove empty messages

# TF-IDF vectorization
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['clean_message'])

# Encode labels
y = LabelEncoder().fit_transform(df['label'])  # 0=ham, 1=spam

print("TF-IDF shape:", X.shape)
print("Sample labels:", y[:10])
