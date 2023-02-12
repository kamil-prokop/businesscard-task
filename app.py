from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/hello/memy')
def memy():
    my_name = "John"
    return f'Hello, {my_name}!'


@app.route('/mypage/me')
def me():
    return render_template("bc_omnie.html")


@app.route('/mypage/contact', methods = ["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("businesscard_kontakt.html")
    elif request.method == "POST":
        print("To był komunikat POST")
        some_topic = request.form.get('some_topic')
        print(request.form)
        return redirect