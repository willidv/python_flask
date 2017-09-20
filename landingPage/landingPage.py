<<<<<<< HEAD
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

=======
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

>>>>>>> e4f57a3582f4e5110e052ec4118556e8dd61e2da
app.run(debug=True)