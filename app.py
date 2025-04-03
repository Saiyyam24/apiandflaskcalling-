from flask import Flask,render_template,request,redirect
from db import database
from api import ner_text

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
        return render_template('register.html',message = "account not able to create")
@app.route('/perform_login', methods=['POST'])
def perform_login():
    email = request.form.get('users_email')
    password = request.form.get('users_password')
    response = dbo.search(email,password)
    if response:
        return redirect('/profile')
    else:
        return render_template('index.html', message="incorrect email password")
    
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner', methods = ['POST'])
def perform_ner():
    text = request.form.get('ner_text')
    response = apio.ner_text(text)
    print(response)

    result = ""
    for i in response['entities']:
        result += i['text'] + " " + i['type']+"\n"
    
    return render_template('ner.html',result=result)

@app.route('/sentiment_analysis')
def sentiment_analysis():
    return "sentiment analysis"

@app.route('/abuse_detection')
def abuse_detection():
    return "abuse_detection"

if __name__ == "__main__":
    app.run(debug=True)