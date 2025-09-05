"""
Use Case : Sales Prediction
Create a model which will predict the sales based on campaigning expenses .
Dataset : Advertising.csv
The dataset can be downloaded from https://www.kaggle.com/datasets
Perform the following task.
· Load the data in the DataFrame.
· Perform Data Preprocessing
. Handle Categorical Data
· Perform Exploratory Data Analysis
. Build the model using Multiple Linear Regression
· Use the appropriate evaluation metrics
"""
# Sales Prediction using Multiple Linear Regression

# Step 1: Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Step 2: Load the dataset
df = pd.read_csv('12_Regression_And_Classification/Advertising.csv')  
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())

# Step 3: Data Preprocessing
# Check for missing values
print("\nMissing values in dataset:")
print(df.isnull().sum())

# Drop duplicates if any
df.drop_duplicates(inplace=True)

# Step 4: Exploratory Data Analysis (EDA)
# Pairplot
sns.pairplot(df)
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Distribution of Sales
sns.histplot(df['Sales'], kde=True)
plt.show()

# Step 5: Build Multiple Linear Regression Model
# Features and Target
X = df[['TV', 'Radio', 'Newspaper']]  # Adjust columns if dataset differs
y = df['Sales']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Step 6: Model Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Metrics:")
print(f"Mean Squared Error (MSE): {mse:.3f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.3f}")
print(f"Mean Absolute Error (MAE): {mae:.3f}")
print(f"R-squared (R2 Score): {r2:.3f}")

# Step 7: Visualize Predictions vs Actual
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()

# Step 8: Print model coefficients
print("\nModel Coefficients:")
coeff_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)
print(f"Intercept: {model.intercept_:.3f}")



"""
Use Case : Diabetes Prediction
Consider the PIMA Indians diabetes dataset. Create a Model for diabetes
prediction based on the features mentioned in the dataset.
Dataset : PIMA Indians diabetes dataset.
The dataset can be downloaded from https://www.kaggle.com/datasets
Perform the following tasks.
· Load the data in the DataFrame.
· Perform Data Preprocessing
· Perform Exploratory Data Analysis
. Build the model using Logistic Regression and K-Nearest Neighbour
· Use the appropriate evaluation metrics
"""

# Diabetes Prediction using Logistic Regression and K-Nearest Neighbors

# Step 1: Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

# Step 2: Load the dataset
df = pd.read_csv('12_Regression_And_Classification/diabetes.csv') 
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nDataset Description:")
print(df.describe())

# Step 3: Data Preprocessing
# Check for missing values
print("\nMissing values in dataset:")
print(df.isnull().sum())


features_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[features_with_zero] = df[features_with_zero].replace(0, np.nan)

# Fill missing values with median
df.fillna(df.median(), inplace=True)

# Step 4: Exploratory Data Analysis (EDA)
# Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Distribution of target variable 'Outcome'
sns.countplot(x='Outcome', data=df)
plt.title("Distribution of Diabetes Outcome")
plt.show()



# Step 5: Prepare Data for Modeling
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# Step 6: Logistic Regression Model
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

# Evaluation
print("Logistic Regression Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred_log))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log))
print("Classification Report:\n", classification_report(y_test, y_pred_log))

# ROC-AUC
y_prob_log = log_model.predict_proba(X_test)[:,1]
roc_auc_log = roc_auc_score(y_test, y_prob_log)
fpr, tpr, thresholds = roc_curve(y_test, y_prob_log)
plt.plot(fpr, tpr, label=f'Logistic Regression (AUC = {roc_auc_log:.2f})')
plt.plot([0,1], [0,1], 'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

# Step 7: K-Nearest Neighbors Model
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)

# Evaluation
print("K-Nearest Neighbors Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))
print("Classification Report:\n", classification_report(y_test, y_pred_knn))

# ROC-AUC for KNN
y_prob_knn = knn_model.predict_proba(X_test)[:,1]
roc_auc_knn = roc_auc_score(y_test, y_prob_knn)
fpr_knn, tpr_knn, thresholds_knn = roc_curve(y_test, y_prob_knn)
plt.plot(fpr_knn, tpr_knn, label=f'KNN (AUC = {roc_auc_knn:.2f})')
plt.plot([0,1], [0,1], 'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
