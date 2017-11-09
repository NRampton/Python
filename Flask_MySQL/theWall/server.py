from flask import Flask, session, flash, redirect, render_template, request
import re
import md5
from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = "Hey, let's not keep this a secret. It's great. HEY, EVERYBODY! HERE'S THE SECRET KEY!"
NUM_REGEX = re.compile('[0-9]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnection(app, 'wall')


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
    if len(request.form['username']) < 2:
        flash("Last name must be at least two characters long.")
        errors += 1
    if not EMAIL_REGEX.match(request.form['email']):
        flash("We're going to need a valid email address.")
        errors += 1
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long (and, honestly, the longer the better).")
        errors += 1
    if not request.form['password'] == request.form['confirm_password']:
        flash("Password and Password Confirmation fields need to match, so we know which one you really meant to type.")
    if errors > 0:
        return redirect('/')
    else:
        query = ("INSERT INTO users (username, email, password, created_at, updated_at) VALUES (:username, :email, :password, NOW(), NOW())")
        data = {
            'username': request.form['username'],
            'email': request.form['email'],
            'password': md5.new(request.form['password']).hexdigest()
        }
        mysql.query_db(query, data)
        query2 = "SELECT users.id FROM users WHERE email='{}'".format(request.form['email'])
        id_result = mysql.query_db(query2)
        session['id'] = int(id_result[0]['id'])
        print session['id']
        return redirect('/wall')


@app.route('/login', methods=['POST'])
def login():
    query = mysql.query_db("SELECT * FROM users")
    for entry in query:
        if entry['email'] == request.form['email'] and entry['password'] == md5.new(request.form['password']).hexdigest():
            session['id'] = entry['id']
            print session['id']
            return redirect('/wall')
    flash("Sorry, those login credentials don't match anything in our records. Please try again.")
    return redirect('/')


@app.route('/wall')
def wall():
    print session['id']
    query = mysql.query_db("SELECT messages.content AS message, messages.id AS message_id, messages.created_at AS message_time, users.username AS user FROM messages JOIN users ON messages.user_id = users.id")
    query2 = mysql.query_db("SELECT comments.content AS comment, comments.created_at AS comment_time, users.username AS user, messages.id AS message_id FROM comments JOIN messages ON messages.id = comments.message_id JOIN users ON users.id = comments.user_id")
    return render_template('wall.html', query=query, query2=query2)


@app.route('/message', methods=['POST'])
def message():
    query = ("INSERT INTO messages (content, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())")
    data = {
        'message': request.form['message'],
        'user_id': session['id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')


@app.route('/comment', methods=['POST'])
def comment():
    print request.form
    query = ("INSERT INTO comments (content, user_id, message_id, created_at, updated_at) VALUES (:comment, :user_id, :message_id, NOW(), NOW())")
    data = {
        'comment': request.form['comment'],
        'user_id': session['id'],
        'message_id': request.form['message_id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')


@app.route('/log_off')
def log_off():
    session['id'] = 0
    return redirect('/')


app.run(debug=True)
