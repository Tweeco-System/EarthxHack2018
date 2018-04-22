#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response, url_for
import random, json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/receiver', methods = ['POST'])
def receiver():

    user = request.args.get('zip')

    # return result
    return redirect(url_for('success',name = user))

@app.route('/success')
def success():
    return render_template("success.html")

if __name__=='__main__':
    app.run(host='https://tweeco-system.herokuapp.com/')
