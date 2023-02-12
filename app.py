from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/mypage/me')
def mypage(me):
    return render_template("businesscard_omnie.html")


@app.route('/mypage/contact')
def mypage(contact):
    return render_template("businesscard_kontakt.html")

