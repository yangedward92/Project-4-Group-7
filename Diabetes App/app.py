from flask import Flask, render_template, redirect, request, jsonify
from model_helper import ModelHelper

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()

# Route to render index.html template
@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

@app.route("/diabetes_predML")
def diabetes_pred_ml():
    """Render the Diabetes Prediction page."""
    return render_template("diabetes_predML.html")

@app.route("/works_cited")
def works_cited():
    """Render the works cited page."""
    return render_template("works_cited.html")

@app.route("/about_us")
def about_us():
    """Render the about us page."""
    return render_template("about_us.html")

@app.route("/tableau_1")
def tableau():
    """Render the Tableau 1 visualization page."""
    return render_template("tableau_1.html")

@app.route("/tableau_2")
def tableau2():
    """Render the Tableau 2 visualization page."""
    return render_template("tableau_2.html")

@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)
    
            
    Pregnancies = int(content.get("Pregnancies", 0))
    Glucose = int(content.get("Glucose", 0))
    BloodPressure = int(content.get("BloodPressure", 0))
    SkinThickness = int(content.get("SkinThickness", 0))
    Insulin = int(content.get("Insulin", 0))
    BMI = float(content.get("BMI", 0))
    DiabetesPedigreeFunction = float(content.get("DiabetesPedigreeFunction", 0))
    Age = int(content.get("Age", 0))

    # Make predictions using the model helper
    preds = modelHelper.make_predictions(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    return jsonify({"ok": True, "prediction": str(preds)})

       
#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force the latest IE rendering engine or Chrome Frame,
    and also to disable caching during development.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)



