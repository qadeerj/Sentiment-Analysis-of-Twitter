# 🐦 Twitter Sentiment Analysis with Flask & Logistic Regression

This project focuses on **Twitter Sentiment Analysis**, where the goal is to classify tweets into **positive** or **negative** sentiments. The project is built using a Flask web application, with a Logistic Regression model trained on a pre-processed dataset of 1.6 million tweets. 

---

## 🔍 Project Overview

This project aims to provide a real-time sentiment analysis tool for tweets, integrating machine learning with a responsive web interface. Users can analyze the sentiment of any given tweet and share insights through the blog feature.

---

## ✨ Features

- **Real-time Sentiment Analysis**: Classifies tweets as positive or negative based on user input.
- **Logistic Regression Model**: Trained from scratch using **Scikit-learn** for efficient sentiment classification.
- **User Authentication**: Users can **sign up**, **log in**, and manage their profiles.
- **Analysis History**: Users can view their **previous sentiment analyses**.
- **Blog Functionality**: Share insights via the integrated **blog**.

---

## 🖥️ Technologies Used

### Frontend:
- **HTML**, **CSS**, **Bootstrap** for a responsive and modern user interface.

### Backend:
- **Flask** (Python web framework) for handling user requests and serving the sentiment analysis.

### Database:
- **SQLite** (or **MySQL** in production) for storing user data, sentiment history, and blog posts.

### Machine Learning Model:
- **Logistic Regression** (Scikit-learn) for binary sentiment classification.
- **TF-IDF** vectorizer for feature extraction from text data.

### Deployment:
- **Flask** for local deployment.

---

## 📊 Dataset

The dataset contains **1.6 million pre-labeled tweets** (positive/negative sentiment). The data was cleaned and pre-processed, and then vectorized using **TF-IDF** to convert textual data into numerical features for model training.

---

## ⚙️ Model Training

- **Logistic Regression** was chosen due to its simplicity and effectiveness in binary classification.
- The tweets were transformed into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.
- **Cross-validation** was applied to ensure the model's accuracy and robustness during training and evaluation.

---

## 🚀 Installation & Setup

Follow the steps below to set up and run the project on your local machine:

### Prerequisites

- Python 3.x
- Flask
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn
- SQLite/MySQL

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/twitter-sentiment-analysis.git
    cd twitter-sentiment-analysis
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask Application**:
    ```bash
    python app.py
    ```

5. **Access the Application**:  
   Open your browser and go to:
