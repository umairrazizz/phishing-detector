# Phishing Website Detector

## Overview
Phishing attacks are a significant cybersecurity threat. This project aims to detect phishing websites using machine learning. It analyzes website features such as URL length, presence of special characters, and other key indicators to classify sites as **phishing** or **legitimate**.

## Features
- **AI-Powered Detection**: Uses a trained machine learning model for classification.
- **User-Friendly Web Interface**: Enter website details and get real-time predictions.
- **Deployment**: Hosted on [Render](https://phishing-detector-08ut.onrender.com) for public access.

## Installation
Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/phishing-detector.git
cd phishing-detector
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask App
```bash
python app.py
```

### 4. Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

## Usage
1. **Enter Website Features**: Input details such as URL length and special characters.
2. **Get Prediction**: Click the **Predict** button to classify the website as phishing or legitimate.

## File Structure
```
phishing-detector/
│
├── app.py                  # Flask application
├── requirements.txt        # Project dependencies
├── Procfile                # Deployment configuration (optional)
├── phishing_model.pkl      # Trained machine learning model
├── X.csv                   # Preprocessed feature dataset
├── y.csv                   # Preprocessed target dataset
├── load_data.py            # Script to load and clean data
├── preprocess_data.py      # Script to preprocess the data
├── train_model.py          # Script to train the model
└── templates/              # HTML templates for the web interface
    └── index.html
```

## Dependencies
The project requires the following Python libraries:
- **Flask** - Web framework
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning algorithms
- **Joblib** - Model serialization
- **Gunicorn** - WSGI server for deployment

All dependencies are listed in `requirements.txt`.

## Contributing
Contributions are welcome! To contribute:
1. **Fork** the repository.
2. **Create a new branch** for your feature or bug fix.
3. **Commit** your changes.
4. **Submit a pull request** for review.

## License
This project is open-source and available under the [MIT License](LICENSE).