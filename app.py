from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import math
import random


app = Flask(__name__)
app.config["SECRET_KEY"] = "HUNG"

def generatePassword(length = 8):
    lowerChars = "abcdefghijklmnopqrstuvwxyz";
    numberChars = "0123456789";
    specialChars = "!@#$%^&*()_+~`|}{[]:;?><,./-=";
    allChars = lowerChars + numberChars + specialChars;
    
    password = "";

    password += lowerChars[math.floor(random.random() * len(lowerChars))];
    password += numberChars[math.floor(random.random() * len(numberChars))];
    password += specialChars[math.floor(random.random() * len(specialChars))];

    for i in range(3, 8):
        password += allChars[math.floor(random.random() * len(allChars))];
    

    return password

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/gen', methods=['GET', 'POST'])
def gen():
    # TODO: consider the methods get or post, create the pass
    if request.method == "POST":
        user_name = request.form["username"]
        if not user_name:
            flash("You've not entered user name")
            return redirect(url_for('gen'))
        else:
            # try:
            #     data = request.get_json()
            #     Pass = data.get("password")
            # except:
            #     raise ValueError("Khong nhan duoc gia tri")
            Pass = generatePassword(8)
            
            return render_template('gen.html', Pass=Pass)
            # flash("Your name has been used", "info")
    return render_template('gen.html')

if __name__ == "__main__":
    app.run(debug=True)
