from flask import Flask, render_template, request
import json
app = Flask(__name__)

Flask.debug = True

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html', title='home') 

@app.route("/process", methods=['POST'])
def process():
    status = 0
    response_text = ""
    try:
        # Retrieving request data
        gender = int(request.form["gender"]);
        age = int(request.form["age"]);
        chest_pain = int(request.form["chest_pain"]);
        blood_pres = int(request.form["blood_pres"]);
        serum = int(request.form["serum"]);
        fasting_blood = int(request.form["fasting_blood_sugar"]);
        resting_ecg = int(request.form["resting_ecg"]);
        max_heart_rate = int(request.form["max_heart_rate"]);
        st_depression = int(request.form["st_depression"]);
        peak_exercise = int(request.form["peak_exercise"]);
        major_fluorosopy = int(request.form["major_fluorosopy"]);
        thal = int(request.form["thal"]);

        response_text = "Gender : " + str(gender) + " | Age : " + str(age) + " | Chest Pain : " + str(chest_pain);
    except(ValueError):
        response_text = "Parsing error!";
        status = -1;
    except(KeyError):
        response_text = "Please fill in all the fields!";
        status = -2;
    except:
        response_text = "Unhandled exception occured!";
        status = -999;
    
    return json.JSONEncoder().encode({"status" : status, "response_text" : response_text});

@app.route("/about")
def about():
    return render_template('about.html', title='about')
