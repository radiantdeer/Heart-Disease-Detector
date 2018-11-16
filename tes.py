from flask import Flask, render_template
app = Flask(__name__)

@app.route("/home", methods=['GET','POST'])
def home():
    return render_template('home.html', title='home') 

@app.route("/about")
def about():
    return render_template('about.html', title='about')