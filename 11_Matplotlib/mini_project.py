"""
Use Case : Diabetes Prediction
Perform Exploratory Data Analysis for the Diabetes Dataset.
Dataset : Diabetes.csv
The dataset can be downloaded from https://www.kaggle.com/datasets
Perform the following tasks
1. Load the data in the DataFrame
2. Data Pre-processing
3. Handle the Categorical Data
4. Perform Uni-variate Analysis
5. Perform Bi-variate Analysis
"""
# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid", palette="muted", context="talk")

# 2. Load the Dataset
df = pd.read_csv("11_Matplotlib/diabetes.csv")   

print("Shape of dataset:", df.shape)
print("\nColumns:\n", df.columns)
print("\nMissing values:\n", df.isnull().sum())
print("\nData types:\n", df.dtypes)
print("\nBasic statistics:\n", df.describe())

# 3. Data Pre-processing
# Remove duplicates if any
df = df.drop_duplicates()

# Replace 0s with np.nan for columns where 0 is medically invalid
cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)

# Fill missing values with median of each column
df = df.fillna(df.median(numeric_only=True))

print("\nMissing values after cleaning:\n", df.isnull().sum())

# 4. Handle Categorical Data
# Outcome column is categorical (0 = Non-diabetic, 1 = Diabetic)
df['Outcome'] = df['Outcome'].astype('category')

print("\nUnique values in Outcome:", df['Outcome'].unique())

# 5. Uni-variate Analysis

# Distribution of Outcome
plt.figure(figsize=(6,4))
sns.countplot(x="Outcome", data=df, palette="Set2")
plt.title("Distribution of Diabetes Outcome (0=No, 1=Yes)")
plt.show()

# Histograms for all numeric features
df.hist(figsize=(15,12), bins=20, color='skyblue', edgecolor='black')
plt.suptitle("Feature Distributions", size=20)
plt.show()

# Boxplots to check outliers
plt.figure(figsize=(15,10))
for i, col in enumerate(df.columns[:-1], 1):
    plt.subplot(3, 3, i)
    sns.boxplot(y=df[col], color='lightblue')
    plt.title(col)
plt.tight_layout()
plt.show()

# 6. Bi-variate Analysis

# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Pairplot of selected features
sns.pairplot(df[['Glucose', 'BMI', 'Age', 'Outcome']], hue="Outcome", diag_kind="hist", palette="coolwarm")
plt.suptitle("Pairplot of Key Features", y=1.02)
plt.show()

# Boxplots of key features vs Outcome
plt.figure(figsize=(15,8))

plt.subplot(1,3,1)
sns.boxplot(x="Outcome", y="Glucose", data=df, palette="Set3")
plt.title("Glucose vs Outcome")

plt.subplot(1,3,2)
sns.boxplot(x="Outcome", y="BMI", data=df, palette="Set3")
plt.title("BMI vs Outcome")

plt.subplot(1,3,3)
sns.boxplot(x="Outcome", y="Age", data=df, palette="Set3")
plt.title("Age vs Outcome")

plt.tight_layout()
plt.show()

