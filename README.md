Twitter Sentiment Analysis with Flask & Logistic Regression
Project Overview
This project focuses on Twitter sentiment analysis, where the goal is to classify tweets into positive and negative sentiments. The project is built using a Flask web application, with a Logistic Regression model trained on a pre-generated dataset of 1.6 million tweets. The web app includes user authentication, sentiment analysis, and a blog feature to share insights.

Features
Real-time Sentiment Analysis: Classify tweets as positive or negative based on user input.
Logistic Regression Model: Trained from scratch using Scikit-learn.
User Authentication: Users can sign up, log in, and manage their profiles.
Analysis History: Users can view their previous sentiment analyses.
Blog Functionality: Users can share analysis insights via the integrated blog.
Technologies Used
Frontend:
HTML, CSS, Bootstrap
Backend:
Flask (Python Framework)
Database:
SQLite (or MySQL for production)
Machine Learning Model:
Logistic Regression (Scikit-learn)
TF-IDF vectorizer for feature extraction
Deployment:
Flask (Local deployment)
Dataset
The dataset used contains 1.6 million pre-labeled tweets (positive/negative sentiment). It was cleaned, pre-processed, and vectorized using TF-IDF to convert textual data into numerical format for model training.

Model Training
Logistic Regression was chosen due to its simplicity and effectiveness for binary classification problems.
TF-IDF (Term Frequency-Inverse Document Frequency) was used to transform tweets into numerical features.
The model was trained and evaluated using cross-validation to ensure accuracy and robustness.
Installation & Setup
Prerequisites
Python 3.x
Flask
Scikit-learn
Pandas
Matplotlib
Seaborn
SQLite/MySQL
Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Run the Application
bash
Copy code
python app.py
Access the Application
Once the application is running, access it in your browser by navigating to:

arduino
Copy code
http://127.0.0.1:5000/
Usage
Sign Up / Login: Create an account to access the application.
Analyze Sentiment: Enter a tweet or text to analyze its sentiment (positive/negative).
View History: View previously analyzed sentiments.
Blog: Share analysis insights via the blog feature.
Screenshots
Home Page

Sentiment Analysis Result

Project Structure
php
Copy code
twitter-sentiment-analysis/
│
├── app.py                     # Flask application
├── templates/
│   ├── index.html              # Homepage template
│   ├── login.html              # Login page template
│   ├── signup.html             # Signup page template
│   └── result.html             # Result page for sentiment analysis
├── static/
│   ├── style.css               # CSS styles
│   └── screenshots/            # Screenshots of the app
├── models/
│   └── logistic_model.pkl      # Pre-trained Logistic Regression model
├── requirements.txt            # List of dependencies
└── README.md                   # Project documentation
Model Performance
Accuracy: 78% (on test data)
Precision: 83%
Recall: 86%
F1-Score: 84%
Future Improvements
Implement additional ML models (e.g., SVM, Random Forest) for comparison.
Add real-time Twitter API integration for live sentiment analysis.
Optimize the UI/UX for better user interaction.
License
This project is licensed under the MIT License. Feel free to fork and contribute!

