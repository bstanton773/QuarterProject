from app import app
from app.forms import LoginForm
from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user

from app.models import Post, User

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():  # post and submit validate
        # get the user from data base use code
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title = 'Sign In', form = form) # GET or submit validate Failed

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))