# *******************************************************
# Name: Hazel Zhu
# UNI: hz2653
# This program create a website for the final project.
# *******************************************************

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/assignment")
def assignment():
    return render_template("assignment.html")
@app.route("/class")
def classpage():
    return render_template("class.html")

#start the server
if __name__ == "__main__":
    app.run()
