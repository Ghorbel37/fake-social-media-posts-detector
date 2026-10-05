# Fake Social Media Posts Detector

A machine learning-powered web application that detects fake news and misinformation in social media posts using Natural Language Processing (NLP) and Random Forest classification.

## 🎯 Project Overview

This project addresses the critical problem of misinformation on social media by building an intelligent classifier that can distinguish between real and fake news posts. The system combines web scraping, data augmentation techniques, machine learning, and a user-friendly Flask interface to provide real-time fake news detection.

## ✨ Features

- **Automated Data Collection**: Web scraper for PolitiFact's fact-checked social media posts
- **Data Augmentation**: Back-translation technique to balance the dataset
- **Machine Learning Classification**: Random Forest model with TF-IDF vectorization
- **Web Interface**: User-friendly Flask application for real-time predictions
- **High Performance**: Trained on 1,784+ fact-checked posts
- **Comprehensive Pipeline**: End-to-end workflow from data collection to deployment

## 📊 Dataset

The dataset consists of:
- **1,500 posts** scraped from PolitiFact (fact-checked social media posts)
- **284 real news articles** from Kaggle dataset
- **Data augmentation** via back-translation to balance classes
- **Final dataset**: 1,784+ labeled social media posts

### Data Sources
1. [PolitiFact](https://www.politifact.com/factchecks/list/) - Fact-checked social media posts
2. [Kaggle Fake News Dataset](https://www.kaggle.com/datasets/sumanthvrao/fakenewsdataset) - Additional real news articles

### Data Distribution
- **Fake News (Class 1)**: ~1,490 posts
- **Real News (Class 0)**: ~294 posts (after augmentation)

## 🛠️ Tech Stack

### Machine Learning & Data Processing
- **Python 3.x**
- **scikit-learn** - Machine Learning algorithms
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **NLTK** - Natural Language Processing
- **joblib** - Model serialization

### Web Scraping
- **BeautifulSoup4** - HTML parsing
- **requests** - HTTP library

### Data Augmentation
- **googletrans** - Translation API for back-translation

### Web Application
- **Flask** - Web framework
- **HTML/CSS** - Frontend interface

## 🚀 Installation

### Prerequisites
```bash
Python 3.7+
pip (Python package manager)
```

### Clone the Repository
```bash
git clone https://github.com/Ghorbel37/fake-social-media-posts-detector.git
cd fake-social-media-posts-detector
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Download NLTK Data (if required)
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

## 💻 Usage

### 1. Data Collection (Optional - Pre-scraped data available)
Run the Jupyter notebook to scrape fresh data:
```bash
jupyter notebook Fake_Social_Media_Posts_Detector.ipynb
```

### 2. Run the Flask Application
```bash
cd "Flask Interface"
python app.py
```

### 3. Access the Web Interface
Open your browser and navigate to:
```
http://localhost:5000
```

### 4. Make Predictions
1. Enter a social media post or headline in the text box
2. Click "Predict"
3. View the classification result (Real or Fake)

## 📁 Project Structure

```
fake-social-media-posts-detector/
│
├── Fake_Social_Media_Posts_Detector.ipynb    # Main notebook with full pipeline
├── Flask Interface/
│   ├── app.py                                # Flask application
│   ├── random_forest_model.pkl               # Trained ML model
│   ├── vectorizer.pkl                        # TF-IDF vectorizer
│   └── templates/
│       └── index.html                        # Web interface
└── README.md                                 # This file
```

## 🧠 Model Architecture

### Text Preprocessing
1. TF-IDF Vectorization
2. Stopword removal
3. Feature extraction from headlines

### Classification Model
- **Algorithm**: Random Forest Classifier
- **Features**: TF-IDF vectors from post headlines
- **Output**: Binary classification (0: Real, 1: Fake)

### Training Process
1. Data cleaning and preprocessing
2. TF-IDF vectorization
3. Train-test split
4. Model training with Random Forest
5. Model evaluation and validation
6. Model serialization for deployment

## 📈 Model Performance

The model achieves strong performance metrics:
- Trained on 1,784+ fact-checked posts
- Uses ensemble learning (Random Forest)
- Real-time inference capability

## 🔍 How It Works

### Data Collection Pipeline
1. **Web Scraping**: Automated scraper collects data from PolitiFact
   - Post headline
   - Source platform
   - Fact-check rating
   - Fact checker name
   - Dates
   - Post type
   - URL

2. **Data Cleaning**:
   - Remove unnecessary text
   - Convert dates to datetime format
   - Map ratings to binary labels
   - Handle missing values

3. **Data Augmentation**:
   - Back-translation (English → French → English)
   - Increases dataset diversity
   - Balances class distribution

### Prediction Pipeline
1. User inputs a social media post
2. Text is vectorized using TF-IDF
3. Random Forest model predicts classification
4. Result displayed: "Real" or "Fake"

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

**Note**: This project is for educational purposes only.
