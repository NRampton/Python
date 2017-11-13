from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "HereisaverySecretKey"


@app.route('/', methods=["POST"])
def index():
    if session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html', counter=session['counter'])


@app.route('/add', methods=["POST"])
def add():
    session['counter'] += 1
    return redirect('/')


@app.route('/reset', methods = ['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')


app.run(debug=True)


# I need a variable that can count the numbe of times index() has run, but it has to be declared
# outside of index(), and there doesn't seem to be anywhere outside of index() that can store it.
