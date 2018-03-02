from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brian'}
    return render_template('index.html', user = user)

app.run()