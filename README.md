# phishing-detector
# Phishing Website Detector

## Project Overview
This project is an AI-powered phishing website detection system. It uses machine learning to analyze website features (e.g., URL length, special characters) and classify them as either **phishing** or **legitimate**. The system is built using Python, Flask, and Scikit-learn, and it is deployed as a web application.

## Features
- **Machine Learning Model**: Trained on a dataset of phishing and legitimate websites.
- **Web Interface**: Users can input website features and get real-time predictions.
- **Deployment**: The app is deployed on [Render](https://phishing-detector-08ut.onrender.com) and accessible via a public URL.

## Installation
To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/phishing-detector.git
   cd phishing-detector
2. **Install Dependencies**:
  ```bash
pip install -r requirements.txt
3. **Run the Flask App**
   ```bash
python app.py
4. **Access the App:**
  Open your browser and go to http://127.0.0.1:5000/
5. **Usage**
Input Features:
   Enter the website features (e.g., URL length, special characters) in the web interface.
**Get Predictions**:
   Click the Predict button to see if the website is classified as phishing or legitimate.
File Structure
phishing-detector/
│
├── app.py                  # Flask application
├── requirements.txt        # Dependencies
├── Procfile                # Render configuration (optional)
├── phishing_model.pkl      # Trained machine learning model
├── X.csv                   # Preprocessed features
├── y.csv                   # Preprocessed target
├── load_data.py            # Script to load and clean the dataset
├── preprocess_data.py      # Script to preprocess the data
├── train_model.py          # Script to train the machine learning model
└── templates/              # Folder for HTML templates
    └── index.html          # Web interface

**Dependencies**
The project requires the following Python libraries:
Flask
Pandas
Scikit-learn
Joblib
Gunicorn
All dependencies are listed in requirements.txt.
**Contributing**
Contributions are welcome! If you'd like to contribute, please follow these steps:
1)Fork the repository.
2)Create a new branch for your feature or bugfix.
3)Commit your changes.
4)Submit a pull request.