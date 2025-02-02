from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('phishing_model.pkl')
# Load feature names from training
X_train = pd.read_csv('X.csv')
feature_names = X_train.columns.tolist()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read form data and convert to a dictionary
        input_data = {col: [float(x)] for col, x in zip(feature_names, request.form.values())}
        df_input = pd.DataFrame(input_data)

        # Apply the same transformations (get_dummies, column alignment)
        df_input = pd.get_dummies(df_input)
        df_input = df_input.reindex(columns=feature_names, fill_value=0)  # Ensure all columns match training

        print(f"Feature Shape Before Prediction: {df_input.shape}")  # Debugging output

        # Predict using the trained model
        prediction = model.predict(df_input)
        result = "Phishing" if prediction[0] == 1 else "Legitimate"

        return render_template('index.html', prediction_text=f'This website is {result}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)