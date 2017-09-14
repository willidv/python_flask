from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def game():
    session['number'] = random.randrange(0,101)
    print session['number']
    return render_template("/numbersGame.html")

@app.route('/guess', methods=['POST'])
def choose():
    session['choice'] = int(request.form['number'])
    print session['choice']
    if session['choice'] > session['number']:
        return render_template("/numbersGame.html", answer="Too High")
    if session['choice'] < session['number']:
        return render_template('/numbersGame.html', answer = "Too Low")
    elif session['choice'] == session['number']:
        return redirect('/guessed')

@app.route('/guessed')
def guessed():
    session['number'] = random.randrange(0,101)
    print session['number']
    return render_template("/numbersGame.html",answer="THATS CORRECT...next number!!")
    

app.run(debug=True)
