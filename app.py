from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_jovian():
    return render_template('home.html')


app.run(host='0.0.0.0', debug=True)