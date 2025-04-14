from flask import Flask,render_template,request,redirect
from db import database
from api import ner_text
from sentimentanalys import analyze_sentiment


dbo = database()
apio = ner_text()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name = request.form.get('users_name')
    email = request.form.get('users_email')
    password = request.form.get('users_password')
    response = dbo.insert(name,email,password)
    if response==1:
        return render_template('index.html',message = "Registratiin successful you can login")
    else:
        return render_template('register.htm