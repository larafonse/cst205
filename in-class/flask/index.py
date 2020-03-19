from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app) 

# Dictionary that holds information that will be passed into home directoryu
dict= {
    'one':'Lab 11: Flask',
    'two':'HW3: Image Search',
    'three':'Blues Music Paper'}

# route that takes in dictioary variable
@app.route('/')
def home():
    return render_template('template1.html', var = dict)