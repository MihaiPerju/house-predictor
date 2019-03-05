from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("OK")
    return render_template("index.html")