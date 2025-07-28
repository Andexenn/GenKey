from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "HUNG"

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
            Pass="123"
            return render_template('gen.html', Pass="123")
            # flash("Your name has been used", "info")
    return render_template('gen.html')

if __name__ == "__main__":
    app.run(debug=True)
