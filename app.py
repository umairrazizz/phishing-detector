from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('phishing_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the form
    features = [float(x) for x in request.form.values()]
    # Predict
    prediction = model.predict([features])
    result = "Phishing" if prediction == 1 else "Legitimate"
    return render_template('index.html', prediction_text=f'This website is {result}')

if __name__ == '__main__':
    app.run(debug=True)