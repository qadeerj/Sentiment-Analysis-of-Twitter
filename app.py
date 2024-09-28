from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
import os
import joblib
import sqlite3
from datetime import datetime
import plotly.graph_objects as go

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/profile_pics'

# Load the model and vectorizer for sentiment analysis
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Create the SQLite database for user info and analysis history
def init_db():
    with sqlite3.connect('users.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                profile_pic TEXT
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS analysis_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                tweet TEXT,
                sentiment TEXT,
                date TEXT
            )
        ''')
init_db()

# Routes for signup, login, and dashboard
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        profile_pic = request.files['profile_pic']

        # Save the profile picture
        if profile_pic:
            filename = secure_filename(profile_pic.filename)
            profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Save user info in the database
        with sqlite3.connect('users.db') as conn:
            conn.execute('INSERT INTO users (username, password, profile_pic) VALUES (?, ?, ?)',
                         (username, password, filename))
        flash('Signup successful! Please login.')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect('users.db') as conn:
            user = conn.execute('SELECT * FROM users WHERE username=? AND password=?',
                                (username, password)).fetchone()

        if user:
            session['username'] = username
            session['profile_pic'] = user[3]
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Retrieve previous analysis history
    with sqlite3.connect('users.db') as conn:
        history = conn.execute('SELECT tweet, sentiment, date FROM analysis_history WHERE user_id=?',
                               (session['username'],)).fetchall()

    return render_template('index.html', profile_pic=session.get('profile_pic'), history=history)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        tweet = request.form['tweet']
        tweet_cleaned = vectorizer.transform([tweet])
        prediction = model.predict(tweet_cleaned)

        sentiment = 'Positive' if prediction == 1 else 'Negative'
        sentiment_score = prediction[0]  # Assume you have a numeric score, adjust as necessary
        bar_color = 'green' if sentiment == 'Positive' else 'red'
        sentiment_text = sentiment

        # Save analysis history
        with sqlite3.connect('users.db') as conn:
            conn.execute('INSERT INTO analysis_history (user_id, tweet, sentiment, date) VALUES (?, ?, ?, ?)',
                         (session['username'], tweet, sentiment, str(datetime.now())))

        return render_template('index.html', prediction_text=f'Tweet Sentiment: {sentiment}', 
                               sentiment_score=sentiment_score,
                               bar_color=bar_color,
                               sentiment_text=sentiment_text,
                               profile_pic=session.get('profile_pic'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('profile_pic', None)
    return redirect(url_for('login'))

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Function to generate sentiment bar chart
def generate_bar_chart(sentiment_score):
    # Choose color based on sentiment
    color = 'green' if sentiment_score > 0 else 'red'
    
    # Create the bar chart using Plotly
    fig = go.Figure([go.Bar(
        x=['Sentiment'],
        y=[sentiment_score],
        marker_color=color,
        text=f'{sentiment_score}',
        textposition='auto'
    )])
    
    fig.update_layout(
        title_text="Sentiment Score",
        yaxis_range=[-1, 1],  # Range between -1 (negative) and 1 (positive)
        height=400
    )
    
    # Render the chart to HTML
    graph_html = fig.to_html(full_html=False)
    return graph_html

if __name__ == "__main__":
    app.run(debug=True)
