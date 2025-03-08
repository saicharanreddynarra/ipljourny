# ipljourny
# Overview:

    This is a Flask-based web application that predicts the final score of an IPL team during a match. The model used in this application is a trained RandomForest regression model that has been serialized using 
    pickle.

# Features:

    🏏 User-Friendly Web Interface – Provides an interactive webpage for user input.
    🔢 One-Hot Encoding – Used for team selection to enhance model accuracy.
    🤖 Machine Learning Model – Employs a RandomForest regression model trained on IPL match data.
    📊 Final Score Prediction – Predicts the total score based on real-time match conditions.

# Installation

# Prerequisites

  Ensure you have the following installed before running the application:

    Python 3.x
    Flask
    NumPy
    Scikit-learn
    Pickle
    
# Setup

## 1.Clone this repository:
    git clone https://github.com/saicharanreddynarra/ipljourny.git
    
    cd ipljourny

## 2.Install dependencies:
    pip install -r requirements.txt

# Project Structure:
    ipljourny/  
    │-- app.py               # Main Flask application  
    │-- ipl_model.pkl        # Trained RandomForest model  
    │-- templates/  
    │   └── index.html       # Webpage for user input  
    │-- static/              # CSS and other static assets (if any)  
    │-- requirements.txt     # List of dependencies  
    │-- README.md            # Project documentation  


# Model Details:

    The model is trained using historical IPL match data.
    It considers the following factors to predict the final score:
    Batting Team
    Bowling Team
    Current Runs
    Wickets Lost
    Overs Bowled
    Runs in Last 5 Overs
    Wickets in Last 5 Overs
    The RandomForest regression model is used for prediction, providing accurate estimates of the final score.

# License
    This project is licensed under the MIT License.



    

