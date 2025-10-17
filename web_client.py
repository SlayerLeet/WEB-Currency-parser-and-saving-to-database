from flask import Flask, url_for, render_template
app = Flask(__name__)
from parser_moex import moex
from parser_binance import cripta
from datetime import datetime


@app.route("/")
def index():
    values = {"fiat" : moex(), "cripta" : cripta()}
    return render_template("index.html", values = values )

if __name__=="__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
