from flask import Flask, render_template, redirect, flash, session, request

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/', methods=['GET'])
def index():
    return render_template('/advanced_validation.html')

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("You know you're email isn't blank")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("You know you're email isn't " + request.form['email'])
    else:
        flash("success!!")
    return redirect('/')

app.run(debug=True)