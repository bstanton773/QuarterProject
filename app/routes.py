from app import app
from app.forms import LoginForm
from flask import render_template, redirect, flash

from app import Post

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brian'}
    posts = Post.query.all()
    return render_template('index.html', user=user, posts = posts, title='A title')

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

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form = form)