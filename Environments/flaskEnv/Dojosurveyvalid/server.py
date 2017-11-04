from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "Hey, very sneaky sneaky"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=["POST"])
def process():
    if len(request.form['name']) < 1 or len(request.form['comment']) > 120 or len(request.form['comment']) < 1:
        flash("Invalid input! Check that you entered your name, and that your comment is limited to 120 characters.")
        return redirect('/')
    return render_template('process.html', name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])


app.run(debug=True)
