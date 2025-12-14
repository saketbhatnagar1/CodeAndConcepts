#library vs framework =>

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HelloWorld'


@app.route('/username/<name>') #Variable Names
def greet(name):
    return f'Hello {name}'













if __name__ == "__main__":
    app.run(debug=True)