import pandas as pd

# Load the DataFrame
df = pd.read_csv("C:/Users/Scherz/Desktop/School/Homework/Project 1/Project-1/Dataset/TEDSA_PUF_2020.csv")

# Explore the structure of the dataset
print("Dataset Overview:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst Few Rows of the Dataset:")
print(df.head())

# Identify unique values in relevant columns
    # Make column cointaining 'Primary Substance Use' 
    
    # Calculate drug preference


print(df['Primary Substance Use'].unique())

# # Summary statistics for numeric columns
# print("\nSummary Statistics:")
# print(df.describe())

# # Count the number of missing values in each column
# print("\nMissing Values:")
# print(df.isnull().sum())
