#!flask/bin/python

import sys
import os

from flask import Flask, render_template, request, redirect, Response, url_for
import random, json
import getDataAndCoors


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/receiver', methods = ['POST'])
def receiver():
    
    tags = request.form['tags']
    print(tags)

    file = open("searchTerms.txt","w") 
 
    file.write(tags) 
         
    file.close() 

    # os.system("getDataAndCoors.py")
    # execfile('getDataAndCoors.py')
    exec(open(getDataAndCoors.py).read())

    return redirect(url_for('success',_external=True))

@app.route('/success')
def success():
    return render_template("success.html")

if __name__=='__main__':
    app.run()
