from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/mypage/me')
def mypage(me):
    return render_template("businesscard_omnie.html")


@app.route('/mypage/contact', methods = ["GET", "POST"])
def mypage(contact):
    if request.method == "GET":
        return render_template("businesscard_kontakt.html")
    elif request.method == "POST":
        print("To był komunikat POST")
        some_topic = request.form.get('some_topic')
        print(request.form)
        return redirect