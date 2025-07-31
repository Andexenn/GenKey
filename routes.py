from flask import Flask, render_template, flash, request, redirect, url_for
from models import User
import math
import random

def register_routes(app, db):

    def generatePassword(length = 8):
        lowerChars = "abcdefghijklmnopqrstuvwxyz"
        numberChars = "0123456789"
        specialChars = "!@#$%^&*()_+~`|}{[]:;?><,./-="
        allChars = lowerChars + numberChars + specialChars
        
        password = ""

        password += lowerChars[math.floor(random.random() * len(lowerChars))]
        password += numberChars[math.floor(random.random() * len(numberChars))]
        password += specialChars[math.floor(random.random() * len(specialChars))]

        for i in range(3, 8):
            password += allChars[math.floor(random.random() * len(allChars))]
        

        return password

    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/gen', methods=['GET', 'POST'])
    def gen():
        if request.method == "POST":
            username = request.form.get("username")
            if not username:
                flash("You've not entered user name")
                return redirect(url_for('gen'))
            else:
                Pass = None
                if User.query.filter(User.username == username).first():
                    flash("Your name has been used")
                else:
                    Pass = username + generatePassword(8)
                    user = User(username=username, password=Pass)
                    db.session.add(user)
                    db.session.commit()

                return render_template('gen.html', Pass=Pass)
        return render_template('gen.html')
    
    @app.route('/find', methods=['GET', 'POST'])
    def find():
        if request.method == 'POST':
            username = request.form.get("username")
            user = User.query.filter(User.username == username).first()
            if user:
                return render_template("find.html", password=user.password)
            else:
                flash("Your name was not found!")
                return render_template("find.html")
            
        return render_template("find.html")
