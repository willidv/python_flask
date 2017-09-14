from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def survey():
    return render_template("DojoSurvey.html")

@app.route('/info', methods=['POST'])
def info():
    return render_template('submissions.html', name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['language'])
    
app.run(debug=True)