from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the model and the vectorizer
model = joblib.load('random_forest_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        # Get the text input from the user
        headline = request.form["headline"]
        
        # Transform the text input using the vectorizer
        transformed_text = vectorizer.transform([headline]).toarray()
        
        # Make a prediction using the model
        prediction = model.predict(transformed_text)[0]
        
        # Convert the numeric prediction to a more understandable label
        if prediction == 0:
            prediction = "Real"
        else:
            prediction = "Fake"
    
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=False)
