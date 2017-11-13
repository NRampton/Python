from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/lightroom")
def lightroom():
    return render_template('lightroom.html')


@app.route('/fumble')
def fumble():
    return render_template('fumble.html')


@app.route('/hallway')
def hallway():
    return render_template('hallway.html')


@app.route('/behind')
def behind():
    return render_template('behind.html')


@app.route('/room1')
def room1():
    return render_template('room1.html')


@app.route('/room2')
def room2():
    return render_template('room2.html')


@app.route('/room3')
def room3():
    return render_template('room3.html')


@app.route('/room4')
def room4():
    return render_template('room4.html')


@app.route('/room5')
def room5():
    return render_template('room5.html')


app.run( host='0.0.0.0', debug=True)
