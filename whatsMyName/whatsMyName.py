<<<<<<< HEAD
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def name():
    return render_template('whatsMyName.html')

@app.route('/process', methods=['POST'])
def process():
    print "name " + request.form['name']
    return redirect('/')

app.run(debug=True)
=======
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def name():
    return render_template('whatsMyName.html')

@app.route('/process', methods=['POST'])
def process():
    print "name " + request.form['name']
    return redirect('/')

app.run(debug=True)
>>>>>>> e4f57a3582f4e5110e052ec4118556e8dd61e2da
