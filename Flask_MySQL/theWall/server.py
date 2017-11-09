from flask import Flask, session, flash, redirect, render_template, request
import re
import md5
from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = "Hey, let's not keep this a secret. It's great. HEY, EVERYBODY! HERE'S THE SECRET KEY!"
NUM_REGEX = re.compile('[0-9]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnection(app, 'theWall')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    errors = 0
    email_list = mysql.query_db("SELECT email FROM users")
    for key in email_list:
        if key['email'] == request.form['email']:
            flash("That email already exists in our records. Pick another. Forgot your email? Too bad.")
            errors += 1
            break
    for key in request.form:
        if len(request.form[key]) < 1:
            flash("All fields in this form are required.")
            errors += 1
            break
    if len(request.form['first_name']) < 2:
        flash("First name must be at least two characters long.")
        errors += 1
    if len(request.form['last_name']) < 2:
        flash("Last name must be at least two characters long.")
        errors += 1
    if not EMAIL_REGEX.match(request.form['email']):
        flash("We're going to need a valid email address.")
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
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long (and, honestly, the longer the better).")
        errors += 1
    if not request.form['password'] == request.form['confirm_password']:
        flash("Password and Password Confirmation fields need to match, so we know which one you really meant to type.")
    if errors > 0:
        return redirect('/')
    else:
        query = ("INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())")
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': md5.new(request.form['password']).hexdigest()
        }
        mysql.query_db(query, data)
        session.id = mysql.query_db("SELECT id FROM users WHERE first_name = {}".format(data['first_name']))
        return redirect('/wall')


@app.route('/login', methods=['POST'])
def login():
    full_users = mysql.query_db("SELECT * FROM users")
    for entry in full_users:
        if entry['email'] == request.form['email'] and entry['password'] == md5.new(request.form['password']).hexdigest():
            session.id = entry['id']
            return redirect('/wall')
    flash("Sorry, those login credentials don't match anything in our records. Please try again.")
    return redirect('/')


@app.route('/wall')
def success():
    return render_template('wall.html')


@app.route('/message')
def message():
    return redirect('/wall')


@app.route('/comment')
def comment():
    return redirect('wall')


app.run(debug=True)
