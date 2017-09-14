from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def style():
    return render_template('my_style_sheet.html')
app.run(debug=True)