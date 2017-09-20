from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('basic_validation_form.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash("your name isn't blank")
    else:
        flash("oh so you think you're real clever do ya, " + request.form['name'])
    return redirect('/')

app.run(debug=True)