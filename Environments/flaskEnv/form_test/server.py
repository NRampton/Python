from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSoSoSecret"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users', methods=["POST"])
def show_user_profile():
    print "Got Post info"
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/user')


@app.route('/user')
def show_user():
    return render_template('user.html', name=session['name'], email=session['email'])


app.run(debug=True)
