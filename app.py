from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/gen', methods=['GET', 'POST'])
def gen():
    
    return render_template('gen.html')

if __name__ == "__main__":
    app.run(debug=True)
