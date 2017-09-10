from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def ninjas():
    return render_template('disappearingNinjas2.html')

@app.route('/ninja')
def all():
    return render_template('allNinjas.html')

@app.route('/ninja/<color>')
def color(color):
    if color == "blue":
        return render_template('leo.html')
    elif color == "red":
        return render_template('raph.html')
    elif color == "purple":
        return render_template('donatello.html')
    elif color == "orange":
        return render_template('mike.html')
    else:
        return render_template('notANinja.html')

app.run(debug=True)