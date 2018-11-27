from flask import Flask, render_template, request
import json
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import RobustScaler
from sklearn.externals import joblib
from traceback import print_exc
app = Flask(__name__)

Flask.debug = True

loaded_model = joblib.load("KNN.dat")
data_transformer = joblib.load("data_transformer.dat")

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html', title='home') 

@app.route("/process", methods=['POST'])
def process():
    global data_transformer, loaded_model
    status = 0
    response_text = ""
    try:
        # Retrieving request data
        gender = np.int64(request.form["gender"]);
        age = np.int64(request.form["age"]);
        chest_pain = np.int64(request.form["chest_pain"]);
        blood_pres = np.int64(request.form["blood_pres"]);
        serum = np.int64(request.form["serum"]);
        fasting_blood = np.int64(request.form["fasting_blood_sugar"]);
        resting_ecg = np.int64(request.form["resting_ecg"]);
        max_heart_rate = np.int64(request.form["max_heart_rate"]);
        exc_induced = np.int64(request.form["exc_induced"]);
        st_depression = np.float64(request.form["st_depression"]);
        peak_exercise = np.int64(request.form["peak_exercise"]);
        major_fluorosopy = np.int64(request.form["major_fluorosopy"]);
        thal = np.int64(request.form["thal"]);

        # Constructing into a new instance
        new_instance = [[age,gender,chest_pain,blood_pres,serum,fasting_blood,resting_ecg,max_heart_rate, exc_induced, st_depression, peak_exercise, major_fluorosopy, thal]];

        # Transform new instance so that it's compatible with the model
        new_instance = data_transformer.transform(new_instance);
        print(new_instance);

        # Predict instance
        prediction = loaded_model.predict(new_instance);
        print(prediction);
        response_text = str(prediction[0]);

    except(ValueError):
        print_exc();
        response_text = "Parsing error!";
        status = -1;
    except:
        print_exc();
        response_text = "Unhandled exception occured!";
        status = -999;
    
    return json.JSONEncoder().encode({"status" : status, "response_text" : response_text});