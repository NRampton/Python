from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=["POST", "GET"])
def process():
    print "Got the info"
    return redirect('/results', name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])


@app.route('/results')
def results():
    return render_template('results.html')


app.run(debug=True)
