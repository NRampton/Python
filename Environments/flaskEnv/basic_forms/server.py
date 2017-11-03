from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "Hey, this is one very sneaky secrt key!"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=["POST"])
def process():
    # Validations go here
    return redirect('/')


app.run(debug=True)
