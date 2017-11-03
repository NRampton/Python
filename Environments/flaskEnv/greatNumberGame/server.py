from flask import Flask, render_template, redirect, session, request
from random import randint
app = Flask(__name__)
app.secret_key = "AVeryVeryVerySecretKy"


@app.route('/', methods=['GET', 'POST'])
def index():
    session['target'] = randint(1,100)
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
    if guess > 100 or guess < 1:
        return render_template('feedback.html', feedback="Did you read the directions?", counter=session['counter'])
    elif guess > session['target']:
        return render_template('feedback.html', feedback="Too high!", counter=session['counter'])
    elif guess < session['target']:
        return render_template('feedback.html', feedback="Too low!", counter=session['counter'])
    elif guess == session['target']:
        return render_template('success.html', target=session['target'], counter=session['counter'])


app.run(debug=True)
