from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app) 

dict= {
    'one':1,
    'two':2,
    'three':3}
@app.route('/hello')
def hello():
    return 'Hello World from Flask'

# @app.route('/')
# def root():
#     return 'Hello You Are in the Root'

@app.route('/')
def home():
    return render_template('template1.html', var = dict)