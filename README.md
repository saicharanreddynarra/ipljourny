# ipljourny
# Overview:

This is a Flask-based web application that predicts the final score of an IPL team during a match. The model used in this application is a trained RandomForest regression model that has been serialized using pickle.

# Features:

.Web interface for user input

.One-Hot Encoding for team selection

.Uses a trained RandomForest model for prediction

.Predicts final score based on match details

# Installation

# Prerequisites

Ensure you have the following installed:

.Python 3.x

.Flask

.NumPy

.Scikit-learn

.Pickle
# Setup
## 1.Clone this repository:
git clone https://github.com/saicharanreddynarra/ipljourny.git

cd ipljourny

## 2.Install dependencies:
pip install -r requirements.txt

# Project Structure:
ipljourny/
│-- app.py  # Main Flask application

│-- ipl_model.pkl  # Trained RandomForest model

│-- templates/

│   └── index.html  # Webpage for user input

│-- static/  # CSS and other static assets (if any)

│-- requirements.txt  # List of dependencies

│-- README.md  # Project documentation

# Model Details:

.The model is trained using IPL match data.

.It considers factors like batting team, bowling team, current runs, wickets, overs, runs in last 5 overs, and wickets in last 5 overs.

.Predicts the final score using RandomForest regression.
