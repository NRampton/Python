from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users/<username>')
def show_user_profile(username):
    print username
    # return redirect('/')
    return render_template("name.html", name=username)


# @app.route('/users', methods=['POST'])
# def create_user():
#     print "Got POST info"
#     print request.form
#     name = request.form['name']
#     email = request.form['email']
#     return redirect('/')


app.run(debug=True)
