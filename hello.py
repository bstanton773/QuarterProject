from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brian'}
    posts = [
        {
            'title': {'main': 'I hate Python', 'sub': 'this is a sad story'},
            'body': 'Python can do every thing. However, it is very hard'
        },
        {
            'title': {'main': 'I love Python', 'sub': 'this is a happy story'},
            'body': 'Python can do every thing. However, it is very easy'
        },
        {
            'title': {'main': 'I love C++', 'sub': 'this is a happy story'},
            'body': 'C++ can do some things. However, it is very silly'
        }
    ]

    return render_template('index.html', user = user, posts = posts, title = "Hello friend")

@app.route('/club')
def club():
    plans = [
        {
            'title': 'Platinum',
            'price': 1000
        },
        {
            'title': 'Gold',
            'price': 750
        },
        {
            'title': 'Silver',
            'price': 500
        },
        {
            'title': 'Bronze',
            'price': 250
        }
    ]
    return render_template('club.html', plans = plans)

app.run()