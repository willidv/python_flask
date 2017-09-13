from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def counter():
    session['count'] += 1
    return render_template('counter.html',number=session['count'])

@app.route('/counter.html')
def counted():
    return redirect('/')

app.run(debug=True)