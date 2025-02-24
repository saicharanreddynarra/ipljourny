from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

# Initialize the Flask app
app = Flask(__name__)

# Load the trained RandomForest model from the pickle file
with open('ipl_model.pkl', 'rb') as f:
    model = pickle.load(f)

# List of teams for One-Hot Encoding
teams = [
    'Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 
    'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
]

def score_predict(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5, model=model):
    prediction_array = []
    
    # One-hot encode the batting team
    for team in teams:
        if team == batting_team:
            prediction_array.append(1)
        else:
            prediction_array.append(0)

    # One-hot encode the bowling team
    for team in teams:
        if team == bowling_team:
            prediction_array.append(1)
        else:
            prediction_array.append(0)
    
    # Add the match details
    prediction_array += [runs, wickets, overs, runs_last_5, wickets_last_5]
    
    # Convert to numpy array and predict the score
    prediction_array = np.array([prediction_array])
    predicted_score = model.predict(prediction_array)
    
    return int(round(predicted_score[0]))

# Home route that renders the input form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission and make prediction
@app.route('/predict', methods=['POST'])
def predict():
    batting_team = request.form['batting_team']
    bowling_team = request.form['bowling_team']
    runs = int(request.form['runs'])
    wickets = int(request.form['wickets'])
    overs = float(request.form['overs'])
    runs_last_5 = int(request.form['runs_last_5'])
    wickets_last_5 = int(request.form['wickets_last_5'])
    
    # Predict the score using the model
    predicted_score = score_predict(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5)

    return render_template('index.html', prediction_text=f'Predicted Score: {predicted_score}')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
