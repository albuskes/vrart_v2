from flask import render_template

from app import app


@app.route('/')
def home():
    return 'Home Page'


@app.route('/hello')
def hello_world():
    return render_template('index.html')

