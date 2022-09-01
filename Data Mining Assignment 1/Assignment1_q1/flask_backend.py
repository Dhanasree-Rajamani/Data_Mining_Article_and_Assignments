#import flask
from flask import Flask, render_template, request, jsonify

#start flask app
app = Flask(__name__)
#app secret key
app.secret_key = 'secret'

#return homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

#return menu page
@app.route('/menu')
def menu():
    return render_template('menu.html')

#return about page
@app.route('/about')
def about():
    return render_template('about.html')

#listen on port 8080
app.run(debug=True, port=8080)