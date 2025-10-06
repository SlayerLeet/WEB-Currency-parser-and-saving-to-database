from flask import Flask, url_for, render_template
app = Flask(__name__)
from parser_moex import norm
import requests

@app.route("/")
def index():
    values = requests.get("http://127.0.0.1:5000/api/main").json()
    return render_template("index.html", values=values)

if __name__=="__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
