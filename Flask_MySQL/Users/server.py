from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnection
app = Flask(__name__)
mysql = MySQLConnection(app, 'users')


@app.route('/')
def redirect_root():
    return redirect('/users')

@app.route('/users')
def index():
    query = mysql.query_db("SELECT id, concat(first_name, ' ', last_name) as full_name, email, DATE_FORMAT(created_at, '%M %D, %Y') AS created_at FROM users")
    return render_template('index.html', query=query)


@app.route('/users/new')
def new():
    return render_template('users_new.html')


@app.route('/users/<id>/edit')
def edit(id):
    query = mysql.query_db("SELECT * FROM users WHERE id='{}'".format(id))
    return render_template('users_edit.html', id=id, query=query)


@app.route('/users/<id>', methods=['GET'])
def show(id):
    query = mysql.query_db("SELECT concat(first_name, ' ', last_name) as full_name, email, DATE_FORMAT(created_at, '%M %D, %Y') AS created_at FROM users WHERE id='{}'".format(id))
    return render_template('users_show.html', id=id, query=query)


@app.route('/users/<id>', methods=['POST'])
def update(id):
    return redirect('/users/{}}'.format(id))


@app.route('/users/create', methods=['POST'])
def create():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    id_result = mysql.query_db("SELECT id FROM users WHERE email='{}'".format(request.form['email']))
    return redirect('/users/{}'.format(id_result[0]['id']))


@app.route('/users/<id>/destroy')
def destroy(id):
    mysql.query_db("DELETE FROM users WHERE id='{}'".format(id))
    return redirect('/users')


app.run(debug=True)
