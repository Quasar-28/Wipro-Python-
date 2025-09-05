# Create a model that can predict the disease of cancer based on features given in the dataset. Use appropriate evaluation metrics. Dataset : cancer. csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

# 1. Load dataset
df = pd.read_csv("12_Regression_And_Classification/cancer.csv")

print("Shape:", df.shape)
print("Columns:", df.columns)

# 2. Handle missing values if present
df = df.dropna()   # or use fillna if you prefer imputing

# 3. Define features (X) and target (y)

target_col = "Diagnosis"  
X = df.drop(columns=[target_col])
y = df[target_col]

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Model training (Logistic Regression)
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# 7. Predictions
y_pred = model.predict(X_test_scaled)

# 8. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='weighted'))
print("Recall:", recall_score(y_test, y_pred, average='weighted'))
print("F1 Score:", f1_score(y_test, y_pred, average='weighted'))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))



# Create a model that can predict that the customer has purchased item or not based on features given in the dataset.Use appropriate evaluation metrics Dataset:Social_Ntetwork_Ads.csv 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

# 1. Load dataset
df = pd.read_csv("12_Regression_And_Classification/Social_Network_Ads.csv")

print("Shape:", df.shape)
print("Columns:", df.columns)

# 2. Handle missing values (if any)
df = df.dropna()

# 3. Define features (X) and target (y)

X = df.drop(columns=["Purchased"])
y = df["Purchased"]

# Encode categorical data (if Gender is present)
if "Gender" in X.columns:
    le = LabelEncoder()
    X["Gender"] = le.fit_transform(X["Gender"])

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Train model (Logistic Regression baseline)
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# 7. Predictions
y_pred = model.predict(X_test_scaled)

# 8. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
