from flask import Flask, render_template, request, redirect, flash
import re
import datetime

app = Flask(__name__)
app.secret_key = "Hey, let's not keep this a secret. It's great."
NUM_REGEX = re.compile('[0-9]')
CAP_REGEX = re.compile('[A-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
BIRTHDAY_REGEX = re.compile('[0-9]{2}/[0-9]{2}/[0-9]{4}')
today = datetime.date.today()
today_formatted = today.strftime('%m/%d/%Y')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    errors = 0
    print request.form
    for key in request.form:
        if len(request.form[key]) < 1:
            flash("All fields in this form are required, but something got left blank.")
            errors += 1
            break
    if not EMAIL_REGEX.match(request.form['email']):
        flash("We're going to need a valid email address. How else will we stay in contact about your account?")
        errors += 1
    for char in range(len(request.form['first_name'])):
        if NUM_REGEX.match(request.form['first_name'][char]):
            flash("No numbers are allowed in first names.")
            errors += 1
            break
    for char in range(len(request.form['last_name'])):
        if NUM_REGEX.match(request.form['last_name'][char]):
            flash("No numbers are allowed in last names.")
            errors += 1
            break
    if not BIRTHDAY_REGEX.match(request.form['birthday']):
        flash('Please check the format of your birth date.')
        errors += 1
    if not CAP_REGEX.search(request.form['password']):
        flash("Your password needs to include at least one capital letter.")
        errors += 1
    if not NUM_REGEX.search(request.form['password']):
        flash("Your password needs to include at least one number.")
        errors += 1
    if len(request.form['password']) < 8 or len(request.form['confirm_password']) < 8:
        flash("Password must be at least 8 characters long (and, honestly, the longer the better).")
        errors += 1
    if not request.form['password'] == request.form['confirm_password']:
        flash("Password and Password Confirmation fields need to match, so we know which one you really meant to type.")
    if errors > 0:
        return redirect('/')
    else:
        return render_template('success.html')


app.run(debug=True)

# Want to go through each character. If there isn't a capital letter or there isn't a number,
# we want to throw an error telling them to make their password stronger. re.search()!
