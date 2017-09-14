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
