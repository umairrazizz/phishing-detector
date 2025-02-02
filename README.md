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
  