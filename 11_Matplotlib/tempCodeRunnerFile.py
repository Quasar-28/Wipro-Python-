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