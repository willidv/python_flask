from flask import Flask, render_template, request, redirect, session, flash

import re
app = Flask(__name__)
app.secret_key = 'secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def registration():
    return render_template('/Registration.html')

@app.route('/info', methods=['POST'])
def registered():
    validated = False
    if len(request.form['first_name']) < 1:
        flash("your first name isn't blank")
        validated = True
    if len(request.form['last_name']) < 1:
        flash("your last name isn't blank")
        validated = True
    if len(request.form['email']) < 1:
        flash("You know you're email isn't blank")
        validated = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash("You know you're email isn't " + request.form['email'])
        validated = True
    if len(request.form['password']) < 1:
        flash("your password can't be blank")
        validated = True
    if len(request.form['password']) < 8:
        flash("your password isn't long enough")
        validated = True
    if request.form['password'] != request.form['confirmed']:
        flash('Your password and confirmation do not match')
        validated = True
    if validated:
        flash("Please fill out the following form correctly")
    else:
        flash("Success!! Thank you for filling out this form")
    return redirect('/')

app.run(debug=True)