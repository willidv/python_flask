from flask import Flask, render_template, redirect, session, request, flash
import random

app = Flask(__name__)

app.secret_key = "secret"

@app.route('/')
def game():
    if session.get('gold') == None:
        session['gold'] = 0
    session['message'] = ""
    print session['gold']
    return render_template('/ninjaGold.html')

@app.route('/process_money', methods=['POST'])
def farm():
    if request.form['building'] == "farm":
        num1 = random.randrange(10,21)
        session['gold'] += num1
        flash("you have earned " + str(num1) + " gold from the farm!")
        print session['message']
    elif request.form['building'] == "cave":
        num2 = random.randrange(5,11)
        session['gold'] += num2
        flash("you have earned " + str(num2) + " gold from the house!")
    elif request.form['building'] == "house":
        num3 = random.randrange(2,6)
        session['gold'] += num3
        flash("you have earned " + str(num3) + " gold from the cave!")
    elif request.form['building'] == "casino":
        chance = random.randrange(0,101) 
        if chance < 50:
            num4 = random.randrange(0,51)
            session['gold'] -= num4
            flash("you have lost " + str(num4) + " gold from the casino!")
        elif chance > 49:
            num5 = random.randrange(0,51)
            session['gold'] += num5
            flash("you have earned " + str(num5) + " gold from the casino!")
    return redirect('/')


app.run(debug=True)