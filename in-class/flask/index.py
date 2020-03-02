from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World from Flask'

@app.route('/')
def root():
    return 'Hello You Are in the Root'