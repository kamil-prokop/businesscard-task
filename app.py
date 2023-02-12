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
        return render_template("bc_kontakt.html")
    elif request.method == "POST":
        print('text_to_send')
        return redirect('/mypage/contact')