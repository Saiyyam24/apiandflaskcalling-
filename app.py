from flask import Flask,render_template,request,redirect
from db import database
from api import ner_text
from sentimentanalys import sentimentanalys
from abusedetection import abusedetect

dbo = database()
apio = ner_text()
senti = sentimentanalys()
abuse = abusedetect()
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
    return render_template('sentiment.html')

@app.route('/perform_sentiment_analysis', methods = ['POST'])
def perform_sentiment_analysis():
    text = request.form.get('Sentiment_text')
    response = senti.analyze_sentiment(text)
    print(response)
    if response['Sentiment Score'] > 0:
        return render_template('sentiment.html',result="positive")
    elif response['Sentiment Score']<0:
        return render_template('sentiment.html',result="negative")
    else:
        return render_template('sentiment.html',result="neutral")

@app.route('/abuse_detection')
def abuse_detection():
    return render_template("/abuse.html")

@app.route('/perform_abuse_detection', methods = ['POST'])
def perform_abuse_detection():
    text = request.form.get('abusetext')
    response = abuse.detect_abuse(text)
    result = []
    if response['label']=='LABEL_1':
        result.append({'detect': 'abuse detected','confidence':response['score'] })
    else:
        result.append({'detect': 'abuse not detected','confidence':response['score'] })
    return render_template("/abuse.html", result = result)

if __name__ == "__main__":
    app.run(debug=True)