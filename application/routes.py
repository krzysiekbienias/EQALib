from application import app,db
from flask import render_template,redirect,json,Response

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/elements")
def elements():
    return render_template("elements.html")










    