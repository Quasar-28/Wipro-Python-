# Data preprocessing assignments
# Data preprocessing using Sk-learn

"""
Assignment 1 : 
Perform Data Preprocessing on melb_data.csv dataset with statistical perspective. 
The dataset can be downloaded from https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download
"""
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

df = pd.read_csv("10_Data_Preprocessing/melb_data.csv")
print("Initial Shape:", df.shape)
print("\nMissing Values before handling:\n", df.isnull().sum())
num_imputer = SimpleImputer(strategy="median")
df[df.select_dtypes(include=np.number).columns] = num_imputer.fit_transform(df.select_dtypes(include=np.number))
cat_imputer = SimpleImputer(strategy="most_frequent")
df[df.select_dtypes(include="object").columns] = cat_imputer.fit_transform(df.select_dtypes(include="object"))
print("\nMissing Values after handling:\n", df.isnull().sum().sum())
if "Address" in df.columns:
    df.drop(columns=["Address"], inplace=True)
for col in df.select_dtypes(include="object").columns:
    freq = df[col].value_counts()
    rare = freq[freq < 50].index
    df[col] = df[col].replace(rare, "Other")
label_enc = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = label_enc.fit_transform(df[col])

print("\nShape after encoding categorical data:", df.shape)
scaler = StandardScaler()
numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("\nFinal Shape after preprocessing:", df.shape)
print(df.head())


# Data preprocessing using Pandas
"""
Assignment 2 : 
Perform Data Preprocessing on melb_data.csv dataset with statistical perspective. 
The dataset can be downloaded from https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download
"""
import pandas as pd
import numpy as np


df = pd.read_csv("10_Data_Preprocessing/melb_data.csv")

print("Initial Shape:", df.shape)
print("\nMissing Values before handling:\n", df.isnull().sum())


for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median()) 

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0]) 

print("\nMissing Values after handling:\n", df.isnull().sum().sum())


if "Address" in df.columns:
    df.drop(columns=["Address"], inplace=True)

def group_rare_categories(series, threshold=50):
    freq = series.value_counts()
    rare = freq[freq < threshold].index
    return series.replace(rare, "Other")

for col in df.select_dtypes(include="object").columns:
    df[col] = group_rare_categories(df[col])

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype("category").cat.codes

print("\nShape after encoding categorical data:", df.shape)


numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()

print("\nFinal Shape after preprocessing:", df.shape)
print(df.head())
