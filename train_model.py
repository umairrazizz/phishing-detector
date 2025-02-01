import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Step 1: Load the preprocessed data
X = pd.read_csv('X.csv')
y = pd.read_csv('y.csv')

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train a Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train.values.ravel())  # .values.ravel() to flatten y_train

# Step 4: Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Step 5: Save the trained model
joblib.dump(model, 'phishing_model.pkl')
print("Model saved as phishing_model.pkl")