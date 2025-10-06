from flask import Flask, url_for, render_template
app = Flask(__name__)
from parser import norm

@app.route("/")
def index():
    values = norm()
    return render_template("index.html", values=values)

if __name__=="__main__":
    app.run(debug=True)
