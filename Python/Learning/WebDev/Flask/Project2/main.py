from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 100)
    return render_template("index.html", num=random_number)

@app.route("/guess/<name>")
def guess(name):
    # Gender prediction
    gender_url = "https://api.genderize.io"
    params = {"name": name}
    gender_response = requests.get(gender_url, params=params)
    gender_data = gender_response.json()
    gender = gender_data.get("gender", "unknown")

    # Age prediction
    age_url = "https://api.agify.io"
    age_response = requests.get(age_url, params=params)
    age_data = age_response.json()
    age = age_data.get("age", "unknown")

    return render_template("age.html", age=age, name=name, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)
