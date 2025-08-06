# Malicious URL Detection System

A machine learning-based web application that analyzes URLs to detect potential phishing and malicious websites. Built with Python, Flask, and scikit-learn.

## Features

- **Real-time URL Analysis**: Instantly analyze any URL for malicious indicators
- **Machine Learning Model**: Trained on thousands of legitimate and malicious URLs
- **Clean Web Interface**: Modern, responsive design with intuitive user experience
- **Comprehensive Feature Extraction**: Analyzes 25+ URL characteristics including:
  - Domain structure and TLD analysis
  - Character frequency and special character detection
  - Suspicious keyword identification
  - URL structure and path analysis
  - Brand name recognition for legitimate sites
    
<img src="https://github.com/user-attachments/assets/70d16bf7-121f-4bc4-bb6f-36a1ce83a834" alt="malicious URL" width="300" />
<img src="https://github.com/user-attachments/assets/224dd843-7541-4b5b-9b10-db69f3bdf518" alt="benign URL" width="300" />


## Technology Stack

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, Random Forest Classifier
- **Data Processing**: pandas, tldextract
- **Frontend**: HTML, CSS (minimal, clean design)
- **Model Persistence**: joblib

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. **Clone the repository**
   git clone https://github.com/zoeybkhal/malicious-url-identifer.git
   cd malicious_urls


2. **Install required dependencies**
   pip install flask pandas scikit-learn tldextract joblib
   

3. **Download the training dataset**
   - Place your `malicious_phish.csv` file in the project root
   - The dataset should contain columns: `url`, `type` (where type is 'benign' or 'defacement')

## �� Setup and Training

1. **Extract features from your dataset**
   python parsing.py

   This creates `features.csv` and `feature_names.pkl`

2. **Train the machine learning model**
   python machine_learning.py
 
   This creates `url_model.pkl` with the trained model

3. **Start the web application**
   python app.py
   

4. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Enter any URL to analyze for malicious indicators

## 📁 Project Structure

malicious_urls/
├── app.py                 # Flask web application
├── parsing.py             # Feature extraction for training data
├── machine_learning.py    # Model training script
├── feature_extraction.py  # Shared feature extraction logic
├── static/
│   └── design.css        # Styling for web interface
├── index.html            # Web interface template
├── malicious_phish.csv   # Training dataset
├── features.csv          # Extracted features (generated)
├── feature_names.pkl     # Feature names (generated)
├── url_model.pkl         # Trained model (generated)
└── README.md            # This file
```


You can customize any sections based on your specific needs or add additional information about your dataset, model performance, or deployment instructions.

## 🎯 How It Works

### Machine Learning Model
- **Algorithm**: Random Forest Classifier
- **Training Data**: Thousands of labeled URLs (benign vs malicious)
- **Accuracy**: Optimized for real-world phishing detection
- **Features**: 25 carefully selected URL characteristics

## Model Performance

The system is trained on a diverse dataset of:
- **Legitimate URLs**: Major websites, services, and platforms
- **Malicious URLs**: Known phishing sites and defacement pages


##  Customization

### Adding New Features
1. Modify `feature_extraction.py`
2. Update the `feature_names` list
3. Retrain the model with `python machine_learning.py`

### Adjusting Sensitivity
- Modify the `malicious_keywords` list in `feature_extraction.py`
- Update suspicious TLD detection in the feature extraction logic
- Retrain the model for updated behavior

## Disclaimer

This tool is designed for educational and research purposes. While it can help identify potentially malicious URLs, it should not be the sole method of security assessment. Always use multiple verification methods and exercise caution when dealing with suspicious links.

