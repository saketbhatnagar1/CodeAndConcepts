from doctest import debug

import requests
from flask import Flask, render_template

app = Flask(__name__)
url = "https://api.npoint.io/f8e2643d4e8fdcbca99c"

@app.route('/')
def hello_world():
    return 'HelloWorld'


@app.route('/blogs') #Variable Names
def greet():
    response = requests.get(url)
    data = response.json()
    return render_template("index.html",posts = data)




if __name__ == "__main__":
    app.run(debug=True)