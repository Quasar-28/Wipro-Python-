# Perform Exploratory Data Analysis for the dataset Mall_Customers. The dataset can be downloaded from https://www.kaggle.com/datasets

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("11_Matplotlib/Mall_Customers.csv")

# Basic info
print("Dataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

# Style
sns.set(style="whitegrid")

# 1. Gender Distribution (Countplot + Pie Chart)
plt.figure(figsize=(6,4))
sns.countplot(x="Gender", data=df, palette="Set2")
plt.title("Gender Distribution")
plt.show()

plt.figure(figsize=(6,6))
df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', colors=['skyblue','pink'], startangle=90)
plt.title("Gender Distribution (Pie)")
plt.ylabel("")
plt.show()

# 2. Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=15, kde=True, color='teal')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# 3. Annual Income Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Annual Income (k$)'], bins=15, kde=True, color='orange')
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Count")
plt.show()

# 4. Spending Score Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Spending Score (1-100)'], bins=15, kde=True, color='purple')
plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Count")
plt.show()

# 5. Age vs Spending Score (Scatter)
plt.figure(figsize=(8,6))
sns.scatterplot(x='Age', y='Spending Score (1-100)', hue='Gender', data=df, palette='Set1')
plt.title("Age vs Spending Score")
plt.show()
# 6. Annual Income vs Spending Score (Scatter)
plt.figure(figsize=(8,6))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender', data=df, palette='Set2')
plt.title("Annual Income vs Spending Score")
plt.show()
# 7. Boxplots (to check outliers)
plt.figure(figsize=(10,6))
sns.boxplot(x="Gender", y="Age", data=df, palette="Set3")
plt.title("Age Distribution by Gender")
plt.show()
plt.figure(figsize=(10,6))
sns.boxplot(x="Gender", y="Annual Income (k$)", data=df, palette="Set2")
plt.title("Annual Income Distribution by Gender")
plt.show()
plt.figure(figsize=(10,6))
sns.boxplot(x="Gender", y="Spending Score (1-100)", data=df, palette="Set1")
plt.title("Spending Score Distribution by Gender")
plt.show()


# Perform Exploratory Data Analysis for the dataset salary_data. The dataset can be downloaded from https://www.kaggle.com/datasets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv("11_Matplotlib/salary_data.csv")  

# 2. Basic overview
print("Shape:", df.shape)
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())
print("\nStatistical Summary:\n", df.describe(include='all'))

# 3. Clean column names (strip spaces)
df.rename(columns=lambda x: x.strip(), inplace=True)

# Set Seaborn style
sns.set(style="whitegrid", context="talk")

# 4. Univariate Analysis

# 4a. Salary distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Salary'], bins=30, kde=True, color='teal')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()

# 4b. Years of Experience distribution
if 'Years of Experience' in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df['Years of Experience'], bins=20, kde=True, color='orange')
    plt.title("Years of Experience Distribution")
    plt.xlabel("Years of Experience")
    plt.ylabel("Count")
    plt.show()

# 4c. Age distribution
if 'Age' in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df['Age'], bins=20, kde=True, color='purple')
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()

# 4d. Categorical columns (Gender, Education Level)
for col in ['Gender', 'Education Level', 'Job Title']:
    if col in df.columns:
        plt.figure(figsize=(10,5))
        sns.countplot(y=col, data=df, order=df[col].value_counts().index, palette='Set2')
        plt.title(f"{col} Distribution")
        plt.xlabel("Count")
        plt.ylabel(col)
        plt.tight_layout()
        plt.show()

# 5. Bivariate Analysis with Salary

# 5a. Salary vs Years of Experience
if 'Years of Experience' in df.columns:
    plt.figure(figsize=(8,6))
    sns.scatterplot(x='Years of Experience', y='Salary', data=df, hue='Education Level', palette='viridis', alpha=0.7)
    plt.title("Salary vs Years of Experience")
    plt.show()

# 5b. Salary vs Age
if 'Age' in df.columns:
    plt.figure(figsize=(8,6))
    sns.scatterplot(x='Age', y='Salary', data=df, hue='Gender', palette='coolwarm', alpha=0.7)
    plt.title("Salary vs Age")
    plt.show()

# 5c. Boxplots for Salary across categorical columns
for col in ['Education Level', 'Gender']:
    if col in df.columns:
        plt.figure(figsize=(8,6))
        sns.boxplot(x=col, y='Salary', data=df, palette='Set3')
        plt.title(f"Salary by {col}")
        plt.show()

# 6. Optional: Pairplot for numeric features
num_cols = [c for c in df.select_dtypes(include='number').columns if c != 'Salary']
if num_cols:
    sns.pairplot(df, vars=num_cols + ['Salary'], hue='Gender' if 'Gender' in df.columns else None, corner=True)
    plt.suptitle("Pairplot of Numeric Features ↔ Salary", y=1.02)
    plt.show()


# Perform Exploratory Data Analysis for the dataset Social Network Ads. The dataset can be downloaded from https://www.kaggle.com/datasets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("11_Matplotlib/Social_Network_Ads.csv")  

# 2. Initial inspection
print("Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Summary:\n", df.describe(include='all'))

# 3. Clean column names
df.rename(columns=lambda x: x.strip(), inplace=True)

# Set Seaborn aesthetic style
sns.set(style="whitegrid", palette="muted", context="talk")

# 4. Univariate Analysis

# 4a. Age distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# 4b. Estimated Salary distribution
plt.figure(figsize=(8,5))
sns.histplot(df['EstimatedSalary'], bins=20, kde=True, color='orange')
plt.title("Estimated Salary Distribution")
plt.xlabel("Estimated Salary")
plt.ylabel("Count")
plt.show()

# 4c. Purchase Count
plt.figure(figsize=(6,4))
sns.countplot(x='Purchased', data=df, palette='Set2')
plt.title("Purchased Count (0 = No, 1 = Yes)")
plt.xlabel("Purchased")
plt.ylabel("Count")
plt.show()

# 5. Bivariate Analysis

# 5a. Age vs EstimatedSalary colored by Purchased
plt.figure(figsize=(8,6))
sns.scatterplot(x='Age', y='EstimatedSalary', hue='Purchased', data=df, palette='coolwarm', alpha=0.7)
plt.title("Age vs Estimated Salary by Purchased")
plt.show()

# 5b. Boxplots for Age and EstimatedSalary by purchase category
plt.figure(figsize=(12,5))
plt.subplot(1, 2, 1)
sns.boxplot(x='Purchased', y='Age', data=df, palette='Set3')
plt.title("Age by Purchase Outcome")

plt.subplot(1, 2, 2)
sns.boxplot(x='Purchased', y='EstimatedSalary', data=df, palette='Set3')
plt.title("Estimated Salary by Purchase Outcome")
plt.tight_layout()
plt.show()

# 6. Pairplot for numeric features with Purchased hue
sns.pairplot(df, vars=['Age', 'EstimatedSalary'], hue='Purchased', diag_kind='hist', palette='coolwarm')
plt.suptitle("Pairplot of Features by Purchase", y=1.02)
plt.show()
