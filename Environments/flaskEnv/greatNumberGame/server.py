from flask import Flask, render_template, redirect, session, request
from random import randint
app = Flask(__name__)
app.secret_key = "AVeryVeryVerySecretKy"


@app.route('/', methods=['GET', 'POST'])
def index():
    session['target'] = randint(0,20)
    session['counter'] = 0
    print session['target']
    return render_template('index.html')


@app.route('/guess', methods=["POST"])
def guess():
    session['counter'] += 1
    guess = int(request.form['player_guess'])
    print guess
    print session['target']
    print guess > session['target']
    if guess > 20 or guess < 1:
        return render_template('feedback.html', guess=guess, feedback="crazy", counter=session['counter'])
    elif guess > session['target']:
        return render_template('feedback.html', guess=guess, feedback="high", counter=session['counter'])
    elif guess < session['target']:
        return render_template('feedback.html', guess=guess, feedback="low", counter=session['counter'])
    elif guess == session['target']:
        return render_template('success.html', target=session['target'], counter=session['counter'])


app.run(debug=True)
