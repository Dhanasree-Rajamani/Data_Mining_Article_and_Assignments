#import flask
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session, g

#start flask app
app = Flask(__name__)
app.secret_key = 'secret'

#return index.html
@app.route('/')
def home():
    return render_template('co_pilot.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')

#listen on port 8080
app.run(debug=True, port=8080)
