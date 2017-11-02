from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def display_root():
    return render_template('port_main.html')


@app.route('/projects')
def display_projects():
    return render_template('port_projects.html')


@app.route('/about')
def display_about():
    return render_template('port_about.html')


app.run(debug=True)
