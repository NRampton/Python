from flask import Flask, render_template, redirect, request, session
from random import randint
app = Flask(__name__)
app.secret_key = "ThisIsAnExtremlySecretK3y"


@app.route('/', methods=['Post', 'Get'])
def index():
    if not session:
        session['gold'] = 0
        session['log'] = ""
    return render_template('index.html', gold=session['gold'], log=session['log'])


@app.route('/process_money', methods=['POST', 'GET'])
def process_money():
    if request.form['building'] == "farm":      # the farm
        earnings = randint(10,20)
        session['gold'] += earnings
        session['log'] += "You earned {} gold working on the farm<br>".format(earnings)
    if request.form['building'] == "cave":      # the cave
        earnings = randint(5, 10)
        session['gold'] += earnings
        session['log'] += "You found {} gold exploring a cave<br>".format(earnings)
    if request.form['building'] == "house":     # the house
        earnings = randint(2, 5)
        session['gold'] += earnings
        session['log'] += "You earned {} gold working from home<br>".format(earnings)
    if request.form['building'] == "casino":        #the casino
        earnings = randint(-50, 50)
        session['gold'] += earnings
        if earnings < 0:
            session['log'] += "Drat, you lost {} gold at the casino. Maybe that will teach you.<br>".format(earnings)
        else:
            session['log'] += "All right, you won {} gold at the casino. Now quite while you're ahead!<br>".format(earnings)
    return redirect('/')


app.run(debug=True)
