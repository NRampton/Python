from flask import Flask, redirect, request, render_template, session
from mysqlconnection import MySQLConnection
app = Flask(__name__)
app.secret_key = "Nobody is ever going to guess this very, VERY sneaky secret key."
mysql = MySQLConnection(app, 'emails')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validate', methods=['POST'])           # Takes email from index.html/error.html and
def validate():
    requested = "INSERT INTO logged_queries (email_requested, created_at) VALUES (:email, NOW())"
    data = {'email': request.form['email']}
    mysql.query_db(requested, data)
    full_log = mysql.query_db("SELECT * FROM logged_queries")
    valid = False
    query = mysql.query_db("SELECT * FROM emails")
    for row in query:                               # checks it against the results of the query,
        if row['email'] == request.form['email']:
            valid = True
    if valid:                                       # rendering the appropriate template
        return render_template('success.html', email=request.form['email'], log=full_log)
    else:
        return render_template('error.html')


@app.route('/delete', methods=['POST'])
def buhleeted():
    query = "DELETE FROM emails WHERE email = :email"
    data = {'email': request.form['email']}
    mysql.query_db(query, data)
    return render_template('deleted.html', deleted=request.form['email'])


app.run(debug=True)
