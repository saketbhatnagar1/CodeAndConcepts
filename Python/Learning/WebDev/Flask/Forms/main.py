import requests
from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/login',methods=["POST"])
def get_data():
    username = request.form['name']
    email = request.form['email']
    return f"{username} {email}"
if __name__ == "__main__":
    app.run(debug=True)