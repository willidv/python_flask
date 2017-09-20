from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def survey():
    return render_template("DojoSurvey.html")
@app.route('/info', methods=['POST'])
def info():
    validated = False
    if len(request.form['name']) < 1:
        flash("your name isn't blank")
        validated = True
    if len(request.form['comment']) > 120:
        flash("Try to cut it down a bit")
        validated = True
    if validated:
        return redirect('/')
    else:
        return render_template('submissions.html', name = request.form['name'], location = request.form['location'], language = request.form['language'], comments = request.form['comments'] )   
app.run(debug=True)