# minor project - data preprocessing
"""
Use-Case : House Price Prediction
Dataset : melb_data.csv
The dataset can be downloaded melb_data.csv Kaggle
Perform the following tasks:
1. Load the data in dataframe (Pandas)
2. Handle inappropriate data
3. Handle the missing data
4. Handle the categorical data
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("10_Data_Preprocessing/melb_data.csv")
print("Initial Shape:", df.shape)
df.drop(columns=["Address", "Unnamed: 0"], inplace=True, errors="ignore")
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("Missing values after handling:", df.isnull().sum().sum())
label_enc = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = label_enc.fit_transform(df[col])

print("Final Shape:", df.shape)
print(df.head())
