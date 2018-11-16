from flask import Flask, render_template, request
from sklearn.naive_bayes import GaussianNB
import json
from sklearn.externals import joblib
from traceback import print_exc
app = Flask(__name__)

Flask.debug = True

loaded_model = joblib.load("NB.dat")

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
        exc_induced = int(request.form["exc_induced"]);
        st_depression = int(request.form["st_depression"]);
        peak_exercise = int(request.form["peak_exercise"]);
        major_fluorosopy = int(request.form["major_fluorosopy"]);
        thal = int(request.form["thal"]);

        new_instance = [gender,age,chest_pain,blood_pres,serum,fasting_blood,resting_ecg,max_heart_rate, exc_induced, st_depression, peak_exercise, major_fluorosopy, thal];

        prediction = loaded_model.predict([new_instance]);
        print(prediction)
        if (prediction[0] == 0):
            response_text = "You don't have heart disease!";
        else:
            response_text = "You have heart disease!";

    except(ValueError):
        print_exc();
        response_text = "Parsing error!";
        status = -1;
    except(KeyError):
        print_exc();
        response_text = "Please fill in all the fields!";
        status = -2;
    except:
        print_exc();
        response_text = "Unhandled exception occured!";
        status = -999;
    
    return json.JSONEncoder().encode({"status" : status, "response_text" : response_text});

@app.route("/about")
def about():
    return render_template('about.html', title='about')
