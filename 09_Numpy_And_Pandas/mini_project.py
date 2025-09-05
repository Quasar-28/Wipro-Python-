"""
Use Case: Perform the Outlier detection for the given dataset i.e. datasetExample
Dataset : datasetExample.csv
Perform the following task :
 . Load the data in the DataFrame.
 · Detection of Outliers
"""
import pandas as pd
import numpy as np

df = pd.read_csv("09_Numpy_And_Pandas/datasetExample.csv")

def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    mask = (data[column] < lower) | (data[column] > upper)
    return data[mask]

numeric_cols = df.select_dtypes(include=[np.number]).columns

all_outliers = pd.DataFrame() 

for col in numeric_cols:
    outliers = detect_outliers_iqr(df, col)
    if not outliers.empty:   # if outliers exist
        print(f"\nOutliers in column {col}:")
        print(outliers)
        all_outliers = pd.concat([all_outliers, outliers])

# Removing duplicates 
all_outliers = all_outliers.drop_duplicates()

print("\nAll detected outliers in dataset:")
print(all_outliers)
