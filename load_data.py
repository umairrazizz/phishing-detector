import pandas as pd
from scipy.io.arff import loadarff

# Load the .arff file
data = loadarff('TrainingDataset.arff')
df = pd.DataFrame(data[0])

# Convert bytes to strings
for col in df.columns:
    if df[col].dtype == object:
        df[col] = df[col].str.decode('utf-8')

# Save the cleaned data to a CSV file for easier use
df.to_csv('phishing_cleaned.csv', index=False)

# Inspect the data
print(df.head())  # View the first few rows
print(df.info())  # Check column names and data types
print(df['Result'].value_counts())  # Check distribution of target variable