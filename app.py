from flask import Flask
from flask import render_template
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello, Flask!'

@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_there.html",
        title='Hello, Flask',
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
