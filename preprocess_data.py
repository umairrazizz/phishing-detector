import pandas as pd

# Load the cleaned data
df = pd.read_csv('phishing_cleaned.csv')

# Convert the target column to binary
df['Result'] = df['Result'].apply(lambda x: 1 if x == '1' else 0)

# Separate features and target
X = df.drop('Result', axis=1)  # Features
y = df['Result']  # Target

# Convert categorical features to numerical
X = pd.get_dummies(X, drop_first=True)

# Save the preprocessed data
X.to_csv('X.csv', index=False)
y.to_csv('y.csv', index=False)

print("Preprocessing complete! Files saved as X.csv and y.csv.")