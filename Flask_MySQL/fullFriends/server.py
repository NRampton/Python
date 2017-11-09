from flask import Flask, session, redirect, render_template, request
from mysqlconnection import MySQLConnection
app = Flask(__name__)
app.secret_key = 'Wow, that is one genuinely secret key!'
mysql = MySQLConnection(app, 'full_friends')


@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html', friends_list=friends)


@app.route('/add_friend', methods=['POST'])
def add_friend():
    query = "INSERT INTO friends (first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
