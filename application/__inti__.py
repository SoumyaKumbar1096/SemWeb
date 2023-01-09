from flask import Flask, render_template

app = Flask(__name__)

from application import routes

@app.route('/')
def hello():
    return render_template('index.html')