# Pandas Assignments

"""
Exercise 3: Pandas-DataFrame
Download the data set and rename to cars.csv
Link : Dataset: https://www.kaggle.com/uciml/autompg-dataset/data?select=auto-mpg.csv
or https://archive.ics.uci.edu/ml/datasets/Auto+MPG
a. Import Pandas
b. Import the Cars Dataset and store the Pandas DataFrame in the variable cars
c. Inspect the first 10 Rows of the DataFrame cars
d. Inspect the DataFrame cars by "printing" cars
e. Inspect the last 5 Rows
f. Get some meta information on our DataFrame!
"""
# a. Import Pandas
# import pandas as pd

# # b. Import the Cars Dataset
# cars = pd.read_csv("09_Numpy_And_Pandas/cars.csv") 

# # c. Inspect the first 10 Rows
# print("First 10 rows:")
# print(cars.head(10))

# # d. Inspect the DataFrame cars
# print("\nComplete DataFrame:")
# print(cars)

# # e. Inspect the last 5 Rows
# print("\nLast 5 rows:")
# print(cars.tail(5))

# # f. Get some meta information on our DataFrame
# print("\nMeta information:")
# print(cars.info())


"""
Exercise 4 : Download 50_startups dataset
Link : https://www.kaggle.com/datasets/farhanmd29/50-startups
a. Create DataFrame using Pandas
b. Read the data from 50_startups.csv file and load the data into dataframe.
c. Check the statistical summary.
d. Check for corelation coefficient between dependent and independent variables.

"""
import pandas as pd

# a & b. Read the dataset into a DataFrame
startups = pd.read_csv("09_Numpy_And_Pandas/50_Startups.csv")  

# Show first 5 rows to confirm
print("First 5 rows of dataset:")
print(startups.head())

# c. Statistical summary
print("\nStatistical Summary:")
print(startups.describe())

# d. Correlation coefficient
print("\nCorrelation Matrix:")
print(startups.corr(numeric_only=True))
